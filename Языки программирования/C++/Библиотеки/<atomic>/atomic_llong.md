# atomic_llong

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<atomic>|<atomic>]] / atomic_llong

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_long|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_uint|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <atomic>

using atomic_llong = atomic<long long>;
```

## Описание

Типовое определение `std::atomic<long long>` — атомарный тип `long long`.

## Примеры

```cpp
#include <atomic>
#include <iostream>

int main()
{
    std::atomic_llong value{1000000000LL};

    value -= 500000000LL;
    std::cout << value.load() << std::endl; // 500000000
}
```

## Исключения

- **Исключения:** атомарные операции не бросают исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<atomic>/atomic|atomic]] — шаблон атомарного типа

## Источники

- https://en.cppreference.com/w/cpp/atomic/atomic
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_long|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_uint|Вперёд]]
