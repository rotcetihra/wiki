# make_pair

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / make_pair

[[Языки программирования/C++/Библиотеки/<utility>/pair|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/piecewise_construct|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<class T1, class T2>
constexpr std::pair<V1, V2> make_pair(T1&& t1, T2&& t2);
```

## Параметры

| Параметр | Описание |
|---|---|
| `t1` | Первое значение |
| `t2` | Второе значение |

## Возвращаемое значение

`std::pair<V1, V2>`, где `V1`/`V2` — типы с учётом reference collapsing.

## Что делает

Создаёт `std::pair` с выведенными типами. Удобнее, чем явное указание типов.

## Примеры

```cpp
#include <utility>
#include <iostream>

int main()
{
    auto p = std::make_pair(42, "hello");
    std::cout << p.first << " " << p.second << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений (noexcept).

## Похожие функции

- `std::pair` — явное создание пары

## Источники

- https://en.cppreference.com/w/cpp/utility/pair/make_pair
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/pair|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/piecewise_construct|Вперёд]]
