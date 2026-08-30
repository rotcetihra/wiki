# longjmp

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<setjmp.h>|<setjmp.h>]] / longjmp

[[Языки программирования/C/Библиотеки/<setjmp.h>/setjmp|Назад]] | [[Языки программирования/C/Библиотеки/<setjmp.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<signal.h>/sig_atomic_t|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <setjmp.h>

_Noreturn void longjmp(jmp_buf env, int val);
```

## Описание

Функция `longjmp` восстанавливает контекст выполнения программы из буфера `env`, ранее сохранённого вызовом `setjmp`. После вызова `longjmp` выполнение продолжается так, как если бы соответствующий `setjmp` вернул значение `val`.

Если `val` равно 0, функция `longjmp` возвращает 1 (для обеспечения уникальности возвращаемого значения). Функция не возвращает управление вызывающему коду — выполнение продолжается в точке, соответствующей сохранённому контексту.

> [!WARNING]
> Поведение не определено, если:
> - буфер `env` не был инициализирован вызовом `setjmp`;
> - функция, в которой был вызван `setjmp`, завершилась до вызова `longjmp`;
> - в области видимости с автоматическими переменными были изменены переменные после `setjmp` (кроме случаев, определённых стандартом).
>
> Использование `longjmp` приводит к утечке памяти, если между `setjmp` и `longjmp` были выделены ресурсы (память, файловые дескрипторы и т. д.).

## Примеры

### Базовый пример

```c
#include <stdio.h>
#include <setjmp.h>

jmp_buf buf;

void cleanup(void)
{
    printf("Очистка ресурсов\n");
    longjmp(buf, 42);
}

int main(void)
{
    int result = setjmp(buf);
    if (result == 0) {
        printf("Начало работы\n");
        cleanup();
    } else {
        printf("Возврат через longjmp с кодом %d\n", result);
    }
    return 0;
}
```

### Обработка ошибок с кодом возврата

```c
#include <stdio.h>
#include <stdlib.h>
#include <setjmp.h>

jmp_buf error_jmp;

enum ErrorCode {
    ERR_OK = 0,
    ERR_ALLOC = 1,
    ERR_READ = 2,
    ERR_WRITE = 3
};

void read_data(void)
{
    /* Имитация ошибки чтения */
    longjmp(error_jmp, ERR_READ);
}

void process_data(void)
{
    read_data();
    longjmp(error_jmp, ERR_WRITE);
}

int main(void)
{
    int err = setjmp(error_jmp);
    switch (err) {
        case ERR_OK:
            printf("Запуск обработки...\n");
            process_data();
            break;
        case ERR_ALLOC:
            fprintf(stderr, "Ошибка выделения памяти\n");
            return 1;
        case ERR_READ:
            fprintf(stderr, "Ошибка чтения данных\n");
            return 2;
        case ERR_WRITE:
            fprintf(stderr, "Ошибка записи данных\n");
            return 3;
        default:
            fprintf(stderr, "Неизвестная ошибка %d\n", err);
            return 99;
    }
    return 0;
}
```

### Использование siglongjmp для восстановления маски сигналов (POSIX)

```c
#include <stdio.h>
#include <setjmp.h>
#include <signal.h>
#include <unistd.h>

sigjmp_buf sig_buf;
volatile sig_atomic_t caught = 0;

void sig_handler(int sig)
{
    caught = 1;
    siglongjmp(sig_buf, sig);
}

int main(void)
{
    struct sigaction sa = {0};
    sa.sa_handler = sig_handler;
    sigemptyset(&sa.sa_mask);
    sigaction(SIGINT, &sa, NULL);
    sigaction(SIGTERM, &sa, NULL);

    if (sigsetjmp(sig_buf, 1) == 0) {
        printf("Ожидание сигналов (PID: %d)...\n", getpid());
        while (!caught) pause();
    } else {
        printf("Получен сигнал %d, маска восстановлена\n", caught);
    }
    return 0;
}
```

### Корректная работа с volatile переменными

```c
#include <stdio.h>
#include <setjmp.h>

jmp_buf buf;
volatile int counter = 0;      /* volatile — сохраняет значение после longjmp */
int normal_var = 0;            /* обычное — значение неопределено после longjmp */

void modify_vars(void)
{
    counter++;
    normal_var++;
    longjmp(buf, 1);
}

int main(void)
{
    int result = setjmp(buf);
    if (result == 0) {
        printf("До longjmp: counter=%d, normal=%d\n", counter, normal_var);
        modify_vars();
    } else {
        printf("После longjmp: counter=%d (volatile), normal=%d (UB!)\n",
               counter, normal_var);
    }
    return 0;
}
```

### Имитация деструкторов (cleanup при longjmp)

```c
#include <stdio.h>
#include <stdlib.h>
#include <setjmp.h>

typedef void (*cleanup_fn)(void *);
struct cleanup_entry { cleanup_fn fn; void *arg; struct cleanup_entry *next; };

static struct cleanup_entry *cleanups = NULL;
static jmp_buf exit_buf;

void register_cleanup(cleanup_fn fn, void *arg)
{
    struct cleanup_entry *e = malloc(sizeof *e);
    e->fn = fn; e->arg = arg; e->next = cleanups; cleanups = e;
}

void run_cleanups(void)
{
    while (cleanups) {
        cleanups->fn(cleanups->arg);
        struct cleanup_entry *next = cleanups->next;
        free(cleanups);
        cleanups = next;
    }
}

void my_cleanup(void *arg)
{
    printf("Очистка: %s\n", (char *)arg);
}

void risky(void)
{
    register_cleanup(my_cleanup, "файл");
    register_cleanup(my_cleanup, "сокет");
    longjmp(exit_buf, 1);
}

int main(void)
{
    if (setjmp(exit_buf) == 0) {
        risky();
    } else {
        run_cleanups();
        printf("Все ресурсы освобождены\n");
    }
    return 0;
}
```

## Параметры

| Параметр | Описание |
|---|---|
| `env` | Буфер, сохранённый ранее вызовом `setjmp` |
| `val` | Значение, которое будет возвращено `setjmp` при восстановлении контекста (если 0, возвращается 1) |

## Возвращаемое значение

Функция `longjmp` не возвращает управление — она передаёт его в точку, соответствующую ранее вызванному `setjmp`.

> [!NOTE]
> Модификатор `_Noreturn` (C11) указывает, что функция не возвращает управления. Это позволяет компилятору выявлять ошибки использования (например, пропущенный `setjmp`).

> [!INFO]
> POSIX добавляет функцию `siglongjmp`, которая работает аналогично `longjmp`, но также восстанавливает маску сигналов, если соответствующий `sigsetjmp` был вызван с ненулевым вторым аргументом. BSD предоставляет `_longjmp`/`_setjmp` без сохранения маски сигналов для совместимости.

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Позволяет немедленно выйти из глубоко вложенных функций | Опасен при наличии автоматических переменных |
| Прост в использовании с `setjmp` | Может привести к утечкам памяти |
| Подходит для обработки критических ошибок | Непереносим (依赖 от реализации) |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<setjmp.h>/setjmp|setjmp]] — сохранение контекста в `jmp_buf`
- [[Языки программирования/C/Библиотеки/<setjmp.h>/jmp_buf|jmp_buf]] — тип буфера для сохранения контекста
- [[Языки программирования/C/Библиотеки/<signal.h>/sig_atomic_t|sig_atomic_t]] — атомарный тип для обработки сигналов

## Обработка ошибок

- **Поведение при передаче NULL:** поведение не определено. Буфер `env` должен быть инициализирован вызовом `setjmp`.
- **Установление errno:** функция не устанавливает `errno`.
- **Возвращаемое значение при ошибке:** функция не возвращает управления вызывающему коду — она передаёт его в точку, соответствующую ранее вызванному `setjmp`. Если `val` равно 0, `setjmp` получит значение 1.
- **Многопоточность:** функция не является потокобезопасной. `longjmp` должен восстанавливать контекст в том же потоке, в котором был вызван `setjmp`.
- **Связанные функции:** `setjmp` — сохранение контекста; `jmp_buf` — тип буфера. В POSIX: `siglongjmp` — аналог с восстановлением маски сигналов.

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.13.2.1
- GNU C Library, заголовочный файл `setjmp.h`
