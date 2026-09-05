# iter_swap

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / iter_swap

[[Языки программирования/C++/Библиотеки/<algorithm>/swap_ranges|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/reverse_iterator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt1, class ForwardIt2>
void iter_swap(ForwardIt1 a, ForwardIt2 b);
```

## Параметры

| Параметр | Описание |
|---|---|
| `a`, `b` | Итераторы на обмениваемые элементы |

## Возвращаемое значение

Не возвращает значения.

## Что делает

Обменивает значения элементов, на которые указывают итераторы `a` и `b`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5};

    std::iter_swap(v.begin(), v.begin() + 4);
    // v: {5, 2, 3, 4, 1}
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/swap_ranges|swap_ranges]] — обмен диапазонов

## Источники

- https://en.cppreference.com/w/cpp/algorithm/iter_swap
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/swap_ranges|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/reverse_iterator|Вперёд]]
