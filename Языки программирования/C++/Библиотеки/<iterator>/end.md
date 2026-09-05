# end

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / end

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/empty|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/begin|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<class Container>
constexpr auto end(Container& c) -> decltype(c.end());
template<class T, size_t N>
constexpr T* end(T (&array)[N]);
```

## Параметры

| Параметр | Описание |
|---|---|
| `c` | контейнер |
| `array` | массив |

## Возвращаемое значение

Возвращает итератор на элемент после последнего (past-the-end).

## Что делает

Возвращает итератор на элемент после последнего (past-the-end).

## Примеры

### Базовое использование

```cpp
std::vector<int> v = {10, 20, 30};
auto it = std::end(v);
--it;
std::cout << *it << std::endl; // 30
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/empty|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/begin|Вперёд]]
