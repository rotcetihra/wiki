# negation

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<type_traits>|<type_traits>]] / negation

[[Языки программирования/C++/Библиотеки/<type_traits>/disjunction|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/is_constant_evaluated|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <type_traits>
template<class B>
struct negation;
```

## Возвращаемое значение

`std::true_type` если B::value == false.

## Что делает

Логическое отрицание метатипа.

## Примеры

### Базовое использование

```cpp
static_assert(std::negation_v<std::is_floating_point<int>>);
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/type_traits
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<type_traits>/disjunction|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/is_constant_evaluated|Вперёд]]
