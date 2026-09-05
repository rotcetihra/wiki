# format_parse_context

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<format>|<format>]] / format_parse_context

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format_context|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/make_format_args|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <format>
template<class CharT>
class basic_format_parse_context;
using format_parse_context = basic_format_parse_context<char>;
```

## Параметры

| Параметр | Описание |
|---|---|
| `CharT` | тип символа |

## Возвращаемое значение

Итератор по форматной строке.

## Что делает

Контекст разбора форматной строки, передаваемый методу `formatter::parse`. Предоставляет итераторы по форматной строке.

## Примеры

### Базовое использование

```cpp
// Использование в formatter::parse:
template<>
struct std::formatter<MyType> {
    constexpr auto parse(std::format_parse_context& ctx) {
        auto it = ctx.begin();
        auto end = ctx.end();
        return it;
    }
};
```

## Исключения

- **Исключения:** Не бросает исключений.

## Источники

- https://en.cppreference.com/w/cpp/header/format
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format_context|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/make_format_args|Вперёд]]
