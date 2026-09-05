# distance

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / distance

[[Языки программирования/C++/Библиотеки/<algorithm>/advance|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/next|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>

template<class InputIt>
typename iterator_traits<InputIt>::difference_type
    distance(InputIt first, InputIt last);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first` | Начальный итератор |
| `last` | Конечный итератор |

## Возвращаемое значение

Расстояние между итераторами.

## Что делает

Возвращает количество элементов между `first` и `last`. Для итераторов ввода расстояние вычисляется за O(N).

## Примеры

```cpp
#include <vector>
#include <iostream>
#include <iterator>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5};

    auto d = std::distance(v.begin(), v.end());
    std::cout << "Размер: " << d << std::endl; // 5
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/advance|advance]] — продвижение итератора

## Источники

- https://en.cppreference.com/w/cpp/iterator/distance
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/advance|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/next|Вперёд]]
