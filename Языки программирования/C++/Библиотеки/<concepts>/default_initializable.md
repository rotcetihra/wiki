# default_initializable

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / default_initializable

[[Языки программирования/C++/Библиотеки/<concepts>/constructible_from|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/copy_initializable|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class T>
concept default_initializable =
    std::constructible_from<T> &&
    requires { T(); } &&
    requires { ::new T(); };
```

## Описание

Концепт, проверяющий, что объект типа `T` может быть инициализирован по умолчанию.

## Примеры

```cpp
#include <concepts>

struct DefaultInit {
    int x = 42;
};

template<std::default_initializable T>
T create() {
    return T();
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/constructible_from|constructible_from]] — конструируемость

## Источники

- https://en.cppreference.com/w/cpp/concepts/default_initializable
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/constructible_from|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/copy_initializable|Вперёд]]
