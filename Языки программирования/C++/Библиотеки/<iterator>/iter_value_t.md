# iter_value_t

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / iter_value_t

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iter_reference_t|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iter_difference_t|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<indirectly_readable T>
using iter_value_t = /* see description */;
```

## Параметры

| Параметр | Описание |
|---|---|
| `T` | тип итератора |

## Возвращаемое значение

Алиас-шаблон `iter_value_t` определяет тип значения итератора.

## Что делает

Алиас-шаблон `iter_value_t` определяет тип значения итератора. Краткая запись вместо `iterator_traits<T>::value_type`.

## Примеры

### Базовое использование

```cpp
static_assert(std::is_same_v<std::iter_value_t<int*>, int>);
static_assert(std::is_same_v<std::iter_value_t<std::vector<int>::iterator>, int>);
```

## Исключения

- **Исключения:** Алиас-шаблон, не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iter_reference_t|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iter_difference_t|Вперёд]]
