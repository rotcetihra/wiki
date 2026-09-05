# count

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / count

[[Языки программирования/C++/Библиотеки/<algorithm>/for_each|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/count_if|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class T>
typename iterator_traits<InputIt>::difference_type
    count(InputIt first, InputIt last, const T& value);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `value` | Искомое значение |

## Возвращаемое значение

Количество элементов, равных `value`.

## Что делает

Подсчитывает количество элементов, равных `value`, в диапазоне `[first, last)`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 3, 2, 4, 2};

    auto n = std::count(v.begin(), v.end(), 2);
    std::cout << "Количество 2: " << n << std::endl; // 3
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/count_if|count_if]] — подсчёт по предикату

## Источники

- https://en.cppreference.com/w/cpp/algorithm/count
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/for_each|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/count_if|Вперёд]]
