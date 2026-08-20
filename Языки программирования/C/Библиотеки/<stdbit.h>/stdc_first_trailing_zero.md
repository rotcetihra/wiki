# stdc_first_trailing_zero

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<stdbit.h>|<stdbit.h>]] / stdc_first_trailing_zero

[[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_first_leading_one|Назад]] | [[Языки программирования/C/Библиотеки/<stdbit.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_first_trailing_one|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <stdbit.h>

unsigned int stdc_first_trailing_zero(unsigned int value);
unsigned int stdc_first_trailing_zero(unsigned long value);
unsigned int stdc_first_trailing_zero(unsigned long long value);
```

## Описание

Макрос `stdc_first_trailing_zero` возвращает позицию первого завершающего нулевого бита в значении `value` (нумерация с 1 от младшего бита). Если все биты равны 1, возвращает 0.

## Пример

```c
#include <stdio.h>
#include <stdbit.h>

int main(void)
{
    unsigned int x = 0x0000000E;
    printf("stdc_first_trailing_zero(%#x) = %u\n", x, stdc_first_trailing_zero(x));
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
| `unsigned int` | Позиция первого завершающего нуля (1-based от младшего бита) или 0 |

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Переносимая альтернатива встроенным функциям | Возвращает 0 при отсутствии нуля |
| Работает со всеми беззнаковыми типами | — |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_first_trailing_one|stdc_first_trailing_one]] — позиция первого завершающего единичного бита
- [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_trailing_zeros|stdc_trailing_zeros]] — количество завершающих нулевых битов

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.18.3.7
- GNU C Library, заголовочный файл `stdbit.h`
