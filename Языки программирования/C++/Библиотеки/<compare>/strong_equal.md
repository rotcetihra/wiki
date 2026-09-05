# strong_equal

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<compare>|<compare>]] / strong_equal

[[Языки программирования/C++/Библиотеки/<compare>/partial_ordering|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>/weak_equal|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <compare>

struct strong_ordering;
consteval bool operator==(strong_ordering, strong_ordering) = default;
```

## Описание

Константа `std::strong_ordering::equal` и `std::strong_ordering::equivalent` оба имеют числовое значение 0, но `equal` означает «значения идентичны», а `equivalent` — «порядковые отношения одинаковы».

## Примеры

```cpp
#include <compare>
#include <iostream>

int main()
{
    auto result = 3 <=> 3;
    std::cout << (result == std::strong_ordering::equal) << std::endl;     // 1
    std::cout << (result == std::strong_ordering::equivalent) << std::endl; // 1
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<compare>/strong_ordering|strong_ordering]] — тип результата

## Источники

- https://en.cppreference.com/w/cpp/utility/compare/strong_ordering
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<compare>/partial_ordering|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>/weak_equal|Вперёд]]
