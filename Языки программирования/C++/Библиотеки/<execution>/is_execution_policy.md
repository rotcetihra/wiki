# is_execution_policy

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<execution>|<execution>]] / is_execution_policy

[[Языки программирования/C++/Библиотеки/<execution>/unseq|Назад]] | [[Языки программирования/C++/Библиотеки/<execution>|Содержание]] | [[Языки программирования/C++/Библиотеки/<execution>/execute|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <execution>

template<class T>
struct is_execution_policy;
```

## Параметры

| Параметр | Описание |
|---|---|
| `T` | Проверяемый тип |

## Возвращаемое значение

`std::true_type` если `T` — один из типов политик выполнения (`sequenced_policy`, `parallel_policy`, `parallel_unsequenced_policy`).

## Что делает

Трейт для определения, является ли тип политикой выполнения.

## Примеры

```cpp
#include <execution>
#include <iostream>

int main()
{
    std::cout << std::is_execution_policy_v<std::execution::par> << std::endl; // 1
    std::cout << std::is_execution_policy_v<int> << std::endl;                 // 0
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- `std::is_same` — проверка типов

## Источники

- https://en.cppreference.com/w/cpp/execution/is_execution_policy
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<execution>/unseq|Назад]] | [[Языки программирования/C++/Библиотеки/<execution>|Содержание]] | [[Языки программирования/C++/Библиотеки/<execution>/execute|Вперёд]]
