# isgreater

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<cmath>|<cmath>]] / isgreater

[[Языки программирования/C++/Библиотеки/<cmath>/fma|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/isgreaterequal|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <cmath>

bool isgreater(float x, float y);
bool isgreater(double x, double y);
bool isgreater(long double x, long double y);
```

## Параметры

| Параметр | Описание |
|---|---|
| `x` | Левый операнд |
| `y` | Правый операнд |

## Возвращаемое значение

`true`, если `x > y`.

## Что делает

Безопасное сравнение «больше». Не генерирует FP-исключения при участии NaN.

## Примеры

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << std::isgreater(3.0, 2.0) << std::endl; // 1
    std::cout << std::isgreater(NAN, 1.0) << std::endl;  // 0
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<cmath>/isless|isless]] — безопасное «меньше»

## Источники

- https://en.cppreference.com/w/cpp/numeric/math/isgreater
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<cmath>/fma|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/isgreaterequal|Вперёд]]
