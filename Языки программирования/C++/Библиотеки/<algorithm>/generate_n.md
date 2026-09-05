# generate_n

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / generate_n

[[Языки программирования/C++/Библиотеки/<algorithm>/generate|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/remove|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class OutputIt, class Size, class Generator>
OutputIt generate_n(OutputIt first, Size count, Generator g);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first` | Начало выходного диапазона |
| `count` | Количество элементов для генерации |
| `g` | Генератор значений |

## Возвращаемое значение

Итератор за последний сгенерированный элемент.

## Что делает

Заполняет `count` элементов значениями, возвращаемыми `g`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v(5);

    std::generate_n(v.begin(), 5, [n = 0]() mutable { return n++; });
    // v: {0, 1, 2, 3, 4}
}
```

## Исключения

- **Исключения:** может бросать исключения, если `g` бросает.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/generate|generate]] — генерация всего диапазона

## Источники

- https://en.cppreference.com/w/cpp/algorithm/generate_n
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/generate|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/remove|Вперёд]]
