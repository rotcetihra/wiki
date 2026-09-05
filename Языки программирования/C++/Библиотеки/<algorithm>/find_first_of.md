# find_first_of

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / find_first_of

[[Языки программирования/C++/Библиотеки/<algorithm>/find_end|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/adjacent_find|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class ForwardIt>
InputIt find_first_of(InputIt first1, InputIt last1,
                      ForwardIt first2, ForwardIt last2);

template<class InputIt, class ForwardIt, class BinaryPredicate>
InputIt find_first_of(InputIt first1, InputIt last1,
                      ForwardIt first2, ForwardIt last2,
                      BinaryPredicate p);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first1`, `last1` | Диапазон для поиска |
| `first2`, `last2` | Множество искомых элементов |
| `p` | Бинарный предикат |

## Возвращаемое значение

Итератор на первый элемент из первого диапазона, который есть во втором. Если не найден — `last1`.

## Что делает

Ищет первое вхождение любого из элементов диапазона `[first2, last2)` в диапазоне `[first1, last1)`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5};
    std::vector<int> targets = {4, 6, 8};

    auto it = std::find_first_of(v.begin(), v.end(), targets.begin(), targets.end());
    if (it != v.end())
        std::cout << "Найдено: " << *it << std::endl; // 4
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/find|find]] — поиск одного значения
- [[Языки программирования/C++/Библиотеки/<algorithm>/find_end|find_end]] — поиск подпоследовательности

## Источники

- https://en.cppreference.com/w/cpp/algorithm/find_first_of
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/find_end|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/adjacent_find|Вперёд]]
