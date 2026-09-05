# rotate_copy

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / rotate_copy

[[Языки программирования/C++/Библиотеки/<algorithm>/rotate|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/shuffle|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt, class OutputIt>
OutputIt rotate_copy(ForwardIt first, ForwardIt middle, ForwardIt last,
                     OutputIt d_first);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first` | Начало диапазона |
| `middle` | Новый первый элемент |
| `last` | Конец диапазона |
| `d_first` | Начало выходного диапазона |

## Возвращаемое значение

Итератор за последний скопированный элемент.

## Что делает

Копирует элементы после циклического сдвига в выходной диапазон.

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> src = {1, 2, 3, 4, 5};
    std::vector<int> dst(5);

    std::rotate_copy(src.begin(), src.begin() + 2, src.end(), dst.begin());
    // dst: {3, 4, 5, 1, 2}
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/rotate|rotate]] — вращение на месте

## Источники

- https://en.cppreference.com/w/cpp/algorithm/rotate_copy
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/rotate|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/shuffle|Вперёд]]
