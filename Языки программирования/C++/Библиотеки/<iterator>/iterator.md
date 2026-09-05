# iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<iterator>|<iterator>]] / iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iterator_traits|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/next|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iterator>
template<class Category, class T, class Distance = ptrdiff_t,
         class Pointer = T*, class Reference = T&>
struct iterator;
```

## Параметры

| Параметр | Описание |
|---|---|
| `Category` | категория итератора |
| `T` | тип значения |
| `Distance` | тип разницы |
| `Pointer` | тип указателя |
| `Reference` | тип ссылки |

## Возвращаемое значение

Базовый класс `std::iterator` **устарел в C++17**.

## Что делает

Базовый класс `std::iterator` **устарел в C++17**. Определяет типы для простых итераторов. Рекомендуется определять типы самостоятельно.

## Примеры

### Базовое использование

```cpp
// Устаревший способ (не рекомендуется):
struct MyIter : std::iterator<std::input_iterator_tag, int> {
    int* p;
    MyIter(int* x) : p(x) {}
    int& operator*() { return *p; }
    MyIter& operator++() { ++p; return *this; }
    bool operator!=(const MyIter& o) const { return p != o.p; }
};
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/iterator
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/iterator_traits|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/next|Вперёд]]
