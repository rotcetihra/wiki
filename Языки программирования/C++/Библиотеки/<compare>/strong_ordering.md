# strong_ordering

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<compare>|<compare>]] / strong_ordering

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>/weak_ordering|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <compare>

struct strong_ordering {
    static const strong_ordering less;
    static const strong_ordering equal;
    static const strong_ordering equivalent;
    static const strong_ordering greater;
};
```

## Описание

Тип результата трёхстороннего сравнения, определяющий строгий полный порядок. `less < equal == equivalent < greater`. Позволяет выводить все классические операторы сравнения (`==`, `!=`, `<`, `>`, `<=`, `>=`).

## Константы

| Константа | Значение | Описание |
|---|---|---|
| `less` | -1 | Меньше |
| `equal` | 0 | Равно (по значению) |
| `equivalent` | 0 | Эквивалентно (по порядку) |
| `greater` | 1 | Больше |

## Примеры

```cpp
#include <compare>
#include <iostream>

int main()
{
    auto result = 1 <=> 2;

    if (result == std::strong_ordering::less)
        std::cout << "1 < 2" << std::endl;

    if (result < 0)
        std::cout << "Тоже 1 < 2" << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<compare>/weak_ordering|weak_ordering]] — слабый порядок

## Источники

- https://en.cppreference.com/w/cpp/utility/compare/strong_ordering
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>/weak_ordering|Вперёд]]
