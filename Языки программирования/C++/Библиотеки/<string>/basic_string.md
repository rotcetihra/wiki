# basic_string

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string>|<string>]] / basic_string

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/char_traits|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/allocator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string>
template<class CharT, class Traits = char_traits<CharT>,
         class Allocator = allocator<CharT>>
class basic_string;
```

## Параметры

| Параметр | Описание |
|---|---|
| `CharT` | тип символа |
| `Traits` | свойства символов |
| `Allocator` | аллокатор |

## Возвращаемое значение

Объект строки.

## Что делает

Динамически изменяемый массив символов с автоматическим управлением памятью. Поддерживает Unicode, сравнение, поиск.

## Примеры

### Базовое использование

```cpp
std::string s1 = "Hello";
std::string s2 = s1 + " World";
std::cout << s2 << std::endl; // Hello World
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Потокобезопасна для разных объектов.')

## Источники

- https://en.cppreference.com/w/cpp/header/string
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/char_traits|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/allocator|Вперёд]]
