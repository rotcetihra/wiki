# <limits.h>

[[Языки программирования/C/Библиотеки|Библиотеки]] / <limits.h>

[[Языки программирования/C/Библиотеки/<iso646.h>|Назад]] | [[Языки программирования/C/Библиотеки|Содержание]] | [[Языки программирования/C/Библиотеки/<stdalign.h>|Вперёд]]

**Дата написания:** 18.08.2026

## Оглавление

### ISO C

- [[Языки программирования/C/Библиотеки/<limits.h>/BITINT_MAXWIDTH|BITINT_MAXWIDTH]] — максимальная ширина типа `_BitInt` (C23)
- [[Языки программирования/C/Библиотеки/<limits.h>/BOOL_WIDTH|BOOL_WIDTH]] — ширина типа `bool` (C23)
- [[Языки программирования/C/Библиотеки/<limits.h>/CHAR_BIT|CHAR_BIT]] — количество битов в байте (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/CHAR_MAX|CHAR_MAX]] — максимум типа `char` (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/CHAR_MIN|CHAR_MIN]] — минимум типа `char` (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/CHAR_WIDTH|CHAR_WIDTH]] — ширина типа `char` (C23)
- [[Языки программирования/C/Библиотеки/<limits.h>/INT_MAX|INT_MAX]] — максимум типа `int` (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/INT_MIN|INT_MIN]] — минимум типа `int` (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/INT_WIDTH|INT_WIDTH]] — ширина типа `int` (C23)
- [[Языки программирования/C/Библиотеки/<limits.h>/LLONG_MAX|LLONG_MAX]] — максимум типа `long long` (C99)
- [[Языки программирования/C/Библиотеки/<limits.h>/LLONG_MIN|LLONG_MIN]] — минимум типа `long long` (C99)
- [[Языки программирования/C/Библиотеки/<limits.h>/LLONG_WIDTH|LLONG_WIDTH]] — ширина типа `long long` (C23)
- [[Языки программирования/C/Библиотеки/<limits.h>/LONG_MAX|LONG_MAX]] — максимум типа `long` (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/LONG_MIN|LONG_MIN]] — минимум типа `long` (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/LONG_WIDTH|LONG_WIDTH]] — ширина типа `long` (C23)
- [[Языки программирования/C/Библиотеки/<limits.h>/MB_LEN_MAX|MB_LEN_MAX]] — максимальная длина многобайтового символа (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/SCHAR_MAX|SCHAR_MAX]] — максимум типа `signed char` (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/SCHAR_MIN|SCHAR_MIN]] — минимум типа `signed char` (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/SCHAR_WIDTH|SCHAR_WIDTH]] — ширина типа `signed char` (C23)
- [[Языки программирования/C/Библиотеки/<limits.h>/SHRT_MAX|SHRT_MAX]] — максимум типа `short` (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/SHRT_MIN|SHRT_MIN]] — минимум типа `short` (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/SHRT_WIDTH|SHRT_WIDTH]] — ширина типа `short` (C23)
- [[Языки программирования/C/Библиотеки/<limits.h>/UCHAR_MAX|UCHAR_MAX]] — максимум типа `unsigned char` (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/UCHAR_WIDTH|UCHAR_WIDTH]] — ширина типа `unsigned char` (C23)
- [[Языки программирования/C/Библиотеки/<limits.h>/UINT_MAX|UINT_MAX]] — максимум типа `unsigned int` (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/UINT_WIDTH|UINT_WIDTH]] — ширина типа `unsigned int` (C23)
- [[Языки программирования/C/Библиотеки/<limits.h>/ULLONG_MAX|ULLONG_MAX]] — максимум типа `unsigned long long` (C99)
- [[Языки программирования/C/Библиотеки/<limits.h>/ULLONG_WIDTH|ULLONG_WIDTH]] — ширина типа `unsigned long long` (C23)
- [[Языки программирования/C/Библиотеки/<limits.h>/ULONG_MAX|ULONG_MAX]] — максимум типа `unsigned long` (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/ULONG_WIDTH|ULONG_WIDTH]] — ширина типа `unsigned long` (C23)
- [[Языки программирования/C/Библиотеки/<limits.h>/USHRT_MAX|USHRT_MAX]] — максимум типа `unsigned short` (C89)
- [[Языки программирования/C/Библиотеки/<limits.h>/USHRT_WIDTH|USHRT_WIDTH]] — ширина типа `unsigned short` (C23)

## Описание библиотеки

Заголовочный файл `<limits.h>` — «пределы» (limits): константы, определяющие диапазоны значений целочисленных типов языка C. Не содержит ни типов, ни функций — только объектоподобные макросы. Для каждого целочисленного типа стандарт гарантирует _минимальные_ значения его минимума и максимума (например, `INT_MAX` не меньше 32767, `LONG_MAX` — не меньше 2147483647), а реализация обязана определить точные значения в этом заголовке. Так программа получает фактические пределы типов на конкретной платформе без вопросов компилятору (`sizeof` пределы не даёт).

В C23 добавлены макросы вида `*_WIDTH` — число битов в значении типа без знаковых и заполняющих битов, а также `BOOL_WIDTH` и `BITINT_MAXWIDTH`. До C23 ширину типа приходилось вычислять через `CHAR_BIT * sizeof(тип)`.

> [!NOTE]
> Значения в glibc соответствуют 32/64-битным платформам: `int` — 32 бита, `long` — 32 бита на 32-битных и 64 бита на 64-битных системах (LP64). Поэтому переносимая программа не должна полагаться на конкретные значения, кроме гарантированных стандартом минимумов.

### Пределы целых типов

| Макрос | Минимум по стандарту | Тип | Стандарт |
|---|---|---|---|
| `CHAR_BIT` | 8 | константа | C89 |
| `SCHAR_MIN` / `SCHAR_MAX` | −127 / 127 | `signed char` | C89 |
| `UCHAR_MAX` | 255 | `unsigned char` | C89 |
| `CHAR_MIN` / `CHAR_MAX` | 0/255 или −127/127 | `char` | C89 |
| `SHRT_MIN` / `SHRT_MAX` | −32767 / 32767 | `short` | C89 |
| `USHRT_MAX` | 65535 | `unsigned short` | C89 |
| `INT_MIN` / `INT_MAX` | −32767 / 32767 | `int` | C89 |
| `UINT_MAX` | 65535 | `unsigned int` | C89 |
| `LONG_MIN` / `LONG_MAX` | −2147483647 / 2147483647 | `long` | C89 |
| `ULONG_MAX` | 4294967295 | `unsigned long` | C89 |
| `LLONG_MIN` / `LLONG_MAX` | −9223372036854775807 / 9223372036854775807 | `long long` | C99 |
| `ULLONG_MAX` | 18446744073709551615 | `unsigned long long` | C99 |
| `MB_LEN_MAX` | 1 | константа | C89 |

### Ширины типов (C23)

| Макрос | Описание |
|---|---|
| `BOOL_WIDTH` | Ширина типа `bool` (обычно 1) |
| `CHAR_WIDTH`, `SCHAR_WIDTH`, `UCHAR_WIDTH` | Ширина `char`, `signed char`, `unsigned char` |
| `SHRT_WIDTH`, `USHRT_WIDTH` | Ширина `short`, `unsigned short` |
| `INT_WIDTH`, `UINT_WIDTH` | Ширина `int`, `unsigned int` |
| `LONG_WIDTH`, `ULONG_WIDTH` | Ширина `long`, `unsigned long` |
| `LLONG_WIDTH`, `ULLONG_WIDTH` | Ширина `long long`, `unsigned long long` |
| `BITINT_MAXWIDTH` | Максимальная ширина типа `_BitInt` |

[[Языки программирования/C/Библиотеки/<iso646.h>|Назад]] | [[Языки программирования/C/Библиотеки|Содержание]] | [[Языки программирования/C/Библиотеки/<stdalign.h>|Вперёд]]