# partial_ordering

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<compare>|<compare>]] / partial_ordering

[[Языки программирования/C++/Библиотеки/<compare>/weak_ordering|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>/strong_equal|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <compare>

struct partial_ordering {
    static const partial_ordering less;
    static const partial_ordering equivalent;
    static const partial_ordering greater;
    static const partial_ordering unordered;
};
```

## Описание

Тип результата трёхстороннего сравнения, определяющий частичный порядок. Может содержать `unordered` для несравнимых значений (например, `NaN`).

## Константы

| Константа | Описание |
|---|---|
| `less` | Меньше |
| `equivalent` | Эквивалентно |
| `greater` | Больше |
| `unordered` | Несравнимо (NaN) |

## Примеры

```cpp
#include <compare>
#include <iostream>

int main()
{
    double a = 1.0, b = std::numeric_limits<double>::quiet_NaN();

    auto result = a <=> b;
    if (result == std::partial_ordering::unordered)
        std::cout << "Несравнимо (NaN)" << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<compare>/strong_ordering|strong_ordering]] — строгий порядок

## Источники

- https://en.cppreference.com/w/cpp/utility/compare/partial_ordering
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<compare>/weak_ordering|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>/strong_equal|Вперёд]]
