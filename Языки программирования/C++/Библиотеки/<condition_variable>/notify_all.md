# notify_all

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<condition_variable>|<condition_variable>]] / notify_all

[[Языки программирования/C++/Библиотеки/<condition_variable>/notify_one|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/notify_all_at_thread_exit|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <condition_variable>

void notify_all() noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| — | Параметров нет |

## Возвращаемое значение

Не возвращает значения (`void`).

## Что делает

Разблокирует все потоки, ожидающие на данной переменной условия. В отличие от `notify_one`, уведомляет каждого ожидающего потока. Потоки пробуждаются по одному и по очереди пытаются снова захватить мьютекс. Если ни один поток не ожидает, вызов ничего не делает.

Полезно, когда несколько потоков могут быть заинтересованы в изменении состояния (например, khi все ждут определённого условия).

## Примеры

### Базовое использование

```cpp
#include <condition_variable>
#include <mutex>
#include <thread>
#include <iostream>

std::mutex mtx;
std::condition_variable cv;
bool shutdown = false;

void worker(int id) {
    std::unique_lock<std::mutex> lock(mtx);
    cv.wait(lock, [] { return shutdown; });
    std::cout << "Worker " << id << " stopped\n";
}

void broadcaster() {
    {
        std::lock_guard<std::mutex> lock(mtx);
        shutdown = true;
    }
    cv.notify_all();
}

int main() {
    std::thread w1(worker, 1);
    std::thread w2(worker, 2);
    std::thread w3(worker, 3);
    std::thread b(broadcaster);
    w1.join(); w2.join(); w3.join(); b.join();
}
```

## Исключения

- **Исключения:** Функция не бросает исключений.
- **Безопасность в C++11:** Потокобезопасна. Может вызываться из обработчика сигнала.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<condition_variable>/notify_one|notify_one]] — уведомление одного потока

## Источники

- https://en.cppreference.com/w/cpp/thread/condition_variable/notify_all
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<condition_variable>/notify_one|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/notify_all_at_thread_exit|Вперёд]]
