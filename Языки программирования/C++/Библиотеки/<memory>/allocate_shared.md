# allocate_shared

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<memory>|<memory>]] / allocate_shared

[[Языки программирования/C++/Библиотеки/<memory>/make_shared|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<memory>/uninitialized_default_construct|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <memory>
template<class T, class Alloc, class... Args>
shared_ptr<T> allocate_shared(const Alloc& a, Args&&... args);
```

## Параметры

| Параметр | Описание |
|---|---|
| `a` | аллокатор |
| `args` | аргументы конструктора |

## Возвращаемое значение

`std::shared_ptr<T>`.

## Что делает

Аналог make_shared с аллокатором.

## Примеры

### Базовое использование

```cpp
std::allocator<int> alloc;
auto p = std::allocate_shared<int>(alloc, 42);
```

## Исключения

- **Исключения:** `std::bad_alloc`.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/memory
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<memory>/make_shared|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<memory>/uninitialized_default_construct|Вперёд]]
