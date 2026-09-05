# size

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / size

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/distance|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/begin|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<class Container>
constexpr auto size(const Container& c) -> decltype(c.size());
template<class T, size_t N>
constexpr size_t size(const T (&array)[N]);
```

## Параметры

| Параметр | Описание |
|---|---|
| `c` | контейнер |
| `array` | массив |

## Возвращаемое значение

Возвращает количество элементов в контейнере или массиве.

## Что делает

Возвращает количество элементов в контейнере или массиве.

## Примеры

### Базовое использование

```cpp
std::vector<int> v = {10, 20, 30};
std::cout << std::size(v) << std::endl; // 3
int arr[] = {1, 2, 3, 4, 5};
std::cout << std::size(arr) << std::endl; // 5
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/distance|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/begin|Вперёд]]
