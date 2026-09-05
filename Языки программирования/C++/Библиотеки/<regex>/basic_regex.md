# basic_regex

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<regex>|<regex>]] / basic_regex

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_traits|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/sub_match|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <regex>
template<class CharT, class Traits = regex_traits<CharT>>
class basic_regex;
using regex = basic_regex<char>;
using wregex = basic_regex<wchar_t>;
```

## Параметры

| Параметр | Описание |
|---|---|
| `CharT` | тип символа |
| `Traits` | класс свойств |

## Возвращаемое значение

Объект `basic_regex` со скомпилированным паттерном.

## Что делает

Класс `std::basic_regex` представляет скомпилированное регулярное выражение. Поддерживает ECMAScript, POSIX, awk, grep, egrep.

## Примеры

### Базовое использование

```cpp
std::regex re("\\d+", std::regex::ECMAScript);
std::string s = "hello 123 world 456";
std::smatch m;
if (std::regex_search(s, m, re))
    std::cout << m[0] << std::endl; // 123
```

## Исключения

- **Исключения:** Бросает `std::regex_error` при ошибке компиляции.

## Источники

- https://en.cppreference.com/w/cpp/header/regex
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_traits|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/sub_match|Вперёд]]
