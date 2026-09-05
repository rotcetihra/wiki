# operator>

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string>|<string>]] / operator>

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/operator>=|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stoi|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string>
template<class CharT, class Traits, class Allocator>
constexpr /* see description */ operator>(
    const basic_string<CharT, Traits, Allocator>& lhs,
    const basic_string<CharT, Traits, Allocator>& rhs);
```

## Параметры

| Параметр | Описание |
|---|---|
| `lhs` | левая строка |
| `rhs` | правая строка |

## Возвращаемое значение

`true`, если `lhs` лексикографически больше `rhs`.

## Что делает

Лексикографическое сравнение.

## Примеры

### Базовое использование

```cpp
std::string a = "banana";
std::string b = "apple";
std::cout << std::boolalpha << (a > b) << std::endl; // true
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Потокобезопасна для разных объектов.')

## Источники

- https://en.cppreference.com/w/cpp/header/string
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/operator>=|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stoi|Вперёд]]
