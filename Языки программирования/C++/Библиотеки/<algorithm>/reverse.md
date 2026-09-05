# reverse

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / reverse

[[Языки программирования/C++/Библиотеки/<algorithm>/replace_copy_if|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/reverse_copy|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class BidirIt>
void reverse(BidirIt first, BidirIt last);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |

## Возвращаемое значение

Не возвращает значения.

## Что делает

Разворачивает порядок элементов в диапазоне `[first, last)`.

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5};

    std::reverse(v.begin(), v.end());
    // v: {5, 4, 3, 2, 1}
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/reverse_copy|reverse_copy]] — копирование в обратном порядке

## Источники

- https://en.cppreference.com/w/cpp/algorithm/reverse
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/replace_copy_if|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/reverse_copy|Вперёд]]
