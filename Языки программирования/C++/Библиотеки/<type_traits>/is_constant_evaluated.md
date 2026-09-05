# is_constant_evaluated

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<type_traits>|<type_traits>]] / is_constant_evaluated

[[Языки программирования/C++/Библиотеки/<type_traits>/negation|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <type_traits>
constexpr bool is_constant_evaluated() noexcept;
```

## Возвращаемое значение

`bool` — true если constexpr контекст.

## Что делает

Проверка constexpr контекста (C++20).

## Примеры

### Базовое использование

```cpp
if constexpr (std::is_constant_evaluated()) {
    // constexpr контекст
}
```

## Исключения

- **Исключения:** Не бросает исключений (`noexcept`).
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/type_traits
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<type_traits>/negation|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
