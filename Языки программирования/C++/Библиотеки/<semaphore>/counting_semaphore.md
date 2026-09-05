# counting_semaphore

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<semaphore>|<semaphore>]] / counting_semaphore

[[Языки программирования/C++/Библиотеки/<semaphore>/binary_semaphore|Назад]] | [[Языки программирования/C++/Библиотеки/<semaphore>|Содержание]] | [[Языки программирования/C++/Библиотеки/<semaphore>/acquire|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <semaphore>

template <std::ptrdiff_t Max = 1>
class counting_semaphore;
```

## Параметры

| Параметр | Описание |
|---|---|
| `Max` | Максимальное значение счётчика семафора (по умолчанию 1) |

## Возвращаемое значение

Не применимо (это класс).

## Что делает

`std::counting_semaphore` — это счётный семафор, ограничивающий количество потоков, имеющих доступ к ресурсу. Внутренний счётчик управляется операциями `acquire()` (уменьшает) и `release()` (увеличивает). Если счётчик равен нулю, `acquire()` блокирует поток до освобождения.

Полезен для ограничения числа одновременных подключений, пула потоков и других сценариев с ограниченным числом ресурсов.

## Примеры

### Базовое использование

```cpp
#include <semaphore>
#include <thread>
#include <iostream>

std::counting_semaphore<3> sem(3); // макс. 3 потока

void worker(int id) {
    sem.acquire();
    std::cout << "Worker " << id << " running\n";
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    sem.release();
}

int main() {
    std::thread workers[6];
    for (int i = 0; i < 6; ++i)
        workers[i] = std::thread(worker, i);
    for (auto& w : workers) w.join();
}
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Операции `acquire`, `release`, `try_acquire`, `try_acquire_for` потокобезопасны. Копирование и перемещение запрещены.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<semaphore>/binary_semaphore|binary_semaphore]] — бинарный семафор

## Источники

- https://en.cppreference.com/w/cpp/atomic/counting_semaphore
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<semaphore>/binary_semaphore|Назад]] | [[Языки программирования/C++/Библиотеки/<semaphore>|Содержание]] | [[Языки программирования/C++/Библиотеки/<semaphore>/acquire|Вперёд]]
