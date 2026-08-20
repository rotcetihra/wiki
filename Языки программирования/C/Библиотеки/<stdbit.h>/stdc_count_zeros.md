# stdc_count_zeros

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<stdbit.h>|<stdbit.h>]] / stdc_count_zeros

[[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_first_trailing_one|Назад]] | [[Языки программирования/C/Библиотеки/<stdbit.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_count_ones|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <stdbit.h>

unsigned int stdc_count_zeros(unsigned int value);
unsigned int stdc_count_zeros(unsigned long value);
unsigned int stdc_count_zeros(unsigned long long value);
```

## Описание

Макрос `stdc_count_zeros` возвращает количество нулевых битов в значении `value`.

> [!NOTE]
> Эквивалент встроенных функций GCC: `~__builtin_popcount`. На архитектурах x86 с поддержкой POPCNT реализуется инструкцией `POPCNT` с предварительным инвертированием.

## Пример

```c
#include <stdio.h>
#include <stdbit.h>

int main(void)
{
    unsigned int x = 0x000000FF;
    printf("stdc_count_zeros(%#x) = %u\n", x, stdc_count_zeros(x));
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
| `unsigned int` | Количество нулевых битов |

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Переносимая альтернатива встроенным функциям | Только для беззнаковых типов |
| Работает со всеми беззнаковыми типами | — |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_count_ones|stdc_count_ones]] — количество единичных битов
- [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_popcount|stdc_popcount]] — количество единичных битов (синоним)

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.18.3.9
- GNU C Library, заголовочный файл `stdbit.h`
