# iterator_traits

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / iterator_traits

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/insert_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/reverse_iterator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<class Iter>
struct iterator_traits;
```

## Параметры

| Параметр | Описание |
|---|---|
| `Iter` | тип итератора |

## Возвращаемое значение

Шаблон `iterator_traits` определяет свойства итератора: тип значения, категорию, разницу, указатель, ссылку.

## Что делает

Шаблон `iterator_traits` определяет свойства итератора: тип значения, категорию, разницу, указатель, ссылку.

## Примеры

### Базовое использование

```cpp
using Traits = std::iterator_traits<std::vector<int>::iterator>;
static_assert(std::is_same_v<Traits::iterator_category, std::random_access_iterator_tag>);
static_assert(std::is_same_v<Traits::value_type, int>);
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Не модифицирует состояние (если не указано иное).')

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/insert_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/reverse_iterator|Вперёд]]
