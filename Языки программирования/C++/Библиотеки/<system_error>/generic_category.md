# generic_category

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<system_error>|<system_error>]] / generic_category

[[Языки программирования/C++/Библиотеки/<system_error>/system_error|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/system_category|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <system_error>

const std::error_category& generic_category() noexcept;
```

## Параметры

Нет.

## Возвращаемое значение

Ссылка на глобальный объект `error_category`, представляющий стандартные коды ошибок (`std::errc`).

## Что делает

Возвращает категорию общих (стандартных) ошибок C++. Используется с `std::errc`.

## Примеры

```cpp
#include <system_error>
#include <iostream>

int main()
{
    auto ec = std::make_error_code(std::errc::permission_denied);
    std::cout << ec.category().name() << std::endl; // "generic"
    std::cout << ec.message() << std::endl; // "Permission denied"
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<system_error>/system_category|system_category]] — системная категория

## Источники

- https://en.cppreference.com/w/cpp/error/generic_category
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<system_error>/system_error|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/system_category|Вперёд]]
