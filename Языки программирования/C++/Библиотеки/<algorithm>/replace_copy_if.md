# replace_copy_if

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / replace_copy_if

[[Языки программирования/C++/Библиотеки/<algorithm>/replace_copy|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/reverse|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class OutputIt, class UnaryPredicate, class T>
OutputIt replace_copy_if(InputIt first, InputIt last,
                         OutputIt d_first,
                         UnaryPredicate p, const T& new_value);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон для копирования |
| `d_first` | Начало выходного диапазона |
| `p` | Унарный предикат |
| `new_value` | Новое значение |

## Возвращаемое значение

Итератор за последний скопированный элемент.

## Что делает

Копирует элементы, заменяя те, для которых `p` возвращает `true`, на `new_value`.

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> src = {1, 2, 3, 4, 5};
    std::vector<int> dst(5);

    std::replace_copy_if(src.begin(), src.end(), dst.begin(),
                         [](int x){ return x % 2 == 0; }, 0);
    // dst: {1, 0, 3, 0, 5}
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/replace_copy|replace_copy]] — копирование с заменой по значению

## Источники

- https://en.cppreference.com/w/cpp/algorithm/replace_copy_if
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/replace_copy|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/reverse|Вперёд]]
