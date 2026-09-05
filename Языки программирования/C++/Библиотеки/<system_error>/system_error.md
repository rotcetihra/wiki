# system_error

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<system_error>|<system_error>]] / system_error

[[Языки программирования/C++/Библиотеки/<system_error>/error_category|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/generic_category|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <system_error>

class system_error : public std::runtime_error;
```

## Параметры

| Параметр | Описание |
|---|---|
| `ec` | Код ошибки |
| `what_arg` | Сообщение об ошибке |

## Возвращаемое значение

Класс-исключение, содержащий `error_code`.

## Что делает

Исключение, бросаемое функциями, сообщающими об ошибках через `error_code`. Содержит `code()` для доступа к ошибке.

## Примеры

```cpp
#include <system_error>
#include <iostream>

int main()
{
    try {
        throw std::system_error(std::error_code(2, std::generic_category()));
    } catch (const std::system_error& e) {
        std::cout << e.what() << std::endl;
        std::cout << e.code().message() << std::endl;
    }
}
```

## Исключения

- **Исключения:** является исключением (наследник `runtime_error`).

## Похожие функции

- `std::runtime_error` — базовый класс

## Источники

- https://en.cppreference.com/w/cpp/error/system_error
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<system_error>/error_category|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/generic_category|Вперёд]]
