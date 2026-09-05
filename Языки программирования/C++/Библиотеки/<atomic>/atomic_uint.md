# atomic_uint

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<atomic>|<atomic>]] / atomic_uint

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_llong|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_ulong|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <atomic>

using atomic_uint = atomic<unsigned int>;
```

## Описание

Типовое определение `std::atomic<unsigned int>` — атомарный беззнаковый тип `unsigned int`.

## Примеры

```cpp
#include <atomic>
#include <iostream>

int main()
{
    std::atomic_uint value{0u};

    value.fetch_add(10u);
    std::cout << value.load() << std::endl; // 10
}
```

## Исключения

- **Исключения:** атомарные операции не бросают исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<atomic>/atomic|atomic]] — шаблон атомарного типа

## Источники

- https://en.cppreference.com/w/cpp/atomic/atomic
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_llong|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_ulong|Вперёд]]
