# remove_volatile

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<type_traits>|<type_traits>]] / remove_volatile

[[Языки программирования/C++/Библиотеки/<type_traits>/remove_const|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/remove_cv|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <type_traits>
template<class T>
struct remove_volatile;
```

## Возвращаемое значение

Тип без volatile.

## Что делает

Удаление volatile.

## Примеры

### Базовое использование

```cpp
using T = std::remove_volatile_t<volatile int>; // int
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/type_traits
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<type_traits>/remove_const|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/remove_cv|Вперёд]]
