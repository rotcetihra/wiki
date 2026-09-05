# is_nothrow_invocable

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<type_traits>|<type_traits>]] / is_nothrow_invocable

[[Языки программирования/C++/Библиотеки/<type_traits>/is_invocable|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/invoke_result|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <type_traits>
template<class F, class... ArgTypes>
struct is_nothrow_invocable;
```

## Возвращаемое значение

`std::true_type` если вызов не бросает.

## Что делает

Проверка безопасности исключений (C++17).

## Примеры

### Базовое использование

```cpp
static_assert(std::is_nothrow_invocable_v<int(*)(int), int>);
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/type_traits
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<type_traits>/is_invocable|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/invoke_result|Вперёд]]
