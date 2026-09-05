# disjunction

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<type_traits>|<type_traits>]] / disjunction

[[Языки программирования/C++/Библиотеки/<type_traits>/conjunction|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/negation|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <type_traits>
template<class... B>
struct disjunction;
```

## Возвращаемое значение

`std::true_type` если хотя бы один true.

## Что делает

Логическое ИЛИ метатипов.

## Примеры

### Базовое использование

```cpp
static_assert(std::disjunction_v<std::is_integral<double>, std::is_floating_point<double>>);
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/type_traits
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<type_traits>/conjunction|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/negation|Вперёд]]
