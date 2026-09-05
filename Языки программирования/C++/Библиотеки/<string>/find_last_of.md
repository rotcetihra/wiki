# find_last_of

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string>|<string>]] / find_last_of

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/find_first_not_of|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/find_last_not_of|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string>
size_type find_last_of(const basic_string& str, size_type pos = npos) const noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `str` | множество символов |
| `pos` | позиция начала поиска назад |

## Возвращаемое значение

Позиция символа или `npos`.

## Что делает

Находит последний символ из множества `str`.

## Примеры

### Базовое использование

```cpp
std::string s = "Hello World";
std::cout << s.find_last_of("aeiou") << std::endl; // 7
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Потокобезопасна для разных объектов.')

## Источники

- https://en.cppreference.com/w/cpp/header/string
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/find_first_not_of|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/find_last_not_of|Вперёд]]
