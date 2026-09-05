# index_sequence

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / index_sequence

[[Языки программирования/C++/Библиотеки/<utility>/integer_sequence|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/make_integer_sequence|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<size_t... Ints>
using index_sequence = std::integer_sequence<size_t, Ints...>;
```

## Параметры

| Параметр | Описание |
|---|---|
| `Ints` | Параметрический пакет индексов |

## Возвращаемое значение

Алиас для `integer_sequence<size_t, ...>`.

## Что делает

Удобный алиас для последовательности `size_t` индексов.

## Примеры

```cpp
#include <utility>
#include <iostream>

int main()
{
    using seq = std::index_sequence<0, 1, 2>;
    std::cout << std::tuple_size_v<std::tuple<int, int, int>> << std::endl;
}
```

## Исключения

- **Исключения:** операция времени компиляции.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<utility>/make_index_sequence|make_index_sequence]] — автоматическое создание

## Источники

- https://en.cppreference.com/w/cpp/utility/index_sequence
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/integer_sequence|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/make_integer_sequence|Вперёд]]
