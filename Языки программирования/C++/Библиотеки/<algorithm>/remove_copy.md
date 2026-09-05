# remove_copy

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / remove_copy

[[Языки программирования/C++/Библиотеки/<algorithm>/remove_if|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/remove_copy_if|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class OutputIt, class T>
OutputIt remove_copy(InputIt first, InputIt last,
                     OutputIt d_first, const T& value);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон для копирования |
| `d_first` | Начало выходного диапазона |
| `value` | Значение для исключения |

## Возвращаемое значение

Итератор за последний скопированный элемент.

## Что делает

Копирует элементы из исходного диапазона, пропуская элементы равные `value`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> src = {1, 2, 3, 2, 4};
    std::vector<int> dst;

    std::remove_copy(src.begin(), src.end(), std::back_inserter(dst), 2);
    // dst: {1, 3, 4}
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/remove_copy_if|remove_copy_if]] — копирование без удалённых по предикату

## Источники

- https://en.cppreference.com/w/cpp/algorithm/remove_copy
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/remove_if|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/remove_copy_if|Вперёд]]
