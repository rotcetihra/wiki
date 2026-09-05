# compare_three_way

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<compare>|<compare>]] / compare_three_way

[[Языки программирования/C++/Библиотеки/<compare>/weak_equal|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>/operator==|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <compare>

struct compare_three_way {
    template<class T, class U>
    constexpr auto operator()(const T& t, const U& u) const;
};
```

## Описание

Функциональный объект, выполняющий трёхстороннее сравнение через `operator<=>`.

## Примеры

```cpp
#include <compare>
#include <iostream>

int main()
{
    std::compare_three_way comp;
    auto result = comp(1, 2);

    if (result < 0)
        std::cout << "1 < 2" << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<compare>/spaceship|spaceship]] — оператор `<=>`

## Источники

- https://en.cppreference.com/w/cpp/utility/compare/compare_three_way
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<compare>/weak_equal|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>/operator==|Вперёд]]
