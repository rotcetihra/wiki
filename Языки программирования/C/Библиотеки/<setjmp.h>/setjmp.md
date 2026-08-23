# setjmp

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<setjmp.h>|<setjmp.h>]] / setjmp

[[Языки программирования/C/Библиотеки/<setjmp.h>/jmp_buf|Назад]] | [[Языки программирования/C/Библиотеки/<setjmp.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<setjmp.h>/longjmp|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <setjmp.h>

int setjmp(jmp_buf env);
```

## Описание

Макрос `setjmp` сохраняет текущий контекст выполнения программы (указатель стека, программный счётчик и сохраняемые регистры) в буфер `env` и возвращает 0.

Если `setjmp` вызывается повторно (после восстановления контекста через `longjmp`), макрос возвращает значение, переданное вторым аргументом `longjmp` (или 0, если передано 0).

> [!WARNING]
> `setjmp` является макросом, а не функцией. Его вызов может привести к неопределённому поведению, если:
> - буфер `env` не инициализирован вызовом `setjmp`;
> - вызов происходит не в теле или не в вычислении условного оператора (`if`, `while`, `for`, `switch`) или тернарного оператора (`?:`);
> - после вызова `setjmp` функция, в которой он был вызван, завершилась (стек развернут).

> [!INFO]
> POSIX предоставляет макрос `sigsetjmp`, который работает аналогично `setjmp`, но может также сохранять маску сигналов (если второй аргумент ненулевой). Соответствующая функция восстановления — `siglongjmp`.

## Примеры

### Базовый пример

```c
#include <stdio.h>
#include <setjmp.h>

jmp_buf environment;

int main(void)
{
    int result = setjmp(environment);
    if (result == 0) {
        printf("Начало работы. result = %d\n", result);
        /* здесь можно вызвать функцию, которая вызовет longjmp */
    } else {
        printf("Восстановлено. result = %d\n", result);
    }
    return 0;
}
```

### Вложенные вызовы setjmp

```c
#include <stdio.h>
#include <setjmp.h>

jmp_buf outer, inner;

void inner_function(void)
{
    if (setjmp(inner) == 0) {
        printf("Внутренний setjmp\n");
        longjmp(outer, 99);  /* Переход сразу к внешнему */
    } else {
        printf("Внутренний восстановлен\n");
    }
}

int main(void)
{
    if (setjmp(outer) == 0) {
        printf("Внешний setjmp\n");
        inner_function();
    } else {
        printf("Внешний восстановлен с кодом %d\n", 99);
    }
    return 0;
}
```

### Обработка ошибок без исключений (try-catch паттерн)

```c
#include <stdio.h>
#include <stdlib.h>
#include <setjmp.h>
#include <string.h>

typedef struct {
    jmp_buf buf;
    int has_error;
    int error_code;
    char error_msg[256];
} try_context;

#define TRY(ctx)     if ((ctx)->has_error = setjmp((ctx)->buf) == 0)
#define CATCH(ctx)   else
#define THROW(ctx, code, msg) do { \
    strncpy((ctx)->error_msg, (msg), sizeof((ctx)->error_msg) - 1); \
    (ctx)->error_code = (code); \
    longjmp((ctx)->buf, (code)); \
} while (0)

void risky_operation(try_context *ctx, int fail)
{
    if (fail) THROW(ctx, 1, "Ошибка выделения памяти");
    if (fail == 2) THROW(ctx, 2, "Ошибка чтения файла");
    printf("Операция успешна\n");
}

int main(void)
{
    try_context ctx = {0};
    
    TRY(&ctx) {
        risky_operation(&ctx, 1);
    } CATCH(&ctx) {
        printf("Перехвачено: [%d] %s\n", ctx.error_code, ctx.error_msg);
    }
    
    TRY(&ctx) {
        risky_operation(&ctx, 0);
    } CATCH(&ctx) {
        printf("Перехвачено: [%d] %s\n", ctx.error_code, ctx.error_msg);
    }
    
    return 0;
}
```

### Использование с циклами

```c
#include <stdio.h>
#include <setjmp.h>
#include <signal.h>

jmp_buf loop_buf;
volatile sig_atomic_t stop = 0;

void handler(int sig)
{
    stop = 1;
    longjmp(loop_buf, 1);
}

int main(void)
{
    signal(SIGINT, handler);
    
    if (setjmp(loop_buf) == 0) {
        printf("Запуск бесконечного цикла (Ctrl+C для выхода)\n");
        while (!stop) {
            /* полезная работа */
        }
    }
    printf("Цикл прерван\n");
    return 0;
}
```

## Параметры

| Параметр | Описание |
|---|---|
| `env` | Буфер для сохранения контекста, объявленный как `jmp_buf` |

## Возвращаемое значение

| Значение | Описание |
|---|---|
| `0` | При первом вызове (сохранение контекста) |
| Ненулевое значение | При восстановлении через `longjmp` (значение второго аргумента `longjmp`) |

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Простой механизм сохранения контекста | Возвращает разные значения при первом и повторном вызове |
| Позволяет реализовать подобие исключений | Ограничения на контекст вызова |
| Может использоваться повторно с одним буфером | Является макросом — не является функцией |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<setjmp.h>/longjmp|longjmp]] — восстановление контекста из `jmp_buf`
- [[Языки программирования/C/Библиотеки/<setjmp.h>/jmp_buf|jmp_buf]] — тип буфера для сохранения контекста

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.13.2.1
- GNU C Library, заголовочный файл `setjmp.h`
