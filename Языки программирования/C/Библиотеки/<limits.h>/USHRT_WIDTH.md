# USHRT_WIDTH

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<limits.h>|<limits.h>]] / USHRT_WIDTH

[[Языки программирования/C/Библиотеки/<limits.h>/USHRT_MAX|Назад]] | [[Языки программирования/C/Библиотеки/<limits.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<stdalign.h>/alignas|Вперёд]]

**Дата написания:** 18.08.2026

## Определение

```c
#include <limits.h>

#define USHRT_WIDTH 16 // в glibc
```

## Описание

Константа (C23) — ширина типа `unsigned short`: количество битов в значении типа. По стандарту не меньше 15; на всех распространённых платформах равна 16.

## Примеры

```c
#include <limits.h>
#include <stdio.h>

int main(void)
{
    printf("Ширина unsigned short: %d\n", USHRT_WIDTH);

    return 0;
}
```

## Похожие определения

- [[Языки программирования/C/Библиотеки/<limits.h>/USHRT_MAX|USHRT_MAX]] — максимум `unsigned short`
- [[Языки программирования/C/Библиотеки/<limits.h>/SHRT_WIDTH|SHRT_WIDTH]] — ширина `short`

## Источники

- ISO/IEC 9899:2024 (C23), раздел 5.2.4.2.1
- GNU C Library, заголовочный файл `limits.h`