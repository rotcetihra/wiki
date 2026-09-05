# swap_ranges

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / swap_ranges

[[Языки программирования/C++/Библиотеки/<algorithm>/stable_partition|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/iter_swap|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt1, class ForwardIt2>
ForwardIt2 swap_ranges(ForwardIt1 first1, ForwardIt1 last1, ForwardIt2 first2);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first1`, `last1` | Первый диапазон |
| `first2` | Начало второго диапазона |

## Возвращаемое значение

Итератор за последний обменённый элемент во втором диапазоне.

## Что делает

Обменивает элементы из двух диапазонов попарно.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> a = {1, 2, 3};
    std::vector<int> b = {4, 5, 6};

    std::swap_ranges(a.begin(), a.end(), b.begin());
    // a: {4, 5, 6}, b: {1, 2, 3}
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/iter_swap|iter_swap]] — обмен двух элементов

## Источники

- https://en.cppreference.com/w/cpp/algorithm/swap_ranges
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/stable_partition|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/iter_swap|Вперёд]]
