# replace_if

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / replace_if

[[Языки программирования/C++/Библиотеки/<algorithm>/replace|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/replace_copy|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt, class UnaryPredicate, class T>
void replace_if(ForwardIt first, ForwardIt last,
                UnaryPredicate p, const T& new_value);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `p` | Унарный предикат |
| `new_value` | Новое значение |

## Возвращаемое значение

Не возвращает значения.

## Что делает

Заменяет все элементы, для которых `p` возвращает `true`, на `new_value`.

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5, 6};

    std::replace_if(v.begin(), v.end(), [](int x){ return x % 2 == 0; }, 0);
    // v: {1, 0, 3, 0, 5, 0}
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/replace|replace]] — замена по значению

## Источники

- https://en.cppreference.com/w/cpp/algorithm/replace_if
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/replace|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/replace_copy|Вперёд]]
