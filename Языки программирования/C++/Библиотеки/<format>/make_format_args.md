# make_format_args

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<format>|<format>]] / make_format_args

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/visit_format_arg|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <format>
template<class Context = format_context, class... Args>
__format_arg_store<Context, Args...> make_format_args(Args&&... fmt_args);
```

## Параметры

| Параметр | Описание |
|---|---|
| `fmt_args` | аргументы для форматирования |

## Возвращаемое значение

Объект `format_arg_store`, преобразуемый в `format_args`.

## Что делает

Создаёт type-erased хранилище аргументов форматирования. Используется с `vformat`.

## Примеры

### Базовое использование

```cpp
auto store = std::make_format_args(42, "hello", 3.14);
std::format_args args = store;
std::string s = std::vformat("{} {} {}", args);
std::cout << s << std::endl; // 42 hello 3.14
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/format
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/visit_format_arg|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format|Вперёд]]
