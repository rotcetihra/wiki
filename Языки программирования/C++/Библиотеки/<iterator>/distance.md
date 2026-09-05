# distance

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / distance

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/end|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/advance|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<class InputIt>
typename std::iterator_traits<InputIt>::difference_type
    distance(InputIt first, InputIt last);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first` | начальный итератор |
| `last` | конечный итератор |

## Возвращаемое значение

Возвращает расстояние от `first` до `last`.

## Что делает

Возвращает расстояние от `first` до `last`. Для итераторов произвольного доступа — O(1), для остальных — O(n).

## Примеры

### Базовое использование

```cpp
std::vector<int> v = {10, 20, 30, 40, 50};
auto d = std::distance(v.begin(), v.end());
std::cout << d << std::endl; // 5
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/end|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/advance|Вперёд]]
