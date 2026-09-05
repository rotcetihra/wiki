# substr

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string_view>|<string_view>]] / substr

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/find_last_not_of|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/compare|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string_view>
constexpr basic_string_view substr(size_type pos = 0, size_type n = npos) const;
```

## Параметры

| Параметр | Описание |
|---|---|
| `pos` | начальная позиция |
| `n` | максимальная длина |

## Возвращаемое значение

Новый `string_view` с подстрокой.

## Что делает

Возвращает подстроку. Не копирует данные — результат ссылается на те же данные.

## Примеры

### Базовое использование

```cpp
std::string_view sv = "Hello World";
std::cout << sv.substr(6, 5) << std::endl; // World
```

## Исключения

- **Исключения:** Бросает `std::out_of_range`, если `pos > size()`.

## Источники

- https://en.cppreference.com/w/cpp/header/string_view
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/find_last_not_of|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/compare|Вперёд]]
