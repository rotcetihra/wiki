# isgreaterequal

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<cmath>|<cmath>]] / isgreaterequal

[[Языки программирования/C++/Библиотеки/<cmath>/isgreater|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/isless|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <cmath>

bool isgreaterequal(float x, float y);
bool isgreaterequal(double x, double y);
bool isgreaterequal(long double x, long double y);
```

## Параметры

| Параметр | Описание |
|---|---|
| `x` | Левый операнд |
| `y` | Правый операнд |

## Возвращаемое значение

`true`, если `x >= y`.

## Что делает

Безопасное сравнение «больше или равно». Не генерирует FP-исключения при участии NaN.

## Примеры

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << std::isgreaterequal(3.0, 3.0) << std::endl; // 1
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<cmath>/isgreater|isgreater]] — безопасное «больше»

## Источники

- https://en.cppreference.com/w/cpp/numeric/math/isgreaterequal
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<cmath>/isgreater|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/isless|Вперёд]]
