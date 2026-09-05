# atomic_ulong

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<atomic>|<atomic>]] / atomic_ulong

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_uint|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_ullong|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <atomic>

using atomic_ulong = atomic<unsigned long>;
```

## Описание

Типовое определение `std::atomic<unsigned long>` — атомарный беззнаковый тип `unsigned long`.

## Примеры

```cpp
#include <atomic>
#include <iostream>

int main()
{
    std::atomic_ulong value{42UL};

    value.store(100UL);
    std::cout << value.load() << std::endl; // 100
}
```

## Исключения

- **Исключения:** атомарные операции не бросают исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<atomic>/atomic|atomic]] — шаблон атомарного типа

## Источники

- https://en.cppreference.com/w/cpp/atomic/atomic
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_uint|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_ullong|Вперёд]]
