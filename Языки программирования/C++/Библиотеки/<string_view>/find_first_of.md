# find_first_of

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string_view>|<string_view>]] / find_first_of

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/rfind|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/find_last_of|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string_view>
constexpr size_type find_first_of(basic_string_view s, size_type pos = 0) const noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `s` | множество символов |
| `pos` | начальная позиция |

## Возвращаемое значение

Позиция символа или `npos`.

## Что делает

Находит первый символ из множества.

## Примеры

### Базовое использование

```cpp
std::string_view sv = "Hello World";
std::cout << sv.find_first_of("aeiou") << std::endl; // 1
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Потокобезопасна для разных объектов.')

## Источники

- https://en.cppreference.com/w/cpp/header/string_view
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/rfind|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/find_last_of|Вперёд]]
