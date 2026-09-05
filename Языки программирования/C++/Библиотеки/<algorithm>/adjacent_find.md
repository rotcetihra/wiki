# adjacent_find

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / adjacent_find

[[Языки программирования/C++/Библиотеки/<algorithm>/find_first_of|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/search|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt>
ForwardIt adjacent_find(ForwardIt first, ForwardIt last);

template<class ForwardIt, class BinaryPredicate>
ForwardIt adjacent_find(ForwardIt first, ForwardIt last, BinaryPredicate p);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `p` | Бинарный предикат |

## Возвращаемое значение

Итератор на первый из двух соседних равных элементов. Если не найдено — `last`.

## Что делает

Ищет первые два соседних элемента, которые равны (или удовлетворяют предикату `p`).

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 3, 3, 4, 5};

    auto it = std::adjacent_find(v.begin(), v.end());
    if (it != v.end())
        std::cout << "Соседние равные: " << *it << std::endl; // 3
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/search|search]] — поиск подпоследовательности

## Источники

- https://en.cppreference.com/w/cpp/algorithm/adjacent_find
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/find_first_of|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/search|Вперёд]]
