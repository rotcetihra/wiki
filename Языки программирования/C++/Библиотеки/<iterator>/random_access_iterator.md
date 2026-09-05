# random_access_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / random_access_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/bidirectional_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/contiguous_iterator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<class I>
concept random_access_iterator = /* see description */;
```

## Параметры

| Параметр | Описание |
|---|---|
| `I` | проверяемый тип итератора |

## Возвращаемое значение

Концепт `random_access_iterator` определяет требования к итератору произвольного доступа.

## Что делает

Концепт `random_access_iterator` определяет требования к итератору произвольного доступа. Поддерживает перемещение на любое количество элементов за O(1) и индексацию `it[n]`.

## Примеры

### Базовое использование

```cpp
std::vector<int> v = {10, 20, 30, 40, 50};
auto it = v.begin();
it += 3;
std::cout << *it << std::endl; // 40
std::cout << (v.end() - v.begin()) << std::endl; // 5
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Не модифицирует состояние (если не указано иное).')

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/bidirectional_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/contiguous_iterator|Вперёд]]
