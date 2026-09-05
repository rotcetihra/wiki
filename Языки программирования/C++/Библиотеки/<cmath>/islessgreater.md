# islessgreater

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<cmath>|<cmath>]] / islessgreater

[[Языки программирования/C++/Библиотеки/<cmath>/islessequal|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/isunordered|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <cmath>

bool islessgreater(float x, float y);
bool islessgreater(double x, double y);
bool islessgreater(long double x, long double y);
```

## Параметры

| Параметр | Описание |
|---|---|
| `x` | Левый операнд |
| `y` | Правый операнд |

## Возвращаемое значение

`true`, если `x < y || x > y`.

## Что делает

Безопасная проверка «меньше или больше» (не равно, без учёта порядка). Эквивалент `x != y` для не-NaN.

## Примеры

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << std::islessgreater(3.0, 3.0) << std::endl; // 0
    std::cout << std::islessgreater(2.0, 3.0) << std::endl; // 1
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- `!=` — оператор неравенства (unsafe при NaN)

## Источники

- https://en.cppreference.com/w/cpp/numeric/math/islessgreater
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<cmath>/islessequal|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/isunordered|Вперёд]]
