# move_backward

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / move_backward

[[Языки программирования/C++/Библиотеки/<algorithm>/move|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/fill|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class BidirIt1, class BidirIt2>
BidirIt2 move_backward(BidirIt1 first, BidirIt1 last, BidirIt2 d_last);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон для перемещения |
| `d_last` | Конец выходного диапазона |

## Возвращаемое значение

Итератор на первый перемещённый элемент.

## Что делает

Перемещает элементы из диапазона `[first, last)` в выходной диапазон, заканчиваясь на `d_last`. Элементы перемещаются в обратном порядке.

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> src = {1, 2, 3, 4, 5};
    std::vector<int> dst(5);

    std::move_backward(src.begin(), src.end(), dst.end());
    // dst: {1, 2, 3, 4, 5}
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/move|move]] — перемещение в прямом порядке

## Источники

- https://en.cppreference.com/w/cpp/algorithm/move_backward
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/move|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/fill|Вперёд]]
