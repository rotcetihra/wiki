# remove_if

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / remove_if

[[Языки программирования/C++/Библиотеки/<algorithm>/remove|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/remove_copy|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt, class UnaryPredicate>
ForwardIt remove_if(ForwardIt first, ForwardIt last, UnaryPredicate p);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `p` | Унарный предикат |

## Возвращаемое значение

Итератор на «новый конец» диапазона.

## Что делает

Удаляет все элементы, для которых `p` возвращает `true`.

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5, 6};

    auto new_end = std::remove_if(v.begin(), v.end(), [](int x){ return x % 2 == 0; });
    v.erase(new_end, v.end());
    // v: {1, 3, 5}
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/remove|remove]] — удаление по значению

## Источники

- https://en.cppreference.com/w/cpp/algorithm/remove_if
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/remove|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/remove_copy|Вперёд]]
