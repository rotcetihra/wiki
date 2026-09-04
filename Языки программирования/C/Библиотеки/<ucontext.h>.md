# <ucontext.h>

[[Языки программирования/C/Библиотеки|Библиотеки]] / <ucontext.h>

**Дата написания:** 04.09.2026

## Оглавление

### Функции

- [[Языки программирования/C/Библиотеки/<ucontext.h>/getcontext|getcontext]] — получение текущего контекста
- [[Языки программирования/C/Библиотеки/<ucontext.h>/setcontext|setcontext]] — установка контекста
- [[Языки программирования/C/Библиотеки/<ucontext.h>/swapcontext|swapcontext]] — сохранение текущего и установка нового контекста
- [[Языки программирования/C/Библиотеки/<ucontext.h>/makecontext|makecontext]] — создание контекста для вызова функции

## Описание библиотеки

Заголовочный файл `<ucontext.h>` — поддержка переключения контекста уровня пользователя (System V ABI). Определяет функции для управления контекстами выполнения, используемые для кооперативного многозадачного переключения.

### Функции

| Функция | Описание |
|---|---|
| `getcontext(ucontext_t *ucp)` | Сохранение текущего контекста в `ucp` |
| `setcontext(const ucontext_t *ucp)` | Восстановление контекста из `ucp` |
| `swapcontext(ucontext_t *oucp, const ucontext_t *uccp)` | Сохранение текущего в `oucp` и переключение на `ucp` |
| `makecontext(ucontext_t *ucp, void (*func)(void), int argc, ...)` | Настройка контекста для вызова `func` с аргументами |

### Возвращаемое значение

- `getcontext()`, `setcontext()`, `swapcontext()`: `0` при успехе или -1 при ошибке.
- `makecontext()`: ничего не возвращает.

### Использование

```c
#include <ucontext.h>

static ucontext_t ctx_main, ctx_func;

static void func(void) {
    printf("Функция выполняется\n");
    swapcontext(&ctx_func, &ctx_main);
    printf("Функция возобновлена\n");
}

int main(void) {
    char stack[16384];
    getcontext(&ctx_func);
    ctx_func.uc_stack.ss_sp = stack;
    ctx_func.uc_stack.ss_size = sizeof(stack);
    ctx_func.uc_link = &ctx_main;
    makecontext(&ctx_func, func, 0);

    swapcontext(&ctx_main, &ctx_func);
    printf("Основной поток возобновлён\n");
    return 0;
}
```

## Исключения

- **NULL:** функции не принимают `NULL`.
- **getcontext():** возвращает -1 при ошибке.
- **setcontext():** не возвращает управление (переключает контекст).
- **makecontext():** аргументы должны быть `int`; для указателей используйте каст.
- **Стек:** контекст должен иметь выделенный стек (`uc_stack`).
- **Не POSIX POSIX:** функции были удалены из POSIX.1-2008, но доступны в glibc.
- **Многопоточность:** функции не потокобезопасны.

## Стандарты

System V ABI, glibc (удалены из POSIX.1-2008).

## Источники

- `/usr/include/ucontext.h`
- `/usr/include/sys/ucontext.h`

[[Языки программирования/C/Библиотеки|Содержание]]
