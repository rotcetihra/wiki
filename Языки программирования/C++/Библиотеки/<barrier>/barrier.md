# barrier

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<barrier>|<barrier>]] / barrier

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<barrier>|Содержание]] | [[Языки программирования/C++/Библиотеки/<barrier>/arrival_token|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <barrier>

template<class Completion = std::default_completion_function>
class barrier;
```

## Описание

`std::barrier` — механизм синхронизации потоков с фазами. Потоки вызывают `arrive_and_wait` и ждут, пока все потоки не прибудут. После завершения фазы вызывается completion function и начинается новая фаза.

## Конструктор

```cpp
barrier(ptrdiff_t num_threads, Completion f = Completion());
```

| Параметр | Описание |
|---|---|
| `num_threads` | Количество потоков, участвующих в барьере |
| `f` | Функция, вызываемая в конце каждой фазы |

## Методы

| Метод | Описание |
|---|---|
| `arrive()` | Прибытие без ожидания |
| `arrive_and_wait()` | Прибытие и ожидание |
| `arrive_and_drop()` | Прибытие с отказом от участия в следующей фазе |
| `phase_count()` | Текущий номер фазы |

## Примеры

```cpp
#include <barrier>
#include <iostream>
#include <thread>
#include <vector>

int main()
{
    constexpr int num_threads = 4;
    std::barrier barrier(num_threads);

    std::vector<std::jthread> threads;
    for (int i = 0; i < num_threads; ++i)
        threads.emplace_back([&barrier, i]{
            std::cout << "Поток " << i << " ждёт\n";
            barrier.arrive_and_wait();
            std::cout << "Поток " << i << " прошёл\n";
        });
}
```

## Исключения

- **Исключения:** `arrive_and_wait` может бросать исключения.
- **Безопасность:** объект `barrier` не является copyable/movable.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<barrier>/arrival_token|arrival_token]] — токен прибытия

## Источники

- https://en.cppreference.com/w/cpp/thread/barrier
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<barrier>|Содержание]] | [[Языки программирования/C++/Библиотеки/<barrier>/arrival_token|Вперёд]]
