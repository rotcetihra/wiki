# error_category

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<system_error>|<system_error>]] / error_category

[[Языки программирования/C++/Библиотеки/<system_error>/error_condition|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/system_error|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <system_error>

class error_category;
```

## Параметры

Нет.

## Возвращаемое значение

Абстрактный базовый класс для категорий ошибок.

## Что делает

Определяет интерфейс для категорий ошибок: имя, сравнение, получение `error_condition` по коду. Готовые категории: `generic_category()` и `system_category()`.

## Примеры

```cpp
#include <system_error>
#include <iostream>

int main()
{
    const auto& cat = std::generic_category();
    std::cout << cat.name() << std::endl; // "generic"
}
```

## Исключения

- **Исключения:** виртуальные методы могут бросать исключения.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<system_error>/generic_category|generic_category]] — общая категория
- [[Языки программирования/C++/Библиотеки/<system_error>/system_category|system_category]] — системная категория

## Источники

- https://en.cppreference.com/w/cpp/error/error_category
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<system_error>/error_condition|Назад]] | [[Языки программирования/C++/Библиотеки/<system_error>|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>/system_error|Вперёд]]
