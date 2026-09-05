# format_to_n

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<format>|<format>]] / format_to_n

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format_to|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/formatted_size|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <format>
template<class Out, class... Args>
format_to_n_result<Out> format_to_n(Out out, iter_difference_t<Out> n,
                                    format_string<Args...> fmt, Args&&... args);
```

## Параметры

| Параметр | Описание |
|---|---|
| `out` | выходной итератор |
| `n` | макс. символов |
| `fmt` | форматная строка |
| `args` | аргументы |

## Возвращаемое значение

Структура `format_to_n_result` с итератором `out` и размером `size`.

## Что делает

Записывает форматированное представление, не превышая `n` символов.

## Примеры

### Базовое использование

```cpp
std::vector<char> buf(10);
auto [it, sz] = std::format_to_n(buf.begin(), 5, "Hello, {}!", "World");
std::string s(buf.begin(), it);
std::cout << s << std::endl; // Hello
```

## Исключения

- **Исключения:** Бросает `std::format_error` при ошибке форматирования.

## Источники

- https://en.cppreference.com/w/cpp/header/format
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format_to|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/formatted_size|Вперёд]]
