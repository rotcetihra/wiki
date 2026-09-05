# upper_bound

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / upper_bound

[[Языки программирования/C++/Библиотеки/<algorithm>/lower_bound|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/equal_range|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt, class T>
ForwardIt upper_bound(ForwardIt first, ForwardIt last, const T& value);

template<class ForwardIt, class T, class Compare>
ForwardIt upper_bound(ForwardIt first, ForwardIt last, const T& value, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Отсортированный диапазон итераторов |
| `value` | Искомое значение |
| `comp` | Функция сравнения |

## Возвращаемое значение

Итератор на первый элемент, больший `value`.

## Что делает

Находит первую позицию, куда можно вставить `value` чтобы все элементы перед ним были не больше `value`. Временная сложность O(log N).

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 3, 5, 5, 7, 9};

    auto it = std::upper_bound(v.begin(), v.end(), 5);
    std::cout << *it << std::endl; // 7
}
```

## Исключения

- **Исключения:** не бросает исключений (если компаратор не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/lower_bound|lower_bound]] — нижняя граница
- [[Языки программирования/C++/Библиотеки/<algorithm>/equal_range|equal_range]] — диапазон равных элементов

## Источники

- https://en.cppreference.com/w/cpp/algorithm/upper_bound
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/lower_bound|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/equal_range|Вперёд]]
