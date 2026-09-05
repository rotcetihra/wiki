# regex_token_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<regex>|<regex>]] / regex_token_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_match|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_iterator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <regex>
template<class BiIt, class CharT = typename iterator_traits<BiIt>::value_type,
          class Traits = regex_traits<CharT>>
class regex_token_iterator;
using sregex_token_iterator = regex_token_iterator<string::const_iterator>;
```

## Параметры

| Параметр | Описание |
|---|---|
| `BiIt` | итератор |
| `CharT` | тип символа |
| `Traits` | свойства |

## Возвращаемое значение

Итератор токенов. Разыменование возвращает `sub_match`.

## Что делает

Итерирует через указанные подвыражения во всех совпадениях.

## Примеры

### Базовое использование

```cpp
std::string s = "Hello 123 World 456";
std::regex re("(\\d+)");
for (auto it = std::sregex_token_iterator(s.begin(), s.end(), re, 1);
     it != std::sregex_token_iterator(); ++it)
    std::cout << it->str() << ' ';
// 123 456
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/regex
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_match|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_iterator|Вперёд]]
