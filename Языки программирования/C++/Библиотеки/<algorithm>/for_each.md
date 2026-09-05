# for_each

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / for_each

[[Языки программирования/C++/Библиотеки/<algorithm>/none_of|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/count|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class UnaryFunction>
UnaryFunction for_each(InputIt first, InputIt last, UnaryFunction f);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `f` | Функция для применения к каждому элементу |

## Возвращаемое значение

`f` (после применения ко всем элементам).

## Что делает

Применяет функцию `f` к каждому элементу в диапазоне `[first, last)`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5};

    std::for_each(v.begin(), v.end(), [](int x){
        std::cout << x * x << " ";
    });
    // Вывод: 1 4 9 16 25
}
```

## Исключения

- **Исключения:** может бросать исключения, если `f` бросает.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/count|count]] — подсчёт значений

## Источники

- https://en.cppreference.com/w/cpp/algorithm/for_each
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/none_of|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/count|Вперёд]]
