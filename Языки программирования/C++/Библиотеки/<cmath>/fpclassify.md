# fpclassify

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<cmath>|<cmath>]] / fpclassify

[[Языки программирования/C++/Библиотеки/<cmath>/math_errhandling|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/isfinite|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <cmath>

int fpclassify(float x);
int fpclassify(double x);
int fpclassify(long double x);
```

## Параметры

| Параметр | Описание |
|---|---|
| `x` | Значение с плавающей точкой |

## Возвращаемое значение

Одно из: `FP_NAN`, `FP_INFINITE`, `FP_NORMAL`, `FP_SUBNORMAL`, `FP_ZERO`.

## Что делает

Классифицирует значение с плавающей точкой: является ли оно NaN, бесконечностью, нормальным, поднормализованным или нулём.

## Примеры

```cpp
#include <cmath>
#include <iostream>

int main()
{
    double vals[] = {0.0, 1.0, HUGE_VAL, 0.0/0.0, 5e-324};
    for (double v : vals) {
        int c = std::fpclassify(v);
        const char* names[] = {"ZERO", "NORMAL", "INFINITE", "NAN", "SUBNORMAL"};
        std::cout << v << " — " << names[c] << std::endl;
    }
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<cmath>/isfinite|isfinite]] — проверка на конечность
- [[Языки программирования/C++/Библиотеки/<cmath>/isnan|isnan]] — проверка на NaN

## Источники

- https://en.cppreference.com/w/cpp/numeric/math/fpclassify
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<cmath>/math_errhandling|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/isfinite|Вперёд]]
