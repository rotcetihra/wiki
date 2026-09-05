# basic_string_view

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string_view>|<string_view>]] / basic_string_view

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/char_traits|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/operator==|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string_view>
template<class CharT, class Traits = char_traits<CharT>>
class basic_string_view;
```

## Параметры

| Параметр | Описание |
|---|---|
| `CharT` | тип символа |
| `Traits` | свойства символов |

## Возвращаемое значение

Объект строкового вида.

## Что делает

Лёгкий не владеющий вид на последовательность символов. Хранит только указатель и размер. Не изменяет данные.

## Примеры

### Базовое использование

```cpp
std::string str = "Hello, World!";
std::string_view sv = str;
std::cout << sv.substr(0, 5) << std::endl; // Hello
```

## Исключения

- **Исключения:** Метод `at()` бросает `std::out_of_range`.

## Источники

- https://en.cppreference.com/w/cpp/header/string_view
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/char_traits|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/operator==|Вперёд]]
