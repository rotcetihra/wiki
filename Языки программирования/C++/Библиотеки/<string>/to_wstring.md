# to_wstring

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<string>|<string>]] / to_wstring

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/find|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/rfind|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <string>
wstring to_wstring(int val);
wstring to_wstring(long val);
wstring to_wstring(long long val);
wstring to_wstring(unsigned val);
wstring to_wstring(unsigned long val);
wstring to_wstring(unsigned long long val);
wstring to_wstring(float val);
wstring to_wstring(double val);
wstring to_wstring(long double val);
```

## Параметры

| Параметр | Описание |
|---|---|
| `val` | числовое значение |

## Возвращаемое значение

Широкая строка (`wstring`) с представлением числа.

## Что делает

Преобразует число в `wstring`.

## Примеры

### Базовое использование

```cpp
std::wstring ws = std::to_wstring(42);
std::wcout << ws << std::endl; // 42
```

## Исключения

- ('bad_alloc', 'Бросает `std::bad_alloc` при ошибке выделения памяти.')
- ('safe', 'Потокобезопасна для разных объектов.')

## Источники

- https://en.cppreference.com/w/cpp/header/string
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/find|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/rfind|Вперёд]]
