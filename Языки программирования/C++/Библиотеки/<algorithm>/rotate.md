# rotate

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / rotate

[[Языки программирования/C++/Библиотеки/<algorithm>/reverse_copy|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/rotate_copy|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt>
ForwardIt rotate(ForwardIt first, ForwardIt middle, ForwardIt last);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first` | Начало диапазона |
| `middle` | Новый первый элемент |
| `last` | Конец диапазона |

## Возвращаемое значение

Итератор на элемент, который раньше стоял первым.

## Что делает

Циклически сдвигает элементы в диапазоне `[first, last)` так, что `middle` становится первым элементом.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5};

    std::rotate(v.begin(), v.begin() + 2, v.end());
    // v: {3, 4, 5, 1, 2}
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/rotate_copy|rotate_copy]] — копирование после вращения

## Источники

- https://en.cppreference.com/w/cpp/algorithm/rotate
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/reverse_copy|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/rotate_copy|Вперёд]]
