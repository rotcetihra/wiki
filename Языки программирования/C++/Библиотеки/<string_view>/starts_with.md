# starts_with

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string_view>|<string_view>]] / starts_with

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/remove_suffix|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/ends_with|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string_view>
constexpr bool starts_with(basic_string_view x) const noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `x` | префикс для проверки |

## Возвращаемое значение

`true`, если строковый вид начинается с префикса.

## Что делает

Проверяет начало строки. Доступно с C++20.

## Примеры

### Базовое использование

```cpp
std::string_view sv = "Hello World";
std::cout << std::boolalpha << sv.starts_with("Hello") << std::endl; // true
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Потокобезопасна для разных объектов.')

## Источники

- https://en.cppreference.com/w/cpp/header/string_view
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/remove_suffix|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/ends_with|Вперёд]]
