# move_initializable

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / move_initializable

[[Языки программирования/C++/Библиотеки/<concepts>/copy_initializable|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/equality_comparable|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class T>
concept move_initializable =
    std::constructible_from<T, T> &&
    std::assignable_from<T&, T>;
```

## Описание

Концепт, проверяющий, что объект типа `T` может быть инициализирован перемещением.

## Примеры

```cpp
#include <concepts>
#include <memory>

template<std::move_initializable T>
T move_value(T&& val) {
    return std::move(val);
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/copy_initializable|copy_initializable]] — копируемая инициализация

## Источники

- https://en.cppreference.com/w/cpp/concepts/move_initializable
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/copy_initializable|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/equality_comparable|Вперёд]]
