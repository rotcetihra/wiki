# inplace_merge

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / inplace_merge

[[Языки программирования/C++/Библиотеки/<algorithm>/merge|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/set_union|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class BidirIt>
void inplace_merge(BidirIt first, BidirIt middle, BidirIt last);

template<class BidirIt, class Compare>
void inplace_merge(BidirIt first, BidirIt middle, BidirIt last, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first` | Начало первого отсортированного диапазона |
| `middle` | Конец первого / начало второго диапазона |
| `last` | Конец второго диапазона |
| `comp` | Функция сравнения |

## Возвращаемое значение

Не возвращает значения.

## Что делает

Сливает два смежных отсортированных поддиапазона `[first, middle)` и `[middle, last)` в один отсортированный диапазон на месте. Временная сложность O(N log N).

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 3, 5, 2, 4, 6};

    std::inplace_merge(v.begin(), v.begin() + 3, v.end());
    // v: {1, 2, 3, 4, 5, 6}
}
```

## Исключения

- **Исключения:** может бросать исключения при нехватке памяти.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/merge|merge]] — слияние в выходной диапазон

## Источники

- https://en.cppreference.com/w/cpp/algorithm/inplace_merge
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/merge|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/set_union|Вперёд]]
