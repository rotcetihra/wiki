# weak_equal

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<compare>|<compare>]] / weak_equal

[[Языки программирования/C++/Библиотеки/<compare>/strong_equal|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>/compare_three_way|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <compare>

struct weak_ordering;
consteval bool operator==(weak_ordering, weak_ordering) = default;
```

## Описание

Для `std::weak_ordering` нет различия между `equal` и `equivalent` — оба обозначают эквивалентность в слабом порядке.

## Примеры

```cpp
#include <compare>
#include <iostream>

int main()
{
    auto result = 3 <=> 3;
    std::cout << (result == std::weak_ordering::equivalent) << std::endl; // 1
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<compare>/weak_ordering|weak_ordering]] — тип результата

## Источники

- https://en.cppreference.com/w/cpp/utility/compare/weak_ordering
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<compare>/strong_equal|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>/compare_three_way|Вперёд]]
