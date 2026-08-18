# ULLONG_WIDTH

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<limits.h>|<limits.h>]] / ULLONG_WIDTH

[[Языки программирования/C/Библиотеки/<limits.h>/ULLONG_MAX|Назад]] | [[Языки программирования/C/Библиотеки/<limits.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<limits.h>/ULONG_MAX|Вперёд]]

**Дата написания:** 18.08.2026

## Определение

```c
#include <limits.h>

#define ULLONG_WIDTH 64 // в glibc
```

## Описание

Константа (C23) — ширина типа `unsigned long long`: количество битов в значении типа. По стандарту не меньше 63; на всех распространённых платформах равна 64.

## Примеры

```c
#include <limits.h>
#include <stdio.h>

int main(void)
{
    printf("Ширина unsigned long long: %d\n", ULLONG_WIDTH);

    return 0;
}
```

## Похожие определения

- [[Языки программирования/C/Библиотеки/<limits.h>/ULLONG_MAX|ULLONG_MAX]] — максимум `unsigned long long`
- [[Языки программирования/C/Библиотеки/<limits.h>/LLONG_WIDTH|LLONG_WIDTH]] — ширина `long long`

## Источники

- ISO/IEC 9899:2024 (C23), раздел 5.2.4.2.1
- GNU C Library, заголовочный файл `limits.h`