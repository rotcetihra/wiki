# weak_ordering

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<compare>|<compare>]] / weak_ordering

[[Языки программирования/C++/Библиотеки/<compare>/strong_ordering|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>/partial_ordering|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <compare>

struct weak_ordering {
    static const weak_ordering less;
    static const weak_ordering equivalent;
    static const weak_ordering greater;
};
```

## Описание

Тип результата трёхстороннего сравнения, определяющий слабый порядок. Не определяет различия между `equal` и `equivalent`.

## Константы

| Константа | Описание |
|---|---|
| `less` | Меньше |
| `equivalent` | Эквивалентно |
| `greater` | Больше |

## Примеры

```cpp
#include <compare>
#include <iostream>

struct CaseInsensitive {
    char c;
    std::weak_ordering operator<=>(const CaseInsensitive& other) const {
        return std::tolower(c) <=> std::tolower(other.c);
    }
};

int main()
{
    CaseInsensitive a{'A'}, b{'a'};
    if ((a <=> b) == std::weak_ordering::equivalent)
        std::cout << "Равны без учёта регистра" << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<compare>/strong_ordering|strong_ordering]] — строгий порядок

## Источники

- https://en.cppreference.com/w/cpp/utility/compare/weak_ordering
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<compare>/strong_ordering|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>/partial_ordering|Вперёд]]
