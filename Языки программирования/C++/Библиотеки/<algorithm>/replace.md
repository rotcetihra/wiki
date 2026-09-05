# replace

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / replace

[[Языки программирования/C++/Библиотеки/<algorithm>/remove_copy_if|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/replace_if|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt, class T>
void replace(ForwardIt first, ForwardIt last,
             const T& old_value, const T& new_value);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `old_value` | Значение для замены |
| `new_value` | Новое значение |

## Возвращаемое значение

Не возвращает значения.

## Что делает

Заменяет все элементы, равные `old_value`, на `new_value` в диапазоне `[first, last)`.

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> v = {1, 2, 3, 2, 4, 2};

    std::replace(v.begin(), v.end(), 2, 99);
    // v: {1, 99, 3, 99, 4, 99}
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/replace_if|replace_if]] — замена по предикату

## Источники

- https://en.cppreference.com/w/cpp/algorithm/replace
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/remove_copy_if|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/replace_if|Вперёд]]
