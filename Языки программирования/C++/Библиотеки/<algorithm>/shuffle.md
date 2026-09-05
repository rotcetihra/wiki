# shuffle

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / shuffle

[[Языки программирования/C++/Библиотеки/<algorithm>/rotate_copy|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/unique|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class RandomIt, class URBG>
void shuffle(RandomIt first, RandomIt last, URBG&& g);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `g` | Генератор псевдослучайных чисел |

## Возвращаемое значение

Не возвращает значения.

## Что делает

Перемешивает элементы в диапазоне `[first, last)` случайным образом. Каждая перестановка равновероятна.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <random>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5};

    std::random_device rd;
    std::mt19937 gen(rd());

    std::shuffle(v.begin(), v.end(), gen);
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/reverse|reverse]] — разворот

## Источники

- https://en.cppreference.com/w/cpp/algorithm/shuffle
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/rotate_copy|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/unique|Вперёд]]
