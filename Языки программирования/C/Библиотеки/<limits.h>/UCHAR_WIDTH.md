# UCHAR_WIDTH

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<limits.h>|<limits.h>]] / UCHAR_WIDTH

[[Языки программирования/C/Библиотеки/<limits.h>/UCHAR_MAX|Назад]] | [[Языки программирования/C/Библиотеки/<limits.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<limits.h>/UINT_MAX|Вперёд]]

**Дата написания:** 18.08.2026

## Определение

```c
#include <limits.h>

#define UCHAR_WIDTH 8 // в glibc
```

## Описание

Константа (C23) — ширина типа `unsigned char`: количество битов в значении типа. Для беззнаковых типов ширина совпадает с числом битов в представлении, поэтому у 8-битного `unsigned char` она равна 8.

## Примеры

```c
#include <limits.h>
#include <stdio.h>

int main(void)
{
    printf("Ширина unsigned char: %d\n", UCHAR_WIDTH);

    return 0;
}
```

## Похожие определения

- [[Языки программирования/C/Библиотеки/<limits.h>/UCHAR_MAX|UCHAR_MAX]] — максимум `unsigned char`
- [[Языки программирования/C/Библиотеки/<limits.h>/SCHAR_WIDTH|SCHAR_WIDTH]] — ширина `signed char`

## Источники

- ISO/IEC 9899:2024 (C23), раздел 5.2.4.2.1
- GNU C Library, заголовочный файл `limits.h`