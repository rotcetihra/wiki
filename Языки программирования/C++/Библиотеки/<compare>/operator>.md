# operator>

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<compare>|<compare>]] / operator>

[[Языки программирования/C++/Библиотеки/<compare>/operator<|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>/operator<=|Вперёд]]

**Дата написания:** 05.09.2026

## Описание

Автоматически выводится из `operator<=>`. Если `(a <=> b) > 0`, то `a > b` — `true`.

## Примеры

```cpp
#include <compare>
#include <iostream>

struct Point {
    int x, y;
    auto operator<=>(const Point&) const = default;
};

int main()
{
    Point a{3, 4}, b{1, 2};
    std::cout << (a > b) << std::endl; // 1
}
```

## Источники

- https://en.cppreference.com/w/cpp/language/operator_comparison
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<compare>/operator<|Назад]] | [[Языки программирования/C++/Библиотеки/<compare>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>/operator<=|Вперёд]]
