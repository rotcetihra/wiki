# equality_comparable

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / equality_comparable

[[Языки программирования/C++/Библиотеки/<concepts>/move_initializable|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/totally_ordered|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class T>
concept equality_comparable = requires(const std::remove_reference_t<T>& a,
                                       const std::remove_reference_t<T>& b) {
    { a == b } -> std::convertible_to<bool>;
    { a != b } -> std::convertible_to<bool>;
};
```

## Описание

Концепт, проверяющий, что значения типа `T` можно сравнивать на равенство/неравенство.

## Примеры

```cpp
#include <concepts>
#include <iostream>

template<std::equality_comparable T>
bool are_equal(const T& a, const T& b) {
    return a == b;
}

int main() {
    std::cout << are_equal(42, 42) << std::endl; // 1
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/totally_ordered|totally_ordered]] — полный порядок

## Источники

- https://en.cppreference.com/w/cpp/concepts/equality_comparable
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/move_initializable|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/totally_ordered|Вперёд]]
