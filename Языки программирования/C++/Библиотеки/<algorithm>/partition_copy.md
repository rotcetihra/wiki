# partition_copy

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / partition_copy

[[Языки программирования/C++/Библиотеки/<algorithm>/partition|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/is_partitioned|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class OutputIt1, class OutputIt2, class UnaryPredicate>
std::pair<OutputIt1, OutputIt2>
    partition_copy(InputIt first, InputIt last,
                   OutputIt1 d_first_true, OutputIt2 d_first_false,
                   UnaryPredicate p);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон для разбиения |
| `d_first_true` | Начало выходного диапазона для `true` |
| `d_first_false` | Начало выходного диапазона для `false` |
| `p` | Унарный предикат |

## Возвращаемое значение

Пара итераторов за последний элемент в каждом выходном диапазоне.

## Что делает

Копирует элементы в два выходных диапазона: для которых `p` возвращает `true` — в первый, `false` — во второй.

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> src = {1, 2, 3, 4, 5, 6};
    std::vector<int> evens, odds;

    std::partition_copy(src.begin(), src.end(),
                        std::back_inserter(evens),
                        std::back_inserter(odds),
                        [](int x){ return x % 2 == 0; });
    // evens: {2, 4, 6}, odds: {1, 3, 5}
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/partition|partition]] — разбиение на месте

## Источники

- https://en.cppreference.com/w/cpp/algorithm/partition_copy
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/partition|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/is_partitioned|Вперёд]]
