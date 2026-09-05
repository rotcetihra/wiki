# format_context

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<format>|<format>]] / format_context

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format_arg_store|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format_parse_context|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <format>
template<class Out, class CharT>
class basic_format_context;
using format_context = basic_format_context</* unspecified */, char>;
```

## Параметры

| Параметр | Описание |
|---|---|
| `Out` | выходной итератор |
| `CharT` | тип символа |

## Возвращаемое значение

Итератор после последнего записанного символа.

## Что делает

Контекст форматирования, передаваемый методу `formatter::format`. Содержит выходной итератор и аргументы.

## Примеры

### Базовое использование

```cpp
// Использование в formatter::format:
template<>
struct std::formatter<MyType> {
    auto format(const MyType& val, std::format_context& ctx) const {
        return std::format_to(ctx.out(), "{}", val.value);
    }
};
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/format
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format_arg_store|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format_parse_context|Вперёд]]
