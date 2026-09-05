# format

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<format>|<format>]] / format

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format_to|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <format>
template<class... Args>
string format(format_string<Args...> fmt, Args&&... args);
```

## Параметры

| Параметр | Описание |
|---|---|
| `fmt` | форматная строка |
| `args` | аргументы для форматирования |

## Возвращаемое значение

Отформатированная строка.

## Что делает

Форматирует аргументы в строку. Форматная строка проверяется на этапе компиляции. Поддерживает локали через перегрузку с `std::locale`.

## Примеры

### Базовое использование

```cpp
std::string s = std::format("Hello, {}! You are {} years old.", "Alice", 30);
std::cout << s << std::endl;
// Hello, Alice! You are 30 years old.
std::string pi = std::format("Pi is {:.2f}", 3.14159);
std::cout << pi << std::endl;
// Pi is 3.14
```

## Исключения

- **Исключения:** Бросает `std::format_error` при ошибке форматирования.

## Источники

- https://en.cppreference.com/w/cpp/header/format
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format_to|Вперёд]]
