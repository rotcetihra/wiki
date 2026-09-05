# search_n

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / search_n

[[Языки программирования/C++/Библиотеки/<algorithm>/search|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/copy|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt, class Size, class T>
ForwardIt search_n(ForwardIt first, ForwardIt last, Size count, const T& value);

template<class ForwardIt, class Size, class T, class BinaryPredicate>
ForwardIt search_n(ForwardIt first, ForwardIt last, Size count, const T& value,
                   BinaryPredicate p);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `count` | Количество искомых подряд идущих элементов |
| `value` | Искомое значение |
| `p` | Бинарный предикат |

## Возвращаемое значение

Итератор на начало последовательности из `count` элементов, равных `value`. Если не найдено — `last`.

## Что делает

Ищет последовательность из `count` подряд идущих элементов, равных `value`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 2, 2, 3, 4};

    auto it = std::search_n(v.begin(), v.end(), 3, 2);
    if (it != v.end())
        std::cout << "Найдено 3 двойки подряд" << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/search|search]] — поиск подпоследовательности

## Источники

- https://en.cppreference.com/w/cpp/algorithm/search_n
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/search|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/copy|Вперёд]]
