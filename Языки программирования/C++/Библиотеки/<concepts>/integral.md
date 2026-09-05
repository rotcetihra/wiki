# integral

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / integral

[[Языки программирования/C++/Библиотеки/<concepts>/convertible_to|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/floating_point|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class T>
concept integral = std::is_integral_v<T>;
```

## Описание

Концепт, ограничивающий тип целочисленным (`bool`, `char`, `int`, `long` и т.д.).

## Примеры

```cpp
#include <concepts>
#include <iostream>

template<std::integral T>
T add(T a, T b) {
    return a + b;
}

int main() {
    std::cout << add(3, 4) << std::endl; // 7
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/floating_point|floating_point]] — типы с плавающей точкой

## Источники

- https://en.cppreference.com/w/cpp/concepts/integral
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/convertible_to|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/floating_point|Вперёд]]
