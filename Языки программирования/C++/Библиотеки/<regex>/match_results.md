# match_results

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<regex>|<regex>]] / match_results

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_token_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_replace|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <regex>
template<class BiIt, class Allocator = allocator<sub_match<BiIt>>>
class match_results;
using smatch = match_results<string::const_iterator>;
```

## Параметры

| Параметр | Описание |
|---|---|
| `BiIt` | итератор |
| `Allocator` | аллокатор |

## Возвращаемое значение

Объект `match_results` с результатами сопоставления.

## Что делает

Хранит результаты сопоставления regex с текстом. Содержит совпадения, позиции, приставку и суффикс.

## Примеры

### Базовое использование

```cpp
std::string s = "Hello 123 World 456";
std::regex re("(\\d+)(\\D+)(\\d+)");
std::smatch m;
if (std::regex_search(s, m, re)) {
    std::cout << "Full: " << m[0] << std::endl;
    std::cout << "Group 1: " << m[1] << std::endl;
}
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/regex
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_token_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_replace|Вперёд]]
