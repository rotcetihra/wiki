# is_formattable

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<format>|<format>]] / is_formattable

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/is_range|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/formatter|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <format>
template<class T, class CharT = char>
concept formattable = /* see description */;
```

## Параметры

| Параметр | Описание |
|---|---|
| `T` | проверяемый тип |
| `CharT` | тип символа |

## Возвращаемое значение

Концепт: `true`, если тип форматируем.

## Что делает

Концепт `formattable` определяет, что тип `T` может быть отформатирован через `std::format`.

## Примеры

### Базовое использование

```cpp
static_assert(std::formattable<int, char>);
static_assert(std::formattable<std::string, char>);
static_assert(!std::formattable<void, char>);
```

## Исключения

- **Исключения:** Концепт — не функция, исключений не бросает.

## Источники

- https://en.cppreference.com/w/cpp/header/format
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/is_range|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/formatter|Вперёд]]
