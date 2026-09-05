# memory_order

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<atomic>|<atomic>]] / memory_order

[[Языки программирования/C++/Библиотеки/<atomic>/kill_dependency|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <atomic>

enum memory_order {
    memory_order_relaxed,
    memory_order_consume,
    memory_order_acquire,
    memory_order_release,
    memory_order_acq_rel,
    memory_order_seq_cst
};
```

## Описание

Перечисление, определяющее уровень гарантий порядка выполнения атомарных операций.

| Значение | Описание |
|---|---|
| `relaxed` | Нет гарантий порядка (только атомарность) |
| `consume` | Гарантии для depend-operations (poisoning) |
| `acquire` | Операции чтения не перемещаются до этой операции |
| `release` | Операции записи не перемещаются после этой операции |
| `acq_rel` | Комбинация acquire + release |
| `seq_cst` | Полная последовательная согласованность (по умолчанию) |

## Примеры

```cpp
#include <atomic>
#include <iostream>
#include <thread>

std::atomic<int> data{0};
std::atomic<bool> ready{false};

void producer()
{
    data.store(42, std::memory_order_release);
    ready.store(true, std::memory_order_release);
}

void consumer()
{
    while (!ready.load(std::memory_order_acquire))
        ;
    std::cout << data.load(std::memory_order_acquire) << std::endl; // 42
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<atomic>/atomic_thread_fence|atomic_thread_fence]] — барьер памяти

## Источники

- https://en.cppreference.com/w/cpp/atomic/memory_order
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<atomic>/kill_dependency|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>|Вперёд]]
