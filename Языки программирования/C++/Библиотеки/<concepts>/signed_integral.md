# signed_integral

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / signed_integral

[[Языки программирования/C++/Библиотеки/<concepts>/floating_point|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/unsigned_integral|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class T>
concept signed_integral = std::integral<T> && std::is_signed_v<T>;
```

## Описание

Концепт, ограничивающий знаковым целочисленным типом (`int`, `long`, `long long` и т.д.).

## Примеры

```cpp
#include <concepts>
#include <iostream>

template<std::signed_integral T>
T negate(T x) {
    return -x;
}

int main() {
    std::cout << negate(5) << std::endl; // -5
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/unsigned_integral|unsigned_integral]] — беззнаковые типы

## Источники

- https://en.cppreference.com/w/cpp/concepts/signed_integral
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/floating_point|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/unsigned_integral|Вперёд]]
