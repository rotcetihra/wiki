# swappable

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / swappable

[[Языки программирования/C++/Библиотеки/<concepts>/assignable_from|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/destructible|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class T>
concept swappable = requires(T& a, T& b) {
    std::ranges::swap(a, b);
};
```

## Описание

Концепт, проверяющий, что значения типа `T` можно обменять через `std::ranges::swap`.

## Примеры

```cpp
#include <concepts>
#include <iostream>

template<std::swappable T>
void swap_values(T& a, T& b) {
    std::ranges::swap(a, b);
}

int main() {
    int x = 1, y = 2;
    swap_values(x, y);
    std::cout << x << " " << y << std::endl; // 2 1
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/assignable_from|assignable_from]] — присваиваемость

## Источники

- https://en.cppreference.com/w/cpp/concepts/swappable
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/assignable_from|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/destructible|Вперёд]]
