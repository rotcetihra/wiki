# unsigned_integral

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / unsigned_integral

[[Языки программирования/C++/Библиотеки/<concepts>/signed_integral|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/assignable_from|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class T>
concept unsigned_integral = std::integral<T> && std::is_unsigned_v<T>;
```

## Описание

Концепт, ограничивающий беззнаковым целочисленным типом (`unsigned int`, `unsigned long` и т.д.).

## Примеры

```cpp
#include <concepts>
#include <iostream>

template<std::unsigned_integral T>
T absolute_diff(T a, T b) {
    return a > b ? a - b : b - a;
}

int main() {
    std::cout << absolute_diff(3u, 7u) << std::endl; // 4
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/signed_integral|signed_integral]] — знаковые типы

## Источники

- https://en.cppreference.com/w/cpp/concepts/unsigned_integral
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/signed_integral|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/assignable_from|Вперёд]]
