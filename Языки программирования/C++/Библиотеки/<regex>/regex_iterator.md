# regex_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<regex>|<regex>]] / regex_iterator

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_token_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/sub_match|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <regex>
template<class BiIt, class CharT = typename iterator_traits<BiIt>::value_type,
          class Traits = regex_traits<CharT>>
class regex_iterator;
using sregex_iterator = regex_iterator<string::const_iterator>;
```

## Параметры

| Параметр | Описание |
|---|---|
| `BiIt` | итератор |
| `CharT` | тип символа |
| `Traits` | свойства |

## Возвращаемое значение

Итератор совпадений. Разыменование возвращает `match_results`.

## Что делает

Итерирует через все совпадения regex в строке. При инкрементации ищет следующее совпадение.

## Примеры

### Базовое использование

```cpp
std::string s = "one 1, two 2, three 3";
std::regex re("\\d+");
for (auto it = std::sregex_iterator(s.begin(), s.end(), re);
     it != std::sregex_iterator(); ++it)
    std::cout << it->str() << ' ';
// 1 2 3
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/regex
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_token_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/sub_match|Вперёд]]
