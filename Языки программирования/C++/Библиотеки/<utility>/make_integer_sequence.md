# make_integer_sequence

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / make_integer_sequence

[[Языки программирования/C++/Библиотеки/<utility>/index_sequence|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/make_index_sequence|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<class T, T N>
using make_integer_sequence = std::integer_sequence<T, /* 0, 1, ..., N-1 */>;
```

## Параметры

| Параметр | Описание |
|---|---|
| `T` | Целочисленный тип |
| `N` | Размер последовательности |

## Возвращаемое значение

`integer_sequence<T, 0, 1, ..., N-1>`.

## Что делает

Создаёт последовательность целых чисел от 0 до N-1.

## Примеры

```cpp
#include <utility>
#include <iostream>

int main()
{
    using seq = std::make_integer_sequence<int, 5>; // 0,1,2,3,4
    std::cout << seq::size() << std::endl; // 5
}
```

## Исключения

- **Исключения:** операция времени компиляции.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<utility>/make_index_sequence|make_index_sequence]] — для `size_t`

## Источники

- https://en.cppreference.com/w/cpp/utility/integer_sequence/make_integer_sequence
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/index_sequence|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/make_index_sequence|Вперёд]]
