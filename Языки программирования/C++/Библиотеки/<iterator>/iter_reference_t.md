# iter_reference_t

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / iter_reference_t

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iter_difference_t|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iterator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template</* dereferenceable */ T>
using iter_reference_t = decltype(*declval<T&>());
```

## Параметры

| Параметр | Описание |
|---|---|
| `T` | тип итератора |

## Возвращаемое значение

Алиас-шаблон `iter_reference_t` определяет тип, возвращаемый при разыменовании итератора `T`.

## Что делает

Алиас-шаблон `iter_reference_t` определяет тип, возвращаемый при разыменовании итератора `T`.

## Примеры

### Базовое использование

```cpp
static_assert(std::is_same_v<std::iter_reference_t<int*>, int&>);
```

## Исключения

- **Исключения:** Алиас-шаблон, не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iter_difference_t|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iterator|Вперёд]]
