# stdc_popcount

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<stdbit.h>|<stdbit.h>]] / stdc_popcount

[[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_bit_width|Назад]] | [[Языки программирования/C/Библиотеки/<stdbit.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<stdint.h>/int8_t|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <stdbit.h>

unsigned int stdc_popcount(unsigned int value);
unsigned int stdc_popcount(unsigned long value);
unsigned int stdc_popcount(unsigned long long value);
```

## Описание

Макрос `stdc_popcount` возвращает количество единичных битов в значении `value`. Это синоним `stdc_count_ones` — оба макроса выполняют одну и ту же операцию (population count).

> [!NOTE]
> Эквивалент встроенных функций GCC: `__builtin_popcount`. На архитектурах x86 с поддержкой POPCNT реализуется инструкцией `POPCNT`.

## Пример

```c
#include <stdio.h>
#include <stdbit.h>

int main(void)
{
    unsigned int x = 0x000000FF;
    printf("stdc_popcount(%#x) = %u\n", x, stdc_popcount(x));
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
| Является стандартной функцией C23 | — |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_count_ones|stdc_count_ones]] — синоним `stdc_popcount`
- [[Языки программирования/C/Библиотеки/<stdint.h>/int8_t|int8_t]] — 8-битный знаковый целочисленный тип

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.18.3.15
- GNU C Library, заголовочный файл `stdbit.h`
