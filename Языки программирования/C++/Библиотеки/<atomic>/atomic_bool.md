# atomic_bool

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<atomic>|<atomic>]] / atomic_bool

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_flag|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_int|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <atomic>

using atomic_bool = atomic<bool>;
```

## Описание

Типовое определение `std::atomic<bool>` — атомарный булев тип.

## Примеры

```cpp
#include <atomic>
#include <iostream>

int main()
{
    std::atomic_bool ready{false};

    ready.store(true);
    std::cout << ready.load() << std::endl; // 1 (true)
}
```

## Исключения

- **Исключения:** атомарные операции не бросают исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<atomic>/atomic|atomic]] — шаблон атомарного типа

## Источники

- https://en.cppreference.com/w/cpp/atomic/atomic
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_flag|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_int|Вперёд]]
