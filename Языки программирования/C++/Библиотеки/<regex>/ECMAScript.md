# ECMAScript

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<regex>|<regex>]] / ECMAScript

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_constants|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_replace|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <regex>
inline constexpr regex_constants::syntax_option_type ECMAScript = /* unspecified */;
```

## Параметры

| Параметр | Описание |
|---|---|


## Возвращаемое значение

Константа типа `syntax_option_type`.

## Что делает

Задаёт синтаксис ECMAScript (JavaScript) по умолчанию для `basic_regex`.

## Примеры

### Базовое использование

```cpp
std::regex re("^\\d{3}-\\d{2}-\\d{4}$", std::regex::ECMAScript);
std::string ssn = "123-45-6789";
std::cout << std::boolalpha << std::regex_match(ssn, re) << std::endl; // true
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/regex
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_constants|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_replace|Вперёд]]
