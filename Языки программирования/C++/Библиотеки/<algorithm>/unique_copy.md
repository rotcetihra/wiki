# unique_copy

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / unique_copy

[[Языки программирования/C++/Библиотеки/<algorithm>/unique|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/partition|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class OutputIt>
OutputIt unique_copy(InputIt first, InputIt last, OutputIt d_first);

template<class InputIt, class OutputIt, class BinaryPredicate>
OutputIt unique_copy(InputIt first, InputIt last, OutputIt d_first,
                     BinaryPredicate p);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон для копирования |
| `d_first` | Начало выходного диапазона |
| `p` | Бинарный предикат |

## Возвращаемое значение

Итератор за последний скопированный элемент.

## Что делает

Копирует элементы, удаляя подряд идущие дубликаты.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> src = {1, 1, 2, 2, 3, 3, 3};
    std::vector<int> dst;

    std::unique_copy(src.begin(), src.end(), std::back_inserter(dst));
    // dst: {1, 2, 3}
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/unique|unique]] — удаление дубликатов на месте

## Источники

- https://en.cppreference.com/w/cpp/algorithm/unique_copy
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/unique|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/partition|Вперёд]]
