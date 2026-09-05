# conjunction

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<type_traits>|<type_traits>]] / conjunction

[[Языки программирования/C++/Библиотеки/<type_traits>/invoke_result|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/disjunction|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <type_traits>
template<class... B>
struct conjunction;
```

## Возвращаемое значение

`std::true_type` если все true.

## Что делает

Логическое И метатипов.

## Примеры

### Базовое использование

```cpp
static_assert(std::conjunction_v<std::is_integral<int>, std::is_signed<int>>);
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/type_traits
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<type_traits>/invoke_result|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/disjunction|Вперёд]]
