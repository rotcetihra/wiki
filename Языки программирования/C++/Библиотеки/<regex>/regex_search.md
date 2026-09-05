# regex_search

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<regex>|<regex>]] / regex_search

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_match|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_replace|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <regex>
template<class BiIt, class Allocator, class CharT, class Traits>
bool regex_search(BiIt first, BiIt last,
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

`true`, если совпадение найдено.

## Что делает

Ищет первое совпадение regex в диапазоне.

## Примеры

### Базовое использование

```cpp
std::string s = "The price is 42 dollars";
std::regex re("\\d+");
std::smatch m;
if (std::regex_search(s, m, re))
    std::cout << "Found: " << m[0] << std::endl; // 42
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/regex
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_match|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_replace|Вперёд]]
