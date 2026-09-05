# floating_point

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / floating_point

[[Языки программирования/C++/Библиотеки/<concepts>/integral|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/signed_integral|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class T>
concept floating_point = std::is_floating_point_v<T>;
```

## Описание

Концепт, ограничивающий тип числом с плавающей точкой (`float`, `double`, `long double`).

## Примеры

```cpp
#include <concepts>
#include <iostream>

template<std::floating_point T>
T square(T x) {
    return x * x;
}

int main() {
    std::cout << square(3.14) << std::endl; // 9.8596
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/integral|integral]] — целочисленные типы

## Источники

- https://en.cppreference.com/w/cpp/concepts/floating_point
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/integral|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/signed_integral|Вперёд]]
