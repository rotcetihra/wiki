# totally_ordered

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / totally_ordered

[[Языки программирования/C++/Библиотеки/<concepts>/equality_comparable|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class T>
concept totally_ordered =
    std::equality_comparable<T> &&
    requires(const std::remove_reference_t<T>& a,
             const std::remove_reference_t<T>& b) {
        { a < b }  -> std::convertible_to<bool>;
        { a > b }  -> std::convertible_to<bool>;
        { a <= b } -> std::convertible_to<bool>;
        { a >= b } -> std::convertible_to<bool>;
    };
```

## Описание

Концепт, проверяющий, что значения типа `T` поддерживают полный порядок (сравнение `<`, `>`, `<=`, `>=`).

## Примеры

```cpp
#include <concepts>
#include <iostream>

template<std::totally_ordered T>
T max_val(const T& a, const T& b) {
    return a > b ? a : b;
}

int main() {
    std::cout << max_val(3, 5) << std::endl; // 5
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/equality_comparable|equality_comparable]] — равенство

## Источники

- https://en.cppreference.com/w/cpp/concepts/totally_ordered
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/equality_comparable|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки|Вперёд]]
