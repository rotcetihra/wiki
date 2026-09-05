# sized_sentinel_for

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / sized_sentinel_for

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/input_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<class S, class I>
concept sized_sentinel_for = /* see description */;
```

## Параметры

| Параметр | Описание |
|---|---|
| `S` | тип сигнала |
| `I` | тип итератора |

## Возвращаемое значение

Концепт `sized_sentinel_for<S, I>` определяет, что расстояние `s - i` вычисляется за O(1).

## Что делает

Концепт `sized_sentinel_for<S, I>` определяет, что расстояние `s - i` вычисляется за O(1).

## Примеры

### Базовое использование

```cpp
static_assert(std::sized_sentinel_for<int*, int*>);
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Не модифицирует состояние (если не указано иное).')

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/input_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]]
