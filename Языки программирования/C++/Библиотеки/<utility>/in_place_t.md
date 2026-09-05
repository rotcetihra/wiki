# in_place_t

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / in_place_t

[[Языки программирования/C++/Библиотеки/<utility>/piecewise_construct_t|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/in_place|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

struct in_place_t {
    explicit in_place_t() = default;
};

inline constexpr in_place_t in_place{};
```

## Параметры

Нет.

## Возвращаемое значение

Тег `in_place_t` и объект `in_place`.

## Что делает

Тег для in-place конструирования (конструирования объекта прямо в выделенной памяти). Используется в `std::optional`, `std::variant`, `std::any`.

## Примеры

```cpp
#include <optional>
#include <iostream>

int main()
{
    std::optional<int> o(std::in_place, 42);
    std::cout << *o << std::endl; // 42
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<utility>/in_place_type_t|in_place_type_t]] — с типом
- [[Языки программирования/C++/Библиотеки/<utility>/in_place_index_t|in_place_index_t]] — с индексом

## Источники

- https://en.cppreference.com/w/cpp/utility/in_place
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/piecewise_construct_t|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/in_place|Вперёд]]
