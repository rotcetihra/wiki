# in_place_index

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / in_place_index

[[Языки программирования/C++/Библиотеки/<utility>/in_place_index_t|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/integer_sequence|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<size_t I>
inline constexpr in_place_index_t<I> in_place_index{};
```

## Параметры

| Параметр | Описание |
|---|---|
| `I` | Индекс |

## Возвращаемое значение

Объект `in_place_index_t<I>`.

## Что делает

Объект тега для in-place конструирования с указанием индекса.

## Примеры

```cpp
#include <tuple>
#include <iostream>

int main()
{
    std::tuple<int, std::string> t(std::in_place_index<1>, 5, 'a');
    std::cout << std::get<1>(t) << std::endl; // "aaaaa"
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<utility>/in_place_type|in_place_type]] — с типом

## Источники

- https://en.cppreference.com/w/cpp/utility/in_place_index
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/in_place_index_t|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/integer_sequence|Вперёд]]
