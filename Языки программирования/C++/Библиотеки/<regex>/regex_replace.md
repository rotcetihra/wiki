# regex_replace

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<regex>|<regex>]] / regex_replace

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_match|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_search|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <regex>
template<class OutputIt, class BiIt, class Traits, class CharT, class ST, class SA>
OutputIt regex_replace(OutputIt out, BiIt first, BiIt last,
                       const basic_regex<CharT, Traits>& e,
                       const basic_string<CharT, ST, SA>& fmt,
                       regex_constants::match_flag_type flags = regex_constants::match_default);
```

## Параметры

| Параметр | Описание |
|---|---|
| `out` | выходной итератор |
| `first` | начало |
| `last` | конец |
| `e` | regex |
| `fmt` | строка замены |

## Возвращаемое значение

Итератор после последнего записанного символа.

## Что делает

Заменяет все совпадения regex на строку `fmt`. Поддерживает `$1`, `$2` для групп.

## Примеры

### Базовое использование

```cpp
std::string s = "Hello 123 World 456";
std::regex re("\\d+");
std::string result = std::regex_replace(s, re, "NUM");
std::cout << result << std::endl;
// Hello NUM World NUM
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/regex
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_match|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_search|Вперёд]]
