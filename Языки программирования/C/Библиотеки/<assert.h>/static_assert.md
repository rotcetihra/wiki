# static_assert

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<assert.h>|<assert.h>]] / static_assert

[[Языки программирования/C/Библиотеки/<assert.h>/NDEBUG|Назад]] | [[Языки программирования/C/Библиотеки/<assert.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<ctype.h>/_tolower|Вперёд]]

**Дата написания:** 18.08.2026
**Дата обновления:** 31.08.2026

## Определение

```c
#include <assert.h>

void static_assert(bool constant-expression, const char *msg);

/* С C23: */
void static_assert(bool constant-expression);
```

## Описание

Макрос `static_assert` похож на `assert(3)`, но работает на этапе компиляции, генерируя ошибку компиляции (с необязательным сообщением), когда входное выражение ложно (равно нулю). Если выражение не равно нулю, код не генерируется.

Параметр `msg` должен быть строковым литералом. С C23 этот аргумент необязателен.

Существует ключевое слово `_Static_assert()`, которое ведёт себя идентично и может использоваться без включения `<assert.h>`.

> [!NOTE]
> В C11 второй аргумент (`msg`) был обязательным; с C23 его можно опустить.

## Возвращаемое значение

Не возвращает значения.

## Примеры

```c
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define must_be(e)                                        \
    (                                                     \
        0 * (int) sizeof(                                 \
            struct {                                      \
                static_assert(e);                         \
                int  ISO_C_forbids_a_struct_with_no_members;  \
            }                                             \
        )                                                 \
    )

#define is_same_type(a, b) \
    __builtin_types_compatible_p(typeof(a), typeof(b))

#define is_array(arr)       (!is_same_type((arr), &*(arr)))
#define must_be_array(arr)  must_be(is_array(arr))

#define sizeof_array(arr)   (sizeof(arr) + must_be_array(arr))
#define NITEMS(arr)         (sizeof((arr)) / sizeof((arr)[0]) \
                             + must_be_array(arr))

int     foo[10];
int8_t  bar[sizeof_array(foo)];

int main(void)
{
    for (size_t i = 0; i < NITEMS(foo); i++) {
        foo[i] = i;
    }

    memcpy(bar, foo, sizeof_array(bar));

    for (size_t i = 0; i < NITEMS(bar); i++) {
        printf("%d,", bar[i]);
    }

    exit(EXIT_SUCCESS);
}
```

## Стандарты

C23.

## История

C11.

В C11 второй аргумент (`msg`) был обязательным; с C23 его можно опустить.

## Источники

- https://man7.org/linux/man-pages/man3/static_assert.3.html
- `/usr/include/assert.h`
- ISO/IEC 9899:2024 (C23)

## См. также

- [[Языки программирования/C/Библиотеки/<assert.h>/assert|assert]] — проверка во время выполнения
