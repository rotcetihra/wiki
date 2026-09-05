# formatter

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<format>|<format>]] / formatter

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format_parse_context|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format_context|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <format>
template<class T, class CharT = char>
struct formatter;
```

## Параметры

| Параметр | Описание |
|---|---|
| `T` | тип значения |
| `CharT` | тип символа |

## Возвращаемое значение

Специализация `formatter<T, CharT>` с методами `parse` и `format`.

## Что делает

Шаблон `std::formatter` определяет правила форматирования для типа `T`. Метод `parse` разбирает спецификаторы, `format` форматирует значение.

## Примеры

### Базовое использование

```cpp
struct Point { int x, y; };

template<>
struct std::formatter<Point> : std::formatter<std::string> {
    auto format(const Point& p, std::format_context& ctx) const {
        return std::format_to(ctx.out(), "({}, {})", p.x, p.y);
    }
};

int main() {
    Point p{10, 20};
    std::string s = std::format("Point: {}", p);
    std::cout << s << std::endl; // Point: (10, 20)
}
```

## Исключения

- **Исключения:** Зависит от специализации.

## Источники

- https://en.cppreference.com/w/cpp/header/format
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format_parse_context|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/format_context|Вперёд]]
