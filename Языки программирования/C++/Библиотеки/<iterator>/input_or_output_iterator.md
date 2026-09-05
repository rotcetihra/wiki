# input_or_output_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / input_or_output_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/sized_sentinel_for|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/input_iterator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<class I>
concept input_or_output_iterator = /* see description */;
```

## Параметры

| Параметр | Описание |
|---|---|
| `I` | проверяемый тип итератора |

## Возвращаемое значение

Концепт `input_or_output_iterator` определяет минимальные требования к итератору: разыменование `*i` и инкремент `++i`.

## Что делает

Концепт `input_or_output_iterator` определяет минимальные требования к итератору: разыменование `*i` и инкремент `++i`.

## Примеры

### Базовое использование

```cpp
static_assert(std::input_or_output_iterator<int*>);
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Не модифицирует состояние (если не указано иное).')

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/sized_sentinel_for|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/input_iterator|Вперёд]]
