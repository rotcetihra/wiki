# disable_sized_sentinel_for

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / disable_sized_sentinel_for

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/sized_sentinel_for|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iter_value_t|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<class S, class I>
inline constexpr bool disable_sized_sentinel_for = false;
```

## Параметры

| Параметр | Описание |
|---|---|
| `S` | тип сигнала |
| `I` | тип итератора |

## Возвращаемое значение

Шаблонная переменная `disable_sized_sentinel_for` позволяет отключить `sized_sentinel_for` для типа `S` и итератора `I`.

## Что делает

Шаблонная переменная `disable_sized_sentinel_for` позволяет отключить `sized_sentinel_for` для типа `S` и итератора `I`.

## Примеры

### Базовое использование

```cpp
static_assert(!std::disable_sized_sentinel_for<int*, int*>);
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/sized_sentinel_for|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iter_value_t|Вперёд]]
