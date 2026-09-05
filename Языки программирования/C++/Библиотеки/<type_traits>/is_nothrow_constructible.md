# is_nothrow_constructible

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<type_traits>|<type_traits>]] / is_nothrow_constructible

[[Языки программирования/C++/Библиотеки/<type_traits>/is_convertible|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/is_trivially_copyable|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <type_traits>
template<class T, class... Args>
struct is_nothrow_constructible;
```

## Возвращаемое значение

`std::true_type` если конструирование не бросает.

## Что делает

Проверка безопасности исключений.

## Примеры

### Базовое использование

```cpp
static_assert(std::is_nothrow_constructible_v<int, int>);
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/type_traits
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<type_traits>/is_convertible|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/is_trivially_copyable|Вперёд]]
