# find

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / find

[[Языки программирования/C++/Библиотеки/<algorithm>/count_if|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/find_if|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class T>
InputIt find(InputIt first, InputIt last, const T& value);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `value` | Искомое значение |

## Возвращаемое значение

Итератор на первый элемент, равный `value`. Если не найден — `last`.

## Что делает

Ищет первое вхождение `value` в диапазоне `[first, last)`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5};

    auto it = std::find(v.begin(), v.end(), 3);
    if (it != v.end())
        std::cout << "Найдено: " << *it << std::endl; // 3
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/find_if|find_if]] — поиск по предикату

## Источники

- https://en.cppreference.com/w/cpp/algorithm/find
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/count_if|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/find_if|Вперёд]]
