# operator!=

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string_view>|<string_view>]] / operator!=

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/operator<|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/operator>|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string_view>
template<class CharT, class Traits>
constexpr bool operator!=(
    basic_string_view<CharT, Traits> x,
    type_identity_t<basic_string_view<CharT, Traits>> y) noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `x` | левый операнд |
| `y` | правый операнд |

## Возвращаемое значение

`true`, если строковые виды не равны.

## Что делает

Эквивалентно `!(x == y)`.

## Примеры

### Базовое использование

```cpp
std::string_view a = "hello";
std::string_view b = "world";
std::cout << std::boolalpha << (a != b) << std::endl; // true
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Потокобезопасна для разных объектов.')

## Источники

- https://en.cppreference.com/w/cpp/header/string_view
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/operator<|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/operator>|Вперёд]]
