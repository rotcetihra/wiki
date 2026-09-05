# piecewise_construct_t

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / piecewise_construct_t

[[Языки программирования/C++/Библиотеки/<utility>/piecewise_construct|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/in_place_t|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

struct piecewise_construct_t {
    explicit piecewise_construct_t() = default;
};
```

## Параметры

Нет.

## Возвращаемое значение

Тип тега `piecewise_construct_t`.

## Что делает

Тип тега для пошаговой инициализации. Используется как первый аргумент конструктора `std::pair`.

## Примеры

```cpp
#include <utility>
#include <tuple>

int main()
{
    std::pair<int, int> p(
        std::piecewise_construct_t{},
        std::make_tuple(1),
        std::make_tuple(2));
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<utility>/piecewise_construct|piecewise_construct]] — объект тега

## Источники

- https://en.cppreference.com/w/cpp/utility/piecewise_construct
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/piecewise_construct|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/in_place_t|Вперёд]]
