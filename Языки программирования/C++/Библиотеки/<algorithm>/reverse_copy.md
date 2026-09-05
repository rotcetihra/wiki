# reverse_copy

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / reverse_copy

[[Языки программирования/C++/Библиотеки/<algorithm>/reverse|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/rotate|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class BidirIt, class OutputIt>
OutputIt reverse_copy(BidirIt first, BidirIt last, OutputIt d_first);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон для копирования |
| `d_first` | Начало выходного диапазона |

## Возвращаемое значение

Итератор за последний скопированный элемент.

## Что делает

Копирует элементы из исходного диапазона в обратном порядке в выходной диапазон.

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> src = {1, 2, 3, 4, 5};
    std::vector<int> dst(5);

    std::reverse_copy(src.begin(), src.end(), dst.begin());
    // dst: {5, 4, 3, 2, 1}
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/reverse|reverse]] — разворот на месте

## Источники

- https://en.cppreference.com/w/cpp/algorithm/reverse_copy
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/reverse|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/rotate|Вперёд]]
