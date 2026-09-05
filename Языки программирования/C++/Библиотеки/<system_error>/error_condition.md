# error_condition

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<system_error>|<system_error>]] / error_condition

[[Языки программирования/C++/Библиотеки/<system_error>/error_code|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/error_category|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <system_error>

class error_condition;
```

## Параметры

Нет.

## Возвращаемое значение

Класс `std::error_condition` — портативное условие ошибки.

## Что делает

Представляет условие ошибки независимо от конкретной системы. Используется для проверки `error_code` через `equivalent()`.

## Примеры

```cpp
#include <system_error>
#include <iostream>

int main()
{
    std::error_condition ec = std::errc::no_such_file_or_directory;
    std::cout << ec.message() << std::endl; // "No such file or directory"
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<system_error>/error_code|error_code]] — код ошибки

## Источники

- https://en.cppreference.com/w/cpp/error/error_condition
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<system_error>/error_code|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/error_category|Вперёд]]
