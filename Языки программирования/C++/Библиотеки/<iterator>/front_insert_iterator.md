# front_insert_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / front_insert_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/insert_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/advance|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<class Container>
class front_insert_iterator;
```

## Параметры

| Параметр | Описание |
|---|---|
| `Container` | тип контейнера |

## Возвращаемое значение

Адаптер итератора, вставляющий элементы в начало контейнера через `push_front`.

## Что делает

Адаптер итератора, вставляющий элементы в начало контейнера через `push_front`. Создаётся `std::front_inserter()`.

## Примеры

### Базовое использование

```cpp
std::deque<int> d;
auto it = std::front_inserter(d);
*it = 10; // d = {10}
*it = 20; // d = {20, 10}
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/insert_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/advance|Вперёд]]
