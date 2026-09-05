# forward_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / forward_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/output_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/bidirectional_iterator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<class I>
concept forward_iterator = /* see description */;
```

## Параметры

| Параметр | Описание |
|---|---|
| `I` | проверяемый тип итератора |

## Возвращаемое значение

Концепт `forward_iterator` определяет требования к прямому итератору.

## Что делает

Концепт `forward_iterator` определяет требования к прямому итератору. Поддерживает многопроходное чтение и сравнение на равенство.

## Примеры

### Базовое использование

```cpp
std::forward_list<int> fl = {1, 2, 3};
auto it = fl.begin();
std::cout << *it << ' ' << *it << std::endl; // 1 1
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Не модифицирует состояние (если не указано иное).')

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/output_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/bidirectional_iterator|Вперёд]]
