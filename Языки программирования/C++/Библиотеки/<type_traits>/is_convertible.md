# is_convertible

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<type_traits>|<type_traits>]] / is_convertible

[[Языки программирования/C++/Библиотеки/<type_traits>/underlying_type|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/is_nothrow_constructible|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <type_traits>
template<class From, class To>
struct is_convertible;
```

## Возвращаемое значение

`std::true_type` если преобразование возможно.

## Что делает

Проверка неявного преобразования.

## Примеры

### Базовое использование

```cpp
static_assert(std::is_convertible_v<int, double>);
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/type_traits
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<type_traits>/underlying_type|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/is_nothrow_constructible|Вперёд]]
