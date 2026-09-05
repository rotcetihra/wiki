# islessequal

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<cmath>|<cmath>]] / islessequal

[[Языки программирования/C++/Библиотеки/<cmath>/isless|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/islessgreater|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <cmath>

bool islessequal(float x, float y);
bool islessequal(double x, double y);
bool islessequal(long double x, long double y);
```

## Параметры

| Параметр | Описание |
|---|---|
| `x` | Левый операнд |
| `y` | Правый операнд |

## Возвращаемое значение

`true`, если `x <= y`.

## Что делает

Безопасное сравнение «меньше или равно».

## Примеры

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << std::islessequal(3.0, 3.0) << std::endl; // 1
    std::cout << std::islessequal(2.0, 3.0) << std::endl; // 1
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<cmath>/isless|isless]] — безопасное «меньше»

## Источники

- https://en.cppreference.com/w/cpp/numeric/math/islessequal
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<cmath>/isless|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/islessgreater|Вперёд]]
