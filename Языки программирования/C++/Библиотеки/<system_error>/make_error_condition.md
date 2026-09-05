# make_error_condition

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<system_error>|<system_error>]] / make_error_condition

[[Языки программирования/C++/Библиотеки/<system_error>/make_error_code|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/is_error_code_enum|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <system_error>

template<class E>
std::error_condition make_error_condition(E e) noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `e` | Значение перечисления ошибок |

## Возвращаемое значение

`error_condition`, построенный из значения `e`.

## Что делает

Создаёт `error_condition` из значений перечислений ошибок.

## Примеры

```cpp
#include <system_error>
#include <iostream>

int main()
{
    auto cond = std::make_error_condition(std::errc::not_supported);
    std::cout << cond.message() << std::endl; // "Not supported"
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<system_error>/make_error_code|make_error_code]] — создание кода ошибки

## Источники

- https://en.cppreference.com/w/cpp/error/make_error_condition
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<system_error>/make_error_code|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/is_error_code_enum|Вперёд]]
