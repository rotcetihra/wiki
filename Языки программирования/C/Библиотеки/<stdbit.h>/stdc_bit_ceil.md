# stdc_bit_ceil

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<stdbit.h>|<stdbit.h>]] / stdc_bit_ceil

[[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_has_single_bit|Назад]] | [[Языки программирования/C/Библиотеки/<stdbit.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_bit_floor|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <stdbit.h>

unsigned int stdc_bit_ceil(unsigned int value);
unsigned int stdc_bit_ceil(unsigned long value);
unsigned int stdc_bit_ceil(unsigned long long value);
```

## Описание

Макрос `stdc_bit_ceil` возвращает наименьшую степень двойки, не меньшую `value`. Если `value` уже является степенью двойки, возвращает его же.

Для `value` = 0 возвращает 1.

> [!NOTE]
> Полезно для выравнивания размеров буферов по границам кэш-линий и страниц памяти.

## Пример

```c
#include <stdio.h>
#include <stdbit.h>

int main(void)
{
    printf("stdc_bit_ceil(5) = %u\n", stdc_bit_ceil(5));
    printf("stdc_bit_ceil(8) = %u\n", stdc_bit_ceil(8));
    printf("stdc_bit_ceil(100) = %u\n", stdc_bit_ceil(100));
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
| `unsigned int` | Наименьшая степень двойки ≥ `value` |

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Удобно для выравнивания | Только для беззнаковых типов |
| Работает со всеми беззнаковыми типами | — |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_bit_floor|stdc_bit_floor]] — наибольшая степень двойки ≤ `value`
- [[Языки программирования/C/Библиотеки/<stdbit.h>/stdc_has_single_bit|stdc_has_single_bit]] — проверка степени двойки

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.18.3.12
- GNU C Library, заголовочный файл `stdbit.h`
