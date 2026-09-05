# destructible

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / destructible

[[Языки программирования/C++/Библиотеки/<concepts>/swappable|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/constructible_from|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class T>
concept destructible = std::is_nothrow_destructible_v<T>;
```

## Описание

Концепт, проверяющий, что объекты типа `T` можно уничтожить без исключений.

## Примеры

```cpp
#include <concepts>
#include <memory>

template<std::destructible T>
void destroy(T* ptr) {
    ptr->~T();
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/constructible_from|constructible_from]] — конструируемость

## Источники

- https://en.cppreference.com/w/cpp/concepts/destructible
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/swappable|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/constructible_from|Вперёд]]
