# make_index_sequence

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / make_index_sequence

[[Языки программирования/C++/Библиотеки/<utility>/make_integer_sequence|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/index_sequence_for|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<size_t N>
using make_index_sequence = std::make_integer_sequence<size_t, N>;
```

## Параметры

| Параметр | Описание |
|---|---|
| `N` | Размер последовательности |

## Возвращаемое значение

`index_sequence<0, 1, ..., N-1>`.

## Что делает

Создаёт последовательность индексов от 0 до N-1.

## Примеры

```cpp
#include <utility>
#include <iostream>

int main()
{
    using seq = std::make_index_sequence<3>; // 0,1,2
    std::cout << std::tuple_size_v<std::tuple<int, int, int>> << std::endl;
}
```

## Исключения

- **Исключения:** операция времени компиляции.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<utility>/index_sequence_for|index_sequence_for]] — для параметров шаблона

## Источники

- https://en.cppreference.com/w/cpp/utility/index_sequence/make_index_sequence
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/make_integer_sequence|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/index_sequence_for|Вперёд]]
