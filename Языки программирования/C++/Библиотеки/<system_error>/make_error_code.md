# make_error_code

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<system_error>|<system_error>]] / make_error_code

[[Языки программирования/C++/Библиотеки/<system_error>/system_category|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/make_error_condition|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <system_error>

template<class E>
std::error_code make_error_code(E e) noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `e` | Значение перечисления ошибок (например, `std::errc`) |

## Возвращаемое значение

`error_code`, построенный из значения `e` и соответствующей категории.

## Что делает

Создаёт `error_code` из значений перечислений ошибок (`std::errc`, `std::io_errc`, `std::future_errc`).

## Примеры

```cpp
#include <system_error>
#include <iostream>

int main()
{
    auto ec = std::make_error_code(std::errc::not_supported);
    std::cout << ec.message() << std::endl; // "Not supported"
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<system_error>/make_error_condition|make_error_condition]] — создание условия

## Источники

- https://en.cppreference.com/w/cpp/error/make_error_code
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<system_error>/system_category|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/make_error_condition|Вперёд]]
