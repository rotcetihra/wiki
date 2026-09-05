# atomic_ullong

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<atomic>|<atomic>]] / atomic_ullong

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_ulong|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_thread_fence|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <atomic>

using atomic_ullong = atomic<unsigned long long>;
```

## Описание

Типовое определение `std::atomic<unsigned long long>` — атомарный беззнаковый тип `unsigned long long`.

## Примеры

```cpp
#include <atomic>
#include <iostream>

int main()
{
    std::atomic_ullong value{0ULL};

    value += 1000000000ULL;
    std::cout << value.load() << std::endl; // 1000000000
}
```

## Исключения

- **Исключения:** атомарные операции не бросают исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<atomic>/atomic|atomic]] — шаблон атомарного типа

## Источники

- https://en.cppreference.com/w/cpp/atomic/atomic
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_ulong|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_thread_fence|Вперёд]]
