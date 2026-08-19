# conj

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<complex.h>|<complex.h>]] / conj

[[Языки программирования/C/Библиотеки/<complex.h>/clog|Назад]] | [[Языки программирования/C/Библиотеки/<complex.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<complex.h>/cpow|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <complex.h>

double conj(double complex z);
float conjf(float complex z);
long double conjl(long double complex z);
```

## Описание

Функция `conj` вычисляет комплексное сопряжение комплексного числа. Сопряжённое число для `z = x + yi` определяется как `x - yi`, то есть мнимая часть меняет знак.

Сопряжение используется для вычисления модуля (через произведение числа и его сопряжения), деления комплексных чисел и других операций.

Существуют три варианта функции: `conjf` для `float complex`, `conj` для `double complex` и `conjl` для `long double complex`.

## Примеры

```c
#include <stdio.h>
#include <complex.h>

int main(void)
{
    double complex z = 3.0 + 4.0 * I;
    double complex z_conj = conj(z);
    printf("z = %.1f + %.1fi\n", creal(z), cimag(z));
    printf("conj(z) = %.1f + %.1fi\n", creal(z_conj), cimag(z_conj));

    double complex product = z * z_conj;
    printf("z * conj(z) = %.1f + %.1fi\n", creal(product), cimag(product));

    return 0;
}
```

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Простая и понятная операция | Три варианта для разных точностей |
| Стандартный способ сопряжения | Не модифицирует исходное число |
| Полезна для вычисления модуля | |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<complex.h>/cabs|cabs]] — модуль комплексного числа
- [[Языки программирования/C/Библиотеки/<complex.h>/creal|creal]] — действительная часть
- [[Языки программирования/C/Библиотеки/<complex.h>/cimag|cimag]] — мнимая часть

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.3.9.2
- GNU C Library, заголовочный файл `complex.h`