# wait

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<condition_variable>|<condition_variable>]] / wait

[[Языки программирования/C++/Библиотеки/<condition_variable>/wait_until|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/wait_for|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <condition_variable>

// condition_variable
void wait(std::unique_lock<std::mutex>& lock);

template <class Predicate>
void wait(std::unique_lock<std::mutex>& lock, Predicate pred);

// condition_variable_any
template <class Lock>
void wait(Lock& lock);

template <class Lock, class Predicate>
void wait(Lock& lock, Predicate pred);
```

## Параметры

| Параметр | Описание |
|---|---|
| `lock` | Блокируемый объект (обычно `std::unique_lock<std::mutex>`) |
| `pred` | Предикат, определяющий условие пробуждения |

## Возвращаемое значение

Не возвращает значения (`void`).

## Что делает

Блокирует текущий поток до тех пор, пока переменная условия не будет уведомлена и предикат `pred` не вернёт `true`. Если предикат не предоставлен, поток блокируется до уведомления.

При вызове `wait(lock)`:
1. Атомарно разблокирует мьютекс и приостанавливает поток.
2. При уведомлении пробуждается и повторно блокирует мьютекс.
3. Проверяет условие (если предикат предоставлен) и возвращает, если условие выполнено.

Без предиката возможны ложные пробуждения (spurious wakeups), поэтому рекомендуется всегда использовать предикат.

## Примеры

### Базовое использование

```cpp
#include <condition_variable>
#include <mutex>
#include <thread>
#include <iostream>

std::mutex mtx;
std::condition_variable cv;
bool data_ready = false;

void consumer() {
    std::unique_lock<std::mutex> lock(mtx);
    cv.wait(lock, [] { return data_ready; });
    std::cout << "Data consumed\n";
}

void producer() {
    {
        std::lock_guard<std::mutex> lock(mtx);
        data_ready = true;
    }
    cv.notify_one();
}

int main() {
    std::thread c(consumer);
    std::thread p(producer);
    c.join();
    p.join();
}
```

## Исключения

- **Исключения:** `wait` для `condition_variable` не бросает исключений. `wait` для `condition_variable_any` может бросить исключения при вызове `lock.unlock()` или `lock.lock()`.
- **Безопасность в C++11:** Вызывается только из заблокированного состояния.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<condition_variable>/wait_for|wait_for]] — ожидание с относительным таймаутом
- [[Языки программирования/C++/Библиотеки/<condition_variable>/wait_until|wait_until]] — ожидание с абсолютным таймаутом

## Источники

- https://en.cppreference.com/w/cpp/thread/condition_variable/wait
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<condition_variable>/wait_until|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/wait_for|Вперёд]]
