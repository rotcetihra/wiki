# equal_range

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / equal_range

[[Языки программирования/C++/Библиотеки/<algorithm>/upper_bound|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/merge|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt, class T>
std::pair<ForwardIt, ForwardIt>
    equal_range(ForwardIt first, ForwardIt last, const T& value);

template<class ForwardIt, class T, class Compare>
std::pair<ForwardIt, ForwardIt>
    equal_range(ForwardIt first, ForwardIt last, const T& value, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Отсортированный диапазон итераторов |
| `value` | Искомое значение |
| `comp` | Функция сравнения |

## Возвращаемое значение

Пара итераторов: `[lower_bound, upper_bound)`.

## Что делает

Находит диапазон всех элементов, равных `value`. Эквивалентно вызову `lower_bound` и `upper_bound`. Временная сложность O(log N).

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 3, 5, 5, 5, 7, 9};

    auto [lo, hi] = std::equal_range(v.begin(), v.end(), 5);
    std::cout << "Количество: " << std::distance(lo, hi) << std::endl; // 3
}
```

## Исключения

- **Исключения:** не бросает исключений (если компаратор не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/lower_bound|lower_bound]] — нижняя граница
- [[Языки программирования/C++/Библиотеки/<algorithm>/upper_bound|upper_bound]] — верхняя граница

## Источники

- https://en.cppreference.com/w/cpp/algorithm/equal_range
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/upper_bound|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/merge|Вперёд]]
