# vformat

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<format>|<format>]] / vformat

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/vformat_to|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/make_format_args|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <format>
string vformat(string_view fmt, format_args args);
```

## Параметры

| Параметр | Описание |
|---|---|
| `fmt` | форматная строка |
| `args` | аргументы форматирования |

## Возвращаемое значение

Отформатированная строка.

## Что делает

Нешаблонная функция форматирования с type-erased аргументами. Используется как база для `std::format`.

## Примеры

### Базовое использование

```cpp
auto args = std::make_format_args(42, 3.14);
std::string s = std::vformat("int={}, double={}", args);
std::cout << s << std::endl; // int=42, double=3.14
```

## Исключения

- **Исключения:** Может бросать `std::format_error`.

## Источники

- https://en.cppreference.com/w/cpp/header/format
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/vformat_to|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/make_format_args|Вперёд]]
