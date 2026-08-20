# stdc_bit_width

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<stdbit.h>|<stdbit.h>]] / stdc_bit_width

[[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_bit_floor|Назад]] | [[Языки программирования/C/Библиотеки/<stdbit.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_popcount|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <stdbit.h>

unsigned int stdc_bit_width(unsigned int value);
unsigned int stdc_bit_width(unsigned long value);
unsigned int stdc_bit_width(unsigned long long value);
```

## Описание

Макрос `stdc_bit_width` возвращает количество значащих битов в значении `value` — то есть позицию старшего установленного бита плюс 1. Для 0 возвращает 0.

Это эквивалент `stdc_leading_zeros(value) + 1` для ненулевых значений.

## Пример

```c
#include <stdio.h>
#include <stdbit.h>

int main(void)
{
    printf("stdc_bit_width(1) = %u\n", stdc_bit_width(1));
    printf("stdc_bit_width(7) = %u\n", stdc_bit_width(7));
    printf("stdc_bit_width(8) = %u\n", stdc_bit_width(8));
    printf("stdc_bit_width(0) = %u\n", stdc_bit_width(0));
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
| `unsigned int` | Количество значащих битов (0 для `value` = 0) |

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Полезно для определения размера данных | Только для беззнаковых типов |
| Работает со всеми беззнаковыми типами | — |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_leading_zeros|stdc_leading_zeros]] — количество ведущих нулевых битов
- [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_popcount|stdc_popcount]] — количество единичных битов

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.18.3.14
- GNU C Library, заголовочный файл `stdbit.h`
