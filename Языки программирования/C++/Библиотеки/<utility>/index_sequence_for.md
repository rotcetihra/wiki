# index_sequence_for

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / index_sequence_for

[[Языки программирования/C++/Библиотеки/<utility>/make_index_sequence|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/exchange|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<class... Types>
using index_sequence_for = std::make_index_sequence<sizeof...(Types)>;
```

## Параметры

| Параметр | Описание |
|---|---|
| `Types` | Параметрический пакет типов |

## Возвращаемое значение

`index_sequence<0, 1, ..., sizeof...(Types)-1>`.

## Что делает

Создаёт последовательность индексов по количеству типов в пакете параметров.

## Примеры

```cpp
#include <utility>
#include <iostream>

int main()
{
    using seq = std::index_sequence_for<int, double, char>; // 0,1,2
    std::cout << seq::size() << std::endl; // 3
}
```

## Исключения

- **Исключения:** операция времени компиляции.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<utility>/make_index_sequence|make_index_sequence]] — по размеру

## Источники

- https://en.cppreference.com/w/cpp/utility/index_sequence/index_sequence_for
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/make_index_sequence|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/exchange|Вперёд]]
