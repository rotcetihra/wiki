# piecewise_construct

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / piecewise_construct

[[Языки программирования/C++/Библиотеки/<utility>/make_pair|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/piecewise_construct_t|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

struct piecewise_construct_t {
    explicit piecewise_construct_t() = default;
};

inline constexpr piecewise_construct_t piecewise_construct{};
```

## Параметры

Нет.

## Возвращаемое значение

Константа `piecewise_construct` типа `piecewise_construct_t`.

## Что делает

Тег для пошаговой (piecewise) инициализации элементов `std::pair` и `std::tuple` через передачу аргументов конструктору каждого элемента отдельно.

## Примеры

```cpp
#include <utility>
#include <tuple>
#include <iostream>

int main()
{
    std::pair<std::tuple<int>, std::tuple<int, int>> p(
        std::piecewise_construct,
        std::make_tuple(1),
        std::make_tuple(2, 3));
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<utility>/piecewise_construct_t|piecewise_construct_t]] — тип тега

## Источники

- https://en.cppreference.com/w/cpp/utility/piecewise_construct
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/make_pair|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/piecewise_construct_t|Вперёд]]
