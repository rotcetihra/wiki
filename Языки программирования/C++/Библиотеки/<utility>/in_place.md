# in_place

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / in_place

[[Языки программирования/C++/Библиотеки/<utility>/in_place_t|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/in_place_type_t|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

inline constexpr in_place_t in_place{};
```

## Параметры

Нет.

## Возвращаемое значение

Объект `in_place_t`.

## Что делает

Объект тега для in-place конструирования.

## Примеры

```cpp
#include <variant>
#include <iostream>

int main()
{
    std::variant<int, std::string> v(std::in_place_type<std::string>, "hello");
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<utility>/in_place_type|in_place_type]] — объект типа

## Источники

- https://en.cppreference.com/w/cpp/utility/in_place
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/in_place_t|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/in_place_type_t|Вперёд]]
