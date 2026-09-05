# system_category

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<system_error>|<system_error>]] / system_category

[[Языки программирования/C++/Библиотеки/<system_error>/generic_category|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/make_error_code|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <system_error>

const std::error_category& system_category() noexcept;
```

## Параметры

Нет.

## Возвращаемое значение

Ссылка на глобальный объект `error_category`, представляющий системные ошибки платформы (POSIX `errno`, Windows `GetLastError()`).

## Что делает

Возвращает категорию системных ошибок. Коды ошибок — платформо-зависимые (например, `errno`).

## Примеры

```cpp
#include <system_error>
#include <iostream>

int main()
{
    auto ec = std::make_error_code(static_cast<std::errc>(ENOENT));
    std::cout << ec.category().name() << std::endl; // "generic" или "system"
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<system_error>/generic_category|generic_category]] — общая категория

## Источники

- https://en.cppreference.com/w/cpp/error/system_category
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<system_error>/generic_category|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/make_error_code|Вперёд]]
