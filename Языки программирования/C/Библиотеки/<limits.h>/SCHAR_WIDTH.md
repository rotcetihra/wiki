# SCHAR_WIDTH

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<limits.h>|<limits.h>]] / SCHAR_WIDTH

[[Языки программирования/C/Библиотеки/<limits.h>/SCHAR_MIN|Назад]] | [[Языки программирования/C/Библиотеки/<limits.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<limits.h>/SHRT_MAX|Вперёд]]

**Дата написания:** 18.08.2026

## Определение

```c
#include <limits.h>

#define SCHAR_WIDTH 8 // в glibc
```

## Описание

Константа (C23) — ширина типа `signed char`: количество битов в значении типа без учёта бита знака. Для 8-битного `signed char` равна 8 (по стандарту — не меньше 7).

## Примеры

```c
#include <limits.h>
#include <stdio.h>

int main(void)
{
    printf("Ширина signed char: %d\n", SCHAR_WIDTH);

    return 0;
}
```

## Похожие определения

- [[Языки программирования/C/Библиотеки/<limits.h>/SCHAR_MAX|SCHAR_MAX]] — максимум `signed char`
- [[Языки программирования/C/Библиотеки/<limits.h>/CHAR_WIDTH|CHAR_WIDTH]] — ширина `char`
- [[Языки программирования/C/Библиотеки/<limits.h>/UCHAR_WIDTH|UCHAR_WIDTH]] — ширина `unsigned char`

## Источники

- ISO/IEC 9899:2024 (C23), раздел 5.2.4.2.1
- GNU C Library, заголовочный файл `limits.h`