# back_insert_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / back_insert_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/front_insert_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/insert_iterator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<class Container>
class back_insert_iterator;
```

## Параметры

| Параметр | Описание |
|---|---|
| `Container` | тип контейнера |

## Возвращаемое значение

Адаптер итератора, вставляющий элементы в конец контейнера через `push_back`.

## Что делает

Адаптер итератора, вставляющий элементы в конец контейнера через `push_back`. Создаётся `std::back_inserter()`.

## Примеры

### Базовое использование

```cpp
std::vector<int> v;
auto it = std::back_inserter(v);
*it = 10; // v = {10}
*it = 20; // v = {10, 20}
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/front_insert_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/insert_iterator|Вперёд]]
