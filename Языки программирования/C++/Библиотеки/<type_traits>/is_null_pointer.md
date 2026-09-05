# is_null_pointer

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<type_traits>|<type_traits>]] / is_null_pointer

[[Языки программирования/C++/Библиотеки/<type_traits>/is_void|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/is_bounded_array|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <type_traits>
template<class T>
struct is_null_pointer;
```

## Возвращаемое значение

`std::true_type` если nullptr_t.

## Что делает

Проверка nullptr.

## Примеры

### Базовое использование

```cpp
static_assert(std::is_null_pointer_v<std::nullptr_t>);
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/type_traits
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<type_traits>/is_void|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/is_bounded_array|Вперёд]]
