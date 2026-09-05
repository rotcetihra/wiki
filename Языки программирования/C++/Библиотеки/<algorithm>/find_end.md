# find_end

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / find_end

[[Языки программирования/C++/Библиотеки/<algorithm>/find_if|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/find_first_of|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt1, class ForwardIt2>
ForwardIt1 find_end(ForwardIt1 first1, ForwardIt1 last1,
                    ForwardIt2 first2, ForwardIt2 last2);

template<class ForwardIt1, class ForwardIt2, class BinaryPredicate>
ForwardIt1 find_end(ForwardIt1 first1, ForwardIt1 last1,
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

Итератор на начало последнего вхождения подпоследовательности. Если не найдено — `last1`.

## Что делает

Ищет последнее вхождение подпоследовательности `[first2, last2)` в диапазоне `[first1, last1)`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 3, 1, 2, 3, 4};
    std::vector<int> sub = {1, 2};

    auto it = std::find_end(v.begin(), v.end(), sub.begin(), sub.end());
    if (it != v.end())
        std::cout << "Последнее вхождение на позиции: " << std::distance(v.begin(), it) << std::endl;
    // 3
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/search|search]] — поиск первого вхождения подпоследовательности

## Источники

- https://en.cppreference.com/w/cpp/algorithm/find_end
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/find_if|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/find_first_of|Вперёд]]
