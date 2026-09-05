# atomic_signal_fence

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<atomic>|<atomic>]] / atomic_signal_fence

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_thread_fence|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/kill_dependency|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <atomic>

void atomic_signal_fence(memory_order order) noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `order` | Порядок памяти |

## Возвращаемое значение

Не возвращает значения.

## Что делает

Устанавливает барьер памяти для обработчиков сигналов в том же потоке. Не влияет на порядок операций между потоками (в отличие от `atomic_thread_fence`).

## Примеры

```cpp
#include <atomic>
#include <csignal>

int data = 0;

void signal_handler(int)
{
    std::atomic_signal_fence(std::memory_order_acquire);
    // data гарантированно видно после signal_handler
}

int main()
{
    data = 42;
    std::atomic_signal_fence(std::memory_order_release);
    std::raise(SIGUSR1);
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<atomic>/atomic_thread_fence|atomic_thread_fence]] — барьер для потоков

## Источники

- https://en.cppreference.com/w/cpp/atomic/atomic_signal_fence
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<atomic>/atomic_thread_fence|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/kill_dependency|Вперёд]]
