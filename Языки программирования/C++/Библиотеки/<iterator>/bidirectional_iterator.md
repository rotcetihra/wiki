# bidirectional_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / bidirectional_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/forward_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/random_access_iterator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<class I>
concept bidirectional_iterator = /* see description */;
```

## Параметры

| Параметр | Описание |
|---|---|
| `I` | проверяемый тип итератора |

## Возвращаемое значение

Концепт `bidirectional_iterator` определяет требования к двунаправленному итератору.

## Что делает

Концепт `bidirectional_iterator` определяет требования к двунаправленному итератору. Поддерживает движение вперёд (`++`) и назад (`--`).

## Примеры

### Базовое использование

```cpp
std::list<int> lst = {1, 2, 3};
auto it = lst.begin();
++it;
--it;
std::cout << *it << std::endl; // 1
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Не модифицирует состояние (если не указано иное).')

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/forward_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/random_access_iterator|Вперёд]]
