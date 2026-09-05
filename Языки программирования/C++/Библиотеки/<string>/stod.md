# stod

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string>|<string>]] / stod

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stold|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/to_string|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string>
double stod(const string& str, size_t* idx = nullptr);
```

## Параметры

| Параметр | Описание |
|---|---|
| `str` | строка |
| `idx` | позиция |

## Возвращаемое значение

Значение `double`.

## Что делает

Преобразует строку в `double`.

## Примеры

### Базовое использование

```cpp
std::string s = "2.718281828";
double val = std::stod(s);
std::cout << val << std::endl;
```

## Исключения

- **Исключения:** `std::invalid_argument`, `std::out_of_range`.

## Источники

- https://en.cppreference.com/w/cpp/header/string
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stold|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/to_string|Вперёд]]
