# atomic

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<atomic>|<atomic>]] / atomic

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_flag|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <atomic>

template<class T>
class atomic;
```

## Описание

Шаблон `std::atomic` обеспечивает атомарные операции над значением типа `T`. Поддерживается для целочисленных типов, указателей и `bool`. Объекты `atomic` не являются copyable/movable.

## Методы

| Метод | Описание |
|---|---|
| `store(T, memory_order)` | Атомарная запись |
| `load(memory_order)` | Атомарное чтение |
| `exchange(T, memory_order)` | Атомарная замена |
| `compare_exchange_strong(T&, T, ...)` | Атомарная условная замена (сильная) |
| `compare_exchange_weak(T&, T, ...)` | Атомарная условная замена (слабая) |
| `fetch_add(T, memory_order)` | Атомарное инкрементирование |
| `fetch_sub(T, memory_order)` | Атомарное декрементирование |
| `operator=` | Атомарное присваивание |
| `operator T()` | Атомарное чтение |

## Примеры

```cpp
#include <atomic>
#include <iostream>
#include <thread>

std::atomic<int> counter{0};

void increment()
{
    for (int i = 0; i < 1000; ++i)
        counter.fetch_add(1, std::memory_order_relaxed);
}

int main()
{
    std::thread t1(increment);
    std::thread t2(increment);

    t1.join();
    t2.join();

    std::cout << "Счётчик: " << counter.load() << std::endl; // 2000
}
```

## Исключения

- **Исключения:** атомарные операции не бросают исключений.
- **Безопасность:** потокобезопасны поdesign. `atomic<T>` требует `sizeof(T) == alignof(T)` и тривиально-копируемого типа.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<atomic>/atomic_flag|atomic_flag]] — атомарный флаг

## Источники

- https://en.cppreference.com/w/cpp/atomic/atomic
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_flag|Вперёд]]
