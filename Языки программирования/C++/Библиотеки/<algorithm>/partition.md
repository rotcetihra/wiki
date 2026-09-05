# partition

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / partition

[[Языки программирования/C++/Библиотеки/<algorithm>/unique_copy|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/partition_copy|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt, class UnaryPredicate>
ForwardIt partition(ForwardIt first, ForwardIt last, UnaryPredicate p);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `p` | Унарный предикат |

## Возвращаемое значение

Итератор на первый элемент второй группы (для которого `p` возвращает `false`).

## Что делает

Разбивает диапазон на две группы: элементы, для которых `p` возвращает `true`, идут перед элементами, для которых `p` возвращает `false`. Относительный порядок не сохраняется.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5, 6};

    auto mid = std::partition(v.begin(), v.end(), [](int x){ return x % 2 == 0; });
    // v: {6, 2, 4, 3, 1, 5} (чётные в начале, порядок не гарантирован)
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/stable_partition|stable_partition]] — устойчивое разбиение
- [[Языки программирования/C++/Библиотеки/<algorithm>/partition_copy|partition_copy]] — копирование с разбиением

## Источники

- https://en.cppreference.com/w/cpp/algorithm/partition
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/unique_copy|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/partition_copy|Вперёд]]
