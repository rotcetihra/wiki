# operator+

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string>|<string>]] / operator+

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/basic_string|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/operator==|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string>
template<class CharT, class Traits, class Allocator>
constexpr basic_string<CharT, Traits, Allocator> operator+(
    const basic_string<CharT, Traits, Allocator>& lhs,
    const basic_string<CharT, Traits, Allocator>& rhs);
```

## Параметры

| Параметр | Описание |
|---|---|
| `lhs` | левая строка |
| `rhs` | правая строка |

## Возвращаемое значение

Новая строка — результат конкатенации.

## Что делает

Конкатенирует две строки. Поддерживает семантику перемещения.

## Примеры

### Базовое использование

```cpp
std::string a = "Hello";
std::string b = " World";
std::string c = a + b;
std::cout << c << std::endl; // Hello World
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Потокобезопасна для разных объектов.')

## Источники

- https://en.cppreference.com/w/cpp/header/string
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/basic_string|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/operator==|Вперёд]]
