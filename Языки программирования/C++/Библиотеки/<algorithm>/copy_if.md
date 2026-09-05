# copy_if

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / copy_if

[[Языки программирования/C++/Библиотеки/<algorithm>/copy|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/copy_n|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class OutputIt, class UnaryPredicate>
OutputIt copy_if(InputIt first, InputIt last,
                 OutputIt d_first, UnaryPredicate p);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон для копирования |
| `d_first` | Начало выходного диапазона |
| `p` | Унарный предикат |

## Возвращаемое значение

Итератор за последний скопированный элемент.

## Что делает

Копирует только элементы, для которых предикат `p` возвращает `true`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> src = {1, 2, 3, 4, 5, 6};
    std::vector<int> dst;

    std::copy_if(src.begin(), src.end(), std::back_inserter(dst),
                 [](int x){ return x % 2 == 0; });
    // dst: {2, 4, 6}
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/copy|copy]] — безусловное копирование
- [[Языки программирования/C++/Библиотеки/<algorithm>/copy_n|copy_n]] — копирование n элементов

## Источники

- https://en.cppreference.com/w/cpp/algorithm/copy_if
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/copy|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/copy_n|Вперёд]]
