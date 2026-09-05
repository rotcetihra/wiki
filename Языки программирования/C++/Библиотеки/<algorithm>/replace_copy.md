# replace_copy

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / replace_copy

[[Языки программирования/C++/Библиотеки/<algorithm>/replace_if|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/replace_copy_if|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class OutputIt, class T>
OutputIt replace_copy(InputIt first, InputIt last,
                      OutputIt d_first,
                      const T& old_value, const T& new_value);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон для копирования |
| `d_first` | Начало выходного диапазона |
| `old_value` | Значение для замены |
| `new_value` | Новое значение |

## Возвращаемое значение

Итератор за последний скопированный элемент.

## Что делает

Копирует элементы, заменяя `old_value` на `new_value`. Исходный диапазон не изменяется.

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> src = {1, 2, 3, 2, 4};
    std::vector<int> dst(5);

    std::replace_copy(src.begin(), src.end(), dst.begin(), 2, 99);
    // dst: {1, 99, 3, 99, 4}
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/replace_copy_if|replace_copy_if]] — копирование с заменой по предикату

## Источники

- https://en.cppreference.com/w/cpp/algorithm/replace_copy
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/replace_if|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/replace_copy_if|Вперёд]]
