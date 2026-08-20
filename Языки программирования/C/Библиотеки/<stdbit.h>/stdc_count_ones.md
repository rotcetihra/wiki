# stdc_count_ones

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<stdbit.h>|<stdbit.h>]] / stdc_count_ones

[[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_count_zeros|Назад]] | [[Языки программирования/C/Библиотеки/<stdbit.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_has_single_bit|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <stdbit.h>

unsigned int stdc_count_ones(unsigned int value);
unsigned int stdc_count_ones(unsigned long value);
unsigned int stdc_count_ones(unsigned long long value);
```

## Описание

Макрос `stdc_count_ones` возвращает количество единичных битов в значении `value`. Также известна как функция popcount (population count).

> [!NOTE]
> Эквивалент встроенных функций GCC: `__builtin_popcount`. На архитектурах x86 с поддержкой POPCNT реализуется инструкцией `POPCNT`.

## Пример

```c
#include <stdio.h>
#include <stdbit.h>

int main(void)
{
    unsigned int x = 0x000000FF;
    printf("stdc_count_ones(%#x) = %u\n", x, stdc_count_ones(x));
    return 0;
}
```

## Параметры

| Параметр | Описание |
|---|---|
| `value` | Беззнаковое целочисленное значение |

## Возвращаемое значение

| Значение | Описание |
|---|---|
| `unsigned int` | Количество единичных битов |

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Переносимая альтернатива встроенным функциям | Только для беззнаковых типов |
| Работает со всеми беззнаковыми типами | — |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_popcount|stdc_popcount]] — синоним `stdc_count_ones`
- [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_count_zeros|stdc_count_zeros]] — количество нулевых битов

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.18.3.10
- GNU C Library, заголовочный файл `stdbit.h`
