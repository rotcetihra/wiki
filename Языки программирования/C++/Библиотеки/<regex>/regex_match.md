# regex_match

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<regex>|<regex>]] / regex_match

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_search|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_token_iterator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <regex>
template<class BiIt, class Allocator, class CharT, class Traits>
bool regex_match(BiIt first, BiIt last,
                 match_results<BiIt, Allocator>& m,
                 const basic_regex<CharT, Traits>& e,
                 regex_constants::match_flag_type flags = regex_constants::match_default);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first` | начало |
| `last` | конец |
| `m` | результаты |
| `e` | regex |

## Возвращаемое значение

`true`, если весь диапазон соответствует выражению.

## Что делает

Проверяет полное сопоставление диапазона с regex (в отличие от `regex_search`).

## Примеры

### Базовое использование

```cpp
std::string s = "12345";
std::regex re("\\d+");
if (std::regex_match(s, re))
    std::cout << "Full match!" << std::endl;
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/regex
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_search|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_token_iterator|Вперёд]]
