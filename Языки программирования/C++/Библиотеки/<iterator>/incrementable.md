# incrementable

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / incrementable

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/weakly_incrementable|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/input_or_output_iterator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<class I>
concept incrementable = /* see description */;
```

## Параметры

| Параметр | Описание |
|---|---|
| `I` | проверяемый тип |

## Возвращаемое значение

Концепт `incrementable` — усиленная версия `weakly_incrementable`.

## Что делает

Концепт `incrementable` — усиленная версия `weakly_incrementable`. Требует `equality_comparable` и сохранение равенства при инкрементации.

## Примеры

### Базовое использование

```cpp
static_assert(std::incrementable<int*>);
static_assert(std::incrementable<std::vector<int>::iterator>);
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Не модифицирует состояние (если не указано иное).')

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/weakly_incrementable|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/input_or_output_iterator|Вперёд]]
