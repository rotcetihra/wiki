# stoll

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string>|<string>]] / stoll

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stoul|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stoull|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string>
long long stoll(const string& str, size_t* idx = nullptr, int base = 10);
```

## Параметры

| Параметр | Описание |
|---|---|
| `str` | строка |
| `idx` | позиция |
| `base` | система счисления |

## Возвращаемое значение

Значение `long long`.

## Что делает

Преобразует строку в `long long`.

## Примеры

### Базовое использование

```cpp
std::string s = "9223372036854775807";
long long val = std::stoll(s);
std::cout << val << std::endl;
```

## Исключения

- **Исключения:** `std::invalid_argument`, `std::out_of_range`.

## Источники

- https://en.cppreference.com/w/cpp/header/string
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stoul|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stoull|Вперёд]]
