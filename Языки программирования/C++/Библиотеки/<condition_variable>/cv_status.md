# cv_status

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<condition_variable>|<condition_variable>]] / cv_status

[[Языки программирования/C++/Библиотеки/<condition_variable>/notify_all_at_thread_exit|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/condition_variable|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <condition_variable>

enum class cv_status {
    no_timeout,
    timeout
};
```

## Параметры

| Параметр | Описание |
|---|---|
| `no_timeout` | Ожидание завершилось по условию (без таймаута) |
| `timeout` | Истёк таймаут ожидания |

## Возвращаемое значение

Не применимо (это перечисление).

## Что делает

`std::cv_status` — это перечисление, используемое для возврата результата операций ожидания с таймаутом (`wait_for` и `wait_until`). Значение `no_timeout` указывает, что ожидание завершилось из-за уведомления (условие выполнено), а `timeout` — что время ожидания истекло.

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
bool ready = false;

void waiter() {
    std::unique_lock<std::mutex> lock(mtx);
    auto status = cv.wait_for(lock, std::chrono::milliseconds(100),
                              [] { return ready; });
    if (status == std::cv_status::timeout) {
        std::cout << "Timeout occurred\n";
    } else {
        std::cout << "Condition met\n";
    }
}

int main() {
    std::thread t(waiter);
    t.join();
}
```

## Исключения

- **Исключения:** Перечисление не бросает исключений.
- **Безопасность в C++11:** Тип безопасен для использования в многопоточной среде.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<condition_variable>/wait_for|wait_for]] — возвращает `cv_status`
- [[Языки программирования/C++/Библиотеки/<condition_variable>/wait_until|wait_until]] — возвращает `cv_status`

## Источники

- https://en.cppreference.com/w/cpp/thread/condition_variable/cv_status
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<condition_variable>/notify_all_at_thread_exit|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/condition_variable|Вперёд]]
