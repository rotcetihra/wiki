# stdc_first_leading_zero

[[Языки программирования/C/Глава 10. Стандартная библиотека C|Глава 10. Стандартная библиотека C]] / [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdbit.h>|<stdbit.h>]] / stdc_first_leading_zero

[[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdbit.h>/stdc_trailing_ones|Назад]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdbit.h>|Содержание]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdbit.h>/stdc_first_leading_one|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <stdbit.h>

unsigned int stdc_first_leading_zero(unsigned int value);
unsigned int stdc_first_leading_zero(unsigned long value);
unsigned int stdc_first_leading_zero(unsigned long long value);
```

## Описание

Макрос `stdc_first_leading_zero` возвращает позицию первого ведущего нулевого бита в значении `value` (нумерация с 1 от старшего бита). Если все биты равны 1, возвращает 0.

## Пример

```c
#include <stdio.h>
#include <stdbit.h>

int main(void)
{
    unsigned int x = 0x7FFFFFFF;
    printf("stdc_first_leading_zero(%#x) = %u\n", x, stdc_first_leading_zero(x));
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
| `unsigned int` | Позиция первого ведущего нуля (1-based от старшего бита) или 0 |

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Переносимая альтернатива встроенным функциям | Возвращает 0 при отсутствии нуля |
| Работает со всеми беззнаковыми типами | — |

## Похожие определения

- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdbit.h>/stdc_first_leading_one|stdc_first_leading_one]] — позиция первого ведущего единичного бита
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdbit.h>/stdc_leading_zeros|stdc_leading_zeros]] — количество ведущих нулевых битов

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.18.3.5
- GNU C Library, заголовочный файл `stdbit.h`
