# remove_suffix

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string_view>|<string_view>]] / remove_suffix

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/starts_with|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/ends_with|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string_view>
constexpr void remove_suffix(size_type n);
```

## Параметры

| Параметр | Описание |
|---|---|
| `n` | количество символов |

## Возвращаемое значение

Ничего не возвращает.

## Что делает

Сдвигает конец на `n` символов назад.

## Примеры

### Базовое использование

```cpp
std::string_view sv = "Hello World";
sv.remove_suffix(6);
std::cout << sv << std::endl; // Hello
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Потокобезопасна для разных объектов.')

## Источники

- https://en.cppreference.com/w/cpp/header/string_view
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/starts_with|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/ends_with|Вперёд]]
