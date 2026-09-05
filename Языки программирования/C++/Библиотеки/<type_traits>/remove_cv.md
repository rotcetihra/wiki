# remove_cv

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<type_traits>|<type_traits>]] / remove_cv

[[Языки программирования/C++/Библиотеки/<type_traits>/remove_volatile|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/remove_reference|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <type_traits>
template<class T>
struct remove_cv;
```

## Возвращаемое значение

Тип без const и volatile.

## Что делает

Удаление cv.

## Примеры

### Базовое использование

```cpp
using T = std::remove_cv_t<const volatile int>; // int
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/type_traits
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<type_traits>/remove_volatile|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/remove_reference|Вперёд]]
