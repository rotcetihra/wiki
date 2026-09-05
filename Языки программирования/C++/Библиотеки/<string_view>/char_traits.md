# char_traits

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string_view>|<string_view>]] / char_traits

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/basic_string_view|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/wstring_view|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string_view>
template<class CharT>
struct char_traits;
```

## Параметры

| Параметр | Описание |
|---|---|
| `CharT` | тип символа |

## Возвращаемое значение

Класс с методами для работы с символами.

## Что делает

Определяет свойства символов для `basic_string_view`. Идентичен `std::char_traits` из `<string>`.

## Примеры

### Базовое использование

```cpp
using traits = std::char_traits<char>;
const char* s = "hello";
std::cout << traits.length(s) << std::endl; // 5
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Потокобезопасна для разных объектов.')

## Источники

- https://en.cppreference.com/w/cpp/header/string_view
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/basic_string_view|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/wstring_view|Вперёд]]
