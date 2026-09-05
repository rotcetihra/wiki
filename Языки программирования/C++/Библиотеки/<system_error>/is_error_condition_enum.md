# is_error_condition_enum

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<system_error>|<system_error>]] / is_error_condition_enum

[[Языки программирования/C++/Библиотеки/<system_error>/is_error_code_enum|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <system_error>

template<class E>
struct is_error_condition_enum;
```

## Параметры

| Параметр | Описание |
|---|---|
| `E` | Проверяемый тип |

## Возвращаемое значение

`std::true_type` если `E` — enum, который может быть использован для создания `error_condition`.

## Что делает

Трейт для определения, может ли тип перечисления быть преобразован в `error_condition`.

## Примеры

```cpp
#include <system_error>
#include <iostream>

int main()
{
    std::cout << std::is_error_condition_enum_v<std::errc> << std::endl; // 1
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<system_error>/is_error_code_enum|is_error_code_enum]] — для `error_code`

## Источники

- https://en.cppreference.com/w/cpp/error/is_error_condition_enum
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<system_error>/is_error_code_enum|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>|Вперёд]]
