# wait_for

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<condition_variable>|<condition_variable>]] / wait_for

[[Языки программирования/C++/Библиотеки/<condition_variable>/wait|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/wait_until|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <condition_variable>

// condition_variable
template <class Rep, class Period>
std::cv_status wait_for(
    std::unique_lock<std::mutex>& lock,
    const std::chrono::duration<Rep, Period>& rel_time);

template <class Rep, class Period, class Predicate>
bool wait_for(
    std::unique_lock<std::mutex>& lock,
    const std::chrono::duration<Rep, Period>& rel_time,
    Predicate pred);

// condition_variable_any
template <class Lock, class Rep, class Period>
std::cv_status wait_for(
    Lock& lock,
    const std::chrono::duration<Rep, Period>& rel_time);

template <class Lock, class Rep, class Period, class Predicate>
bool wait_for(
    Lock& lock,
    const std::chrono::duration<Rep, Period>& rel_time,
    Predicate pred);
```

## Параметры

| Параметр | Описание |
|---|---|
| `lock` | Блокируемый объект |
| `rel_time` | Относительный таймаут ожидания |
| `pred` | Предикат, определяющий условие пробуждения |

## Возвращаемое значение

- Без предиката: `std::cv_status::no_timeout` или `std::cv_status::timeout`.
- С предикатом: `true`, если условие выполнено, `false` — если истёк таймаут.

## Что делает

Блокирует текущий поток до уведомления или истечения относительного таймаута. В отличие от `wait`, поддерживает ограничение по времени. Если предикат предоставлен, возвращает `true` при выполнении условия и `false` при таймауте.

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
    auto status = cv.wait_for(lock, std::chrono::seconds(1), [] { return false; });
    if (!status) {
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
- [[Языки программирования/C++/Библиотеки/<condition_variable>/wait_until|wait_until]] — ожидание с абсолютным таймаутом

## Источники

- https://en.cppreference.com/w/cpp/thread/condition_variable/wait_for
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<condition_variable>/wait|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/wait_until|Вперёд]]
