# getline

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string>|<string>]] / getline

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/operator>=|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stof|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string>
template<class CharT, class Traits, class Allocator>
basic_istream<CharT, Traits>& getline(
    basic_istream<CharT, Traits>& is,
    basic_string<CharT, Traits, Allocator>& str,
    CharT delim);
```

## Параметры

| Параметр | Описание |
|---|---|
| `is` | входной поток |
| `str` | строка |
| `delim` | разделитель |

## Возвращаемое значение

Ссылка на поток `is`.

## Что делает

Читает из потока в строку до разделителя `delim` (по умолчанию `\n`).

## Примеры

### Базовое использование

```cpp
std::string line;
std::getline(std::cin, line);
std::cout << "You entered: " << line << std::endl;
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Потокобезопасна для разных объектов.')

## Источники

- https://en.cppreference.com/w/cpp/header/string
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/operator>=|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stof|Вперёд]]
