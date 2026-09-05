# stoi

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string>|<string>]] / stoi

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stol|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stoll|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string>
int stoi(const string& str, size_t* idx = nullptr, int base = 10);
```

## Параметры

| Параметр | Описание |
|---|---|
| `str` | строка |
| `idx` | позиция необработанного символа |
| `base` | система счисления |

## Возвращаемое значение

Значение `int`.

## Что делает

Преобразует строку в `int`. Бросает `std::invalid_argument` или `std::out_of_range`.

## Примеры

### Базовое использование

```cpp
std::string s = "42 hello";
size_t pos;
int val = std::stoi(s, &pos);
std::cout << val << std::endl; // 42
std::cout << pos << std::endl; // 2
```

## Исключения

- **Исключения:** `std::invalid_argument`, `std::out_of_range`.

## Источники

- https://en.cppreference.com/w/cpp/header/string
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stol|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/stoll|Вперёд]]
