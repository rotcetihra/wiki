# move

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / move

[[Языки программирования/C++/Библиотеки/<algorithm>/copy_backward|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/move_backward|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class OutputIt>
OutputIt move(InputIt first, InputIt last, OutputIt d_first);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон для перемещения |
| `d_first` | Начало выходного диапазона |

## Возвращаемое значение

Итератор за последний перемещённый элемент.

## Что делает

Перемещает элементы из диапазона `[first, last)` в выходной диапазон. После перемещения исходные элементы остаются в неопределённом, но допустимом состоянии.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>

int main()
{
    std::vector<std::string> src = {"hello", "world"};
    std::vector<std::string> dst(2);

    std::move(src.begin(), src.end(), dst.begin());
    // dst: {"hello", "world"}, src: {"", ""}
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/move_backward|move_backward]] — перемещение в обратном порядке
- [[Языки программирования/C++/Библиотеки/<algorithm>/copy|copy]] — копирование

## Источники

- https://en.cppreference.com/w/cpp/algorithm/move
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/copy_backward|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/move_backward|Вперёд]]
