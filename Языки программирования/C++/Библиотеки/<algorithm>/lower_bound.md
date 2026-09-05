# lower_bound

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / lower_bound

[[Языки программирования/C++/Библиотеки/<algorithm>/binary_search|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/upper_bound|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt, class T>
ForwardIt lower_bound(ForwardIt first, ForwardIt last, const T& value);

template<class ForwardIt, class T, class Compare>
ForwardIt lower_bound(ForwardIt first, ForwardIt last, const T& value, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Отсортированный диапазон итераторов |
| `value` | Искомое значение |
| `comp` | Функция сравнения |

## Возвращаемое значение

Итератор на первый элемент, не меньший `value`.

## Что делает

Находит первую позицию, куда можно вставить `value` без нарушения порядка. Временная сложность O(log N).

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 3, 5, 7, 9};

    auto it = std::lower_bound(v.begin(), v.end(), 5);
    std::cout << *it << std::endl; // 5
}
```

## Исключения

- **Исключения:** не бросает исключений (если компаратор не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/upper_bound|upper_bound]] — верхняя граница
- [[Языки программирования/C++/Библиотеки/<algorithm>/binary_search|binary_search]] — бинарный поиск

## Источники

- https://en.cppreference.com/w/cpp/algorithm/lower_bound
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/binary_search|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/upper_bound|Вперёд]]
