# count_if

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / count_if

[[Языки программирования/C++/Библиотеки/<algorithm>/count|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/find|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class UnaryPredicate>
typename iterator_traits<InputIt>::difference_type
    count_if(InputIt first, InputIt last, UnaryPredicate p);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `p` | Унарный предикат |

## Возвращаемое значение

Количество элементов, для которых `p` возвращает `true`.

## Что делает

Подсчитывает количество элементов, удовлетворяющих предикату `p`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5, 6};

    auto n = std::count_if(v.begin(), v.end(), [](int x){ return x % 2 == 0; });
    std::cout << "Чётных: " << n << std::endl; // 3
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/count|count]] — подсчёт значений

## Источники

- https://en.cppreference.com/w/cpp/algorithm/count_if
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/count|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/find|Вперёд]]
