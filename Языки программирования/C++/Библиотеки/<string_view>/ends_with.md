# ends_with

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string_view>|<string_view>]] / ends_with

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/starts_with|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/contains|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string_view>
constexpr bool ends_with(basic_string_view x) const noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `x` | суффикс для проверки |

## Возвращаемое значение

`true`, если строковый вид заканчивается суффиксом.

## Что делает

Проверяет конец строки. Доступно с C++20.

## Примеры

### Базовое использование

```cpp
std::string_view sv = "Hello World";
std::cout << std::boolalpha << sv.ends_with("World") << std::endl; // true
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Потокобезопасна для разных объектов.')

## Источники

- https://en.cppreference.com/w/cpp/header/string_view
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/starts_with|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/contains|Вперёд]]
