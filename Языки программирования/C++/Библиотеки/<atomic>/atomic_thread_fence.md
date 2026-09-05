# atomic_thread_fence

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<atomic>|<atomic>]] / atomic_thread_fence

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_ullong|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_signal_fence|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <atomic>

void atomic_thread_fence(memory_order order) noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `order` | Порядок памяти (`memory_order_acquire`, `memory_order_release` и т.д.) |

## Возвращаемое значение

Не возвращает значения.

## Что делает

Устанавливает барьер памяти между операциями в разных потоках. Гарантирует, что операции до барьера не будут перемещены после него и наоборот.

## Примеры

```cpp
#include <atomic>
#include <iostream>
#include <thread>

int data = 0;
std::atomic<bool> ready{false};

void producer()
{
    data = 42;
    std::atomic_thread_fence(std::memory_order_release);
    ready.store(true, std::memory_order_relaxed);
}

void consumer()
{
    while (!ready.load(std::memory_order_relaxed))
        ;
    std::atomic_thread_fence(std::memory_order_acquire);
    std::cout << data << std::endl; // 42
}

int main()
{
    std::thread p(producer);
    std::thread c(consumer);
    p.join();
    c.join();
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<atomic>/atomic_signal_fence|atomic_signal_fence]] — барьер для сигналов
- [[Языки программирования/C++/Библиотеки/<atomic>/memory_order|memory_order]] — порядок памяти

## Источники

- https://en.cppreference.com/w/cpp/atomic/atomic_thread_fence
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_ullong|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_signal_fence|Вперёд]]
