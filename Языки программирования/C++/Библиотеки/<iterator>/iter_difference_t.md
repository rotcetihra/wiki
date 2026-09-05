# iter_difference_t

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / iter_difference_t

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iter_value_t|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iter_reference_t|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<weakly_incrementable I>
using iter_difference_t = incrementable_traits<I>::difference_type;
```

## Параметры

| Параметр | Описание |
|---|---|
| `I` | тип итератора |

## Возвращаемое значение

Алиас-шаблон `iter_difference_t` определяет тип разницы для итератора `I`.

## Что делает

Алиас-шаблон `iter_difference_t` определяет тип разницы для итератора `I`.

## Примеры

### Базовое использование

```cpp
static_assert(std::is_same_v<std::iter_difference_t<int*>, std::ptrdiff_t>);
```

## Исключения

- **Исключения:** Алиас-шаблон, не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iter_value_t|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iter_reference_t|Вперёд]]
