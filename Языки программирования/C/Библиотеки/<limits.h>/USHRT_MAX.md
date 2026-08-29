# USHRT_MAX

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<limits.h>|<limits.h>]] / USHRT_MAX

[[Языки программирования/C/Библиотеки/<limits.h>/ULONG_WIDTH|Назад]] | [[Языки программирования/C/Библиотеки/<limits.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<limits.h>/USHRT_WIDTH|Вперёд]]

**Дата написания:** 18.08.2026

## Определение

```c
#include <limits.h>

#define USHRT_MAX 65535 // в glibc
```

## Описание

Константа — максимальное значение типа `unsigned short`. Стандарт гарантирует, что `USHRT_MAX` не меньше 65535; на всех распространённых платформах `unsigned short` занимает 16 бит, и значение равно 65535 (2¹⁶−1).

## Примеры

```c
#include <limits.h>
#include <stdio.h>

int main(void)
{
    unsigned short n = USHRT_MAX;

    printf("Максимум unsigned short: %u\n", USHRT_MAX);

    return 0;
}
```

## Похожие определения

- [[Языки программирования/C/Библиотеки/<limits.h>/USHRT_WIDTH|USHRT_WIDTH]] — ширина `unsigned short`
- [[Языки программирования/C/Библиотеки/<limits.h>/SHRT_MAX|SHRT_MAX]] — максимум `short`

## Источники

- ISO/IEC 9899:2024 (C23), раздел 5.2.4.2.1
- GNU C Library, заголовочный файл `limits.h`