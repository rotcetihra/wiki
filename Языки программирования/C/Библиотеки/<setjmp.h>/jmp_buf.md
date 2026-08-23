# jmp_buf

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<setjmp.h>|<setjmp.h>]] / jmp_buf

[[Языки программирования/C/Библиотеки/<locale.h>/setlocale|Назад]] | [[Языки программирования/C/Библиотеки/<setjmp.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<setjmp.h>/setjmp|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <setjmp.h>

typedef /* unspecified */ jmp_buf;
```

## Описание

Тип `jmp_buf` — массив, способный хранить информацию о контексте стека, необходимую для восстановления программного состояния с помощью `longjmp`. Конкретная структура массива определяется реализацией и зависит от архитектуры.

Буфер `jmp_buf` используется совместно с макросом `setjmp` для сохранения текущего контекста и функцией `longjmp` для его восстановления. Одна переменная типа `jmp_buf` может использоваться многократно — например, для повторных попыток выполнения операции.

> [!NOTE]
> Тип `jmp_buf` должен быть достаточно большим, чтобы сохранить весь контекст стека — включая указатель стека, программный счётчик и регистры общего назначения. На некоторых платформах размер `jmp_buf` может достигать нескольких сотен байтов.

> [!WARNING]
> После восстановления контекста через `longjmp` значения автоматических (локальных) переменных в функции, вызвавшей `setjmp`, становятся неопределёнными, если они не объявлены как `volatile` и не были изменены между `setjmp` и `longjmp`. Для сохранения значений используйте `volatile` переменные или глобальные/статические переменные.

## Примеры

### Базовое использование

```c
#include <stdio.h>
#include <setjmp.h>

jmp_buf buf;

void deep_function(void)
{
    printf("Вызов deep_function\n");
    longjmp(buf, 1);
}

int main(void)
{
    if (setjmp(buf) == 0) {
        printf("Первый вызов setjmp\n");
        deep_function();
    } else {
        printf("Возврат через longjmp\n");
    }
    return 0;
}
```

### Использование нескольких буферов для обработки разных ошибок

```c
#include <stdio.h>
#include <stdlib.h>
#include <setjmp.h>

jmp_buf error_buf[3];
enum { ERR_MEMORY, ERR_FILE, ERR_NETWORK };

void allocate_memory(void)
{
    void *p = malloc(1000000000000UL);
    if (!p) longjmp(error_buf[ERR_MEMORY], 1);
}

void open_file(void)
{
    FILE *f = fopen("/nonexistent", "r");
    if (!f) longjmp(error_buf[ERR_FILE], 2);
}

int main(void)
{
    for (int i = 0; i < 3; ++i) {
        if (setjmp(error_buf[i]) == 0) {
            switch (i) {
                case ERR_MEMORY: allocate_memory(); break;
                case ERR_FILE:   open_file(); break;
                case ERR_NETWORK: printf("Сетевая ошибка\n"); longjmp(error_buf[ERR_NETWORK], 3);
            }
        } else {
            printf("Обработана ошибка #%d\n", i);
        }
    }
    return 0;
}
```

### Паттерн повторной попытки (retry)

```c
#include <stdio.h>
#include <setjmp.h>
#include <unistd.h>

jmp_buf retry_buf;
volatile int attempt = 0;

int unreliable_operation(void)
{
    /* Имитация нестабильной операции */
    if (attempt++ < 2) return -1;
    return 0;
}

int main(void)
{
    if (setjmp(retry_buf) == 0) {
        if (unreliable_operation() != 0) {
            printf("Попытка %d не удалась\n", attempt);
            sleep(1);
            longjmp(retry_buf, 1);
        }
    } else {
        printf("Повторная попытка %d\n", attempt);
        if (unreliable_operation() != 0) {
            longjmp(retry_buf, 1);
        }
    }
    printf("Операция успешна после %d попыток\n", attempt);
    return 0;
}
```

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Позволяет сохранять контекст стека | Размер и содержимое определяются реализацией |
| Можно использовать повторно | Не потокобезопасен |
| Прост в использовании с `setjmp`/`longjmp` | Переход через изменённые автоматические переменные — неопределённое поведение |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<setjmp.h>/setjmp|setjmp]] — сохранение контекста в `jmp_buf`
- [[Языки программирования/C/Библиотеки/<setjmp.h>/longjmp|longjmp]] — восстановление контекста из `jmp_buf`

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.13.2.1
- GNU C Library, заголовочный файл `setjmp.h`
