# string_view

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string_view>|<string_view>]] / string_view

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/basic_string_view|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/u8string_view|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string_view>
using string_view = basic_string_view<char>;
```

## Параметры

| Параметр | Описание |
|---|---|


## Возвращаемое значение

Алиас для `basic_string_view<char>`.

## Что делает

Самый часто используемый тип строкового вида.

## Примеры

### Базовое использование

```cpp
std::string_view sv = "Hello";
std::cout << sv << std::endl; // Hello
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Потокобезопасна для разных объектов.')

## Источники

- https://en.cppreference.com/w/cpp/header/string_view
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/basic_string_view|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/u8string_view|Вперёд]]
