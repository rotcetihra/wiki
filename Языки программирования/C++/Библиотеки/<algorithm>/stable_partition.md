# stable_partition

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / stable_partition

[[Языки программирования/C++/Библиотеки/<algorithm>/is_partitioned|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/swap_ranges|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class BidirIt, class UnaryPredicate>
BidirIt stable_partition(BidirIt first, BidirIt last, UnaryPredicate p);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `p` | Унарный предикат |

## Возвращаемое значение

Итератор на первый элемент второй группы.

## Что делает

Разбивает диапазон на две группы, сохраняя относительный порядок элементов в каждой группе.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5, 6};

    auto mid = std::stable_partition(v.begin(), v.end(), [](int x){ return x % 2 == 0; });
    // v: {2, 4, 6, 1, 3, 5} — порядок сохранён
}
```

## Исключения

- **Исключения:** может бросать исключения при нехватке памяти.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/partition|partition]] — неустойчивое разбиение

## Источники

- https://en.cppreference.com/w/cpp/algorithm/stable_partition
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/is_partitioned|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/swap_ranges|Вперёд]]
