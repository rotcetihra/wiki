# stdc_first_leading_one

[[Языки программирования/C/Глава 10. Стандартная библиотека C|Глава 10. Стандартная библиотека C]] / [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdbit.h>|<stdbit.h>]] / stdc_first_leading_one

[[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdbit.h>/stdc_first_leading_zero|Назад]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdbit.h>|Содержание]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdbit.h>/stdc_first_trailing_zero|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <stdbit.h>

unsigned int stdc_first_leading_one(unsigned int value);
unsigned int stdc_first_leading_one(unsigned long value);
unsigned int stdc_first_leading_one(unsigned long long value);
```

## Описание

Макрос `stdc_first_leading_one` возвращает позицию первого ведущего единичного бита в значении `value` (нумерация с 1 от старшего бита). Если все биты равны 0, возвращает 0.

## Пример

```c
#include <stdio.h>
#include <stdbit.h>

int main(void)
{
    unsigned int x = 0x00FF0000;
    printf("stdc_first_leading_one(%#x) = %u\n", x, stdc_first_leading_one(x));
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
| `unsigned int` | Позиция первого ведущего единичного бита (1-based от старшего бита) или 0 |

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Переносимая альтернатива встроенным функциям | Возвращает 0 при отсутствии единицы |
| Работает со всеми беззнаковыми типами | — |

## Похожие определения

- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdbit.h>/stdc_first_leading_zero|stdc_first_leading_zero]] — позиция первого ведущего нуля
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdbit.h>/stdc_leading_ones|stdc_leading_ones]] — количество ведущих единичных битов

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.18.3.6
- GNU C Library, заголовочный файл `stdbit.h`
