# copy_initializable

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / copy_initializable

[[Языки программирования/C++/Библиотеки/<concepts>/default_initializable|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/move_initializable|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class T>
concept copy_initializable =
    std::movable<T> &&
    std::constructible_from<T, T&> &&
    std::constructible_from<T, const T&> &&
    std::constructible_from<T, const T> &&
    std::assignable_from<T&, T&> &&
    std::assignable_from<T&, const T&> &&
    std::assignable_from<T&, const T>;
```

## Описание

Концепт, проверяющий, что объект типа `T` может быть инициализирован копированием.

## Примеры

```cpp
#include <concepts>
#include <vector>

template<std::copy_initializable T>
T copy_value(const T& val) {
    return val;
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/move_initializable|move_initializable]] — перемещаемая инициализация

## Источники

- https://en.cppreference.com/w/cpp/concepts/copy_initializable
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/default_initializable|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/move_initializable|Вперёд]]
