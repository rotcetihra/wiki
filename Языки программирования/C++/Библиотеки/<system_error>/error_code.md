# error_code

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<system_error>|<system_error>]] / error_code

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/error_condition|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <system_error>

class error_code;
```

## Параметры

Нет.

## Возвращаемое значение

Класс `std::error_code` — портативный код ошибки с указанием категории.

## Что делает

Представляет код ошибки в сочетании с категорией. Используется как возвращаемое значение функций, сообщающих об ошибках (например, `std::filesystem`).

## Примеры

```cpp
#include <system_error>
#include <iostream>

int main()
{
    std::error_code ec = std::make_error_code(std::errc::no_such_file_or_directory);
    std::cout << ec.message() << std::endl; // "No such file or directory"
    std::cout << ec.category().name() << std::endl; // "generic"
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<system_error>/error_condition|error_condition]] — условие ошибки

## Источники

- https://en.cppreference.com/w/cpp/error/error_code
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/error_condition|Вперёд]]
