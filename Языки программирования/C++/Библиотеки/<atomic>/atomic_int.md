# atomic_int

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<atomic>|<atomic>]] / atomic_int

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_bool|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_long|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <atomic>

using atomic_int = atomic<int>;
```

## Описание

Типовое определение `std::atomic<int>` — атомарный тип `int`.

## Примеры

```cpp
#include <atomic>
#include <iostream>

int main()
{
    std::atomic_int counter{0};

    counter.fetch_add(1);
    counter += 5;

    std::cout << counter.load() << std::endl; // 6
}
```

## Исключения

- **Исключения:** атомарные операции не бросают исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<atomic>/atomic|atomic]] — шаблон атомарного типа

## Источники

- https://en.cppreference.com/w/cpp/atomic/atomic
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_bool|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_long|Вперёд]]
