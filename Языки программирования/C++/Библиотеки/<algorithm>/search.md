# search

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / search

[[Языки программирования/C++/Библиотеки/<algorithm>/adjacent_find|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/search_n|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt1, class ForwardIt2>
ForwardIt1 search(ForwardIt1 first1, ForwardIt1 last1,
                  ForwardIt2 first2, ForwardIt2 last2);

template<class ForwardIt1, class ForwardIt2, class BinaryPredicate>
ForwardIt1 search(ForwardIt1 first1, ForwardIt1 last1,
                  ForwardIt2 first2, ForwardIt2 last2,
                  BinaryPredicate p);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first1`, `last1` | Диапазон для поиска |
| `first2`, `last2` | Искомая подпоследовательность |
| `p` | Бинарный предикат |

## Возвращаемое значение

Итератор на начало первого вхождения подпоследовательности. Если не найдено — `last1`.

## Что делает

Ищет первое вхождение подпоследовательности `[first2, last2)` в диапазоне `[first1, last1)`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5};
    std::vector<int> sub = {3, 4};

    auto it = std::search(v.begin(), v.end(), sub.begin(), sub.end());
    if (it != v.end())
        std::cout << "Найдено на позиции: " << std::distance(v.begin(), it) << std::endl; // 2
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/find_end|find_end]] — последнее вхождение подпоследовательности
- [[Языки программирования/C++/Библиотеки/<algorithm>/search_n|search_n]] — поиск n подряд идущих элементов

## Источники

- https://en.cppreference.com/w/cpp/algorithm/search
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/adjacent_find|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/search_n|Вперёд]]
