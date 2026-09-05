# generate

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / generate

[[Языки программирования/C++/Библиотеки/<algorithm>/fill_n|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/generate_n|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt, class Generator>
void generate(ForwardIt first, ForwardIt last, Generator g);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `g` | Генератор значений |

## Возвращаемое значение

Не возвращает значения.

## Что делает

Заполняет диапазон значениями, возвращаемыми генератором `g`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v(5);
    int n = 0;

    std::generate(v.begin(), v.end(), [&n]{ return ++n; });
    // v: {1, 2, 3, 4, 5}
}
```

## Исключения

- **Исключения:** может бросать исключения, если `g` бросает.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/generate_n|generate_n]] — генерация n элементов
- [[Языки программирования/C++/Библиотеки/<algorithm>/fill|fill]] — заполнение значением

## Источники

- https://en.cppreference.com/w/cpp/algorithm/generate
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/fill_n|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/generate_n|Вперёд]]
