# stold

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string>|<string>]] / stold

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/to_string|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/to_wstring|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string>
long double stold(const string& str, size_t* idx = nullptr);
```

## Параметры

| Параметр | Описание |
|---|---|
| `str` | строка |
| `idx` | позиция |

## Возвращаемое значение

Значение `long double`.

## Что делает

Преобразует строку в `long double`.

## Примеры

### Базовое использование

```cpp
std::string s = "3.14159265358979323846";
long double val = std::stold(s);
```

## Исключения

- **Исключения:** `std::invalid_argument`, `std::out_of_range`.

## Источники

- https://en.cppreference.com/w/cpp/header/string
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/to_string|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/to_wstring|Вперёд]]
