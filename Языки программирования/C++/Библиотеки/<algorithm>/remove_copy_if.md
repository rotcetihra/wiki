# remove_copy_if

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / remove_copy_if

[[Языки программирования/C++/Библиотеки/<algorithm>/remove_copy|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/replace|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class OutputIt, class UnaryPredicate>
OutputIt remove_copy_if(InputIt first, InputIt last,
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

Копирует элементы, пропуская те, для которых `p` возвращает `true`.

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> src = {1, 2, 3, 4, 5, 6};
    std::vector<int> dst;

    std::remove_copy_if(src.begin(), src.end(), std::back_inserter(dst),
                        [](int x){ return x % 2 == 0; });
    // dst: {1, 3, 5}
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/remove_copy|remove_copy]] — копирование без удалённых по значению

## Источники

- https://en.cppreference.com/w/cpp/algorithm/remove_copy_if
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/remove_copy|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/replace|Вперёд]]
