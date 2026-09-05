# spaceship

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<compare>|<compare>]] / spaceship

[[Языки программирования/C++/Библиотеки/<compare>/operator>=|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <compare>

auto operator<=>(const T& lhs, const T& rhs);
```

## Описание

Оператор трёхстороннего сравнения («spaceship operator»). Возвращает результат, который сравнивается с константами `strong_ordering`, `weak_ordering` или `partial_ordering`. Позволяет определить все операторы сравнения через одну функцию.

## Примеры

```cpp
#include <compare>
#include <iostream>

struct Point {
    int x, y;
    auto operator<=>(const Point&) const = default;
};

int main()
{
    Point a{1, 2}, b{2, 3};

    auto result = a <=> b;
    if (result < 0)
        std::cout << "a < b" << std::endl;
    else if (result == 0)
        std::cout << "a == b" << std::endl;
    else
        std::cout << "a > b" << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений (если `operator<=>` не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<compare>/strong_ordering|strong_ordering]] — тип результата

## Источники

- https://en.cppreference.com/w/cpp/language/operator_comparison
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<compare>/operator>=|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>|Вперёд]]
