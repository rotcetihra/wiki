# copy_n

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / copy_n

[[Языки программирования/C++/Библиотеки/<algorithm>/copy_if|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/copy_backward|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class Size, class OutputIt>
OutputIt copy_n(InputIt first, Size count, OutputIt d_first);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first` | Начало входного диапазона |
| `count` | Количество элементов для копирования |
| `d_first` | Начало выходного диапазона |

## Возвращаемое значение

Итератор за последний скопированный элемент.

## Что делает

Копирует `count` элементов, начиная с `first`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> src = {1, 2, 3, 4, 5};
    std::vector<int> dst(3);

    std::copy_n(src.begin(), 3, dst.begin());
    // dst: {1, 2, 3}
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/copy|copy]] — копирование всего диапазона

## Источники

- https://en.cppreference.com/w/cpp/algorithm/copy_n
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/copy_if|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/copy_backward|Вперёд]]
