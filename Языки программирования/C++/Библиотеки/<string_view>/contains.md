# contains

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string_view>|<string_view>]] / contains

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/ends_with|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string_view>
constexpr bool contains(basic_string_view x) const noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `x` | подстрока для проверки |

## Возвращаемое значение

`true`, если подстрока найдена.

## Что делает

Проверяет наличие подстроки. Доступно с C++23.

## Примеры

### Базовое использование

```cpp
std::string_view sv = "Hello World";
std::cout << std::boolalpha << sv.contains("lo Wo") << std::endl; // true
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Потокобезопасна для разных объектов.')

## Источники

- https://en.cppreference.com/w/cpp/header/string_view
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/ends_with|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]]
