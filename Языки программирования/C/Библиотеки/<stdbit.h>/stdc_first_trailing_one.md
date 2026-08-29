# stdc_first_trailing_one

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<stdbit.h>|<stdbit.h>]] / stdc_first_trailing_one

[[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_first_trailing_zero|Назад]] | [[Языки программирования/C/Библиотеки/<stdbit.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_count_zeros|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <stdbit.h>

unsigned int stdc_first_trailing_one(unsigned int value);
unsigned int stdc_first_trailing_one(unsigned long value);
unsigned int stdc_first_trailing_one(unsigned long long value);
```

## Описание

Макрос `stdc_first_trailing_one` возвращает позицию первого завершающего единичного бита в значении `value` (нумерация с 1 от младшего бита). Если все биты равны 0, возвращает 0.

## Пример

```c
#include <stdio.h>
#include <stdbit.h>

int main(void)
{
    unsigned int x = 0x00000006;
    printf("stdc_first_trailing_one(%#x) = %u\n", x, stdc_first_trailing_one(x));
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
| `unsigned int` | Позиция первого завершающего единичного бита (1-based от младшего бита) или 0 |

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Переносимая альтернатива встроенным функциям | Возвращает 0 при отсутствии единицы |
| Работает со всеми беззнаковыми типами | — |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_first_trailing_zero|stdc_first_trailing_zero]] — позиция первого завершающего нуля
- [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_trailing_ones|stdc_trailing_ones]] — количество завершающих единичных битов

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.18.3.8
- GNU C Library, заголовочный файл `stdbit.h`
