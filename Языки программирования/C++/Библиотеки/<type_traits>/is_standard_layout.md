# is_standard_layout

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<type_traits>|<type_traits>]] / is_standard_layout

[[Языки программирования/C++/Библиотеки/<type_traits>/is_trivially_copyable|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/is_pod|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <type_traits>
template<class T>
struct is_standard_layout;
```

## Возвращаемое значение

`std::true_type` если standard layout.

## Что делает

Проверка стандартного расположения.

## Примеры

### Базовое использование

```cpp
static_assert(std::is_standard_layout_v<int>);
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/type_traits
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<type_traits>/is_trivially_copyable|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<type_traits>/is_pod|Вперёд]]
