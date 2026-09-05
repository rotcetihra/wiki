# regex_constants

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<regex>|<regex>]] / regex_constants

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_error|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/basic_regex|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <regex>
namespace regex_constants {
    using syntax_option_type = /* T1 */;
    using match_flag_type = /* T2 */;
    using error_type = /* T3 */;
}
```

## Параметры

| Параметр | Описание |
|---|---|


## Возвращаемое значение

Пространство имён с константами.

## Что делает

Содержит константы: опции синтаксиса (ECMAScript, basic, extended, icase, nosubs, optimize, multiline), флаги сопоставления, коды ошибок.

## Примеры

### Базовое использование

```cpp
std::regex re("test", std::regex_constants::ECMAScript);
std::regex re2("test", std::regex_constants::icase);
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/regex
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_error|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/basic_regex|Вперёд]]
