# stoul

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string>|<string>]] / stoul

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stoull|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stof|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string>
unsigned long stoul(const string& str, size_t* idx = nullptr, int base = 10);
```

## Параметры

| Параметр | Описание |
|---|---|
| `str` | строка |
| `idx` | позиция |
| `base` | система счисления |

## Возвращаемое значение

Значение `unsigned long`.

## Что делает

Преобразует строку в `unsigned long`.

## Примеры

### Базовое использование

```cpp
std::string s = "4294967295";
unsigned long val = std::stoul(s);
std::cout << val << std::endl;
```

## Исключения

- **Исключения:** `std::invalid_argument`, `std::out_of_range`.

## Источники

- https://en.cppreference.com/w/cpp/header/string
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stoull|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stof|Вперёд]]
