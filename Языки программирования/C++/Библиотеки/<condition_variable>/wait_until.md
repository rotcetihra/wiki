# wait_until

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<condition_variable>|<condition_variable>]] / wait_until

[[Языки программирования/C++/Библиотеки/<condition_variable>/wait_for|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/notify_one|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <condition_variable>

// condition_variable
template <class Clock, class Duration>
std::cv_status wait_until(
    std::unique_lock<std::mutex>& lock,
    const std::chrono::time_point<Clock, Duration>& abs_time);

template <class Clock, class Duration, class Predicate>
bool wait_until(
    std::unique_lock<std::mutex>& lock,
    const std::chrono::time_point<Clock, Duration>& abs_time,
    Predicate pred);

// condition_variable_any
template <class Lock, class Clock, class Duration>
std::cv_status wait_until(
    Lock& lock,
    const std::chrono::time_point<Clock, Duration>& abs_time);

template <class Lock, class Clock, class Duration, class Predicate>
bool wait_until(
    Lock& lock,
    const std::chrono::time_point<Clock, Duration>& abs_time,
    Predicate pred);
```

## Параметры

| Параметр | Описание |
|---|---|
| `lock` | Блокируемый объект |
| `abs_time` | Абсолютный момент времени до которого длится ожидание |
| `pred` | Предикат, определяющий условие пробуждения |

## Возвращаемое значение

- Без предиката: `std::cv_status::no_timeout` или `std::cv_status::timeout`.
- С предикатом: `true`, если условие выполнено, `false` — если истёк таймаут.

## Что делает

Блокирует текущий поток до уведомления или наступления абсолютного момента времени. В отличие от `wait_for`, принимает абсолютное время, что исключает проблемы с дрифтом времени.

## Примеры

### Базовое использование

```cpp
#include <condition_variable>
#include <mutex>
#include <thread>
#include <iostream>
#include <chrono>

std::mutex mtx;
std::condition_variable cv;

void worker() {
    std::unique_lock<std::mutex> lock(mtx);
    auto deadline = std::chrono::steady_clock::now() + std::chrono::seconds(1);
    auto status = cv.wait_until(lock, deadline, [] { return false; });
    if (status == std::cv_status::timeout) {
        std::cout << "Timeout\n";
    }
}

int main() {
    std::thread t(worker);
    t.join();
}
```

## Исключения

- **Исключения:** Аналогично `wait`.
- **Безопасность в C++11:** Вызывается только из заблокированного состояния.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<condition_variable>/wait|wait]] — ожидание без таймаута
- [[Языки программирования/C++/Библиотеки/<condition_variable>/wait_for|wait_for]] — ожидание с относительным таймаутом

## Источники

- https://en.cppreference.com/w/cpp/thread/condition_variable/wait_until
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<condition_variable>/wait_for|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/notify_one|Вперёд]]
