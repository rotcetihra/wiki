# sub_match

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<regex>|<regex>]] / sub_match

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/match_results|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <regex>
template<class BiIt>
class sub_match : public pair<BiIt, BiIt>;
```

## Параметры

| Параметр | Описание |
|---|---|
| `BiIt` | тип итератора |

## Возвращаемое значение

Объект `sub_match` с диапазоном совпадения и флагом `matched`.

## Что делает

Идентифицирует последовательность символов подвыражения. Наследует `pair<BiIt, BiIt>`, добавляет `matched`, `str()`, `length()`.

## Примеры

### Базовое использование

```cpp
std::string s = "Hello 123";
std::regex re("(\\d+)");
std::smatch m;
if (std::regex_search(s, m, re)) {
    std::cout << "Matched: " << m[1].matched << std::endl; // 1
    std::cout << "String: " << m[1].str() << std::endl; // 123
}
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/regex
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_iterator|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/match_results|Вперёд]]
