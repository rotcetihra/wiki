# notify_one

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<condition_variable>|<condition_variable>]] / notify_one

[[Языки программирования/C++/Библиотеки/<condition_variable>/wait_until|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/notify_all|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <condition_variable>

void notify_one() noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| — | Параметров нет |

## Возвращаемое значение

Не возвращает значения (`void`).

## Что делает

Разблокирует один из потоков, ожидающих на данной переменной условия. Если несколько потоков находятся в состоянии ожидания, системой выбирается один из них (порядок не определён). Если ни один поток не ожидает, вызов ничего не делает.

Функция может вызываться как с заблокированным, так и с разблокированным мьютексом. Вызов с заблокированным мьютексом может привести к тому, что разблокированный поток сразу же заблокируется снова.

## Примеры

### Базовое использование

```cpp
#include <condition_variable>
#include <mutex>
#include <thread>
#include <iostream>

std::mutex mtx;
std::condition_variable cv;
bool ready = false;

void worker() {
    std::unique_lock<std::mutex> lock(mtx);
    cv.wait(lock, [] { return ready; });
    std::cout << "Worker done\n";
}

void notifier() {
    {
        std::lock_guard<std::mutex> lock(mtx);
        ready = true;
    }
    cv.notify_one();
}

int main() {
    std::thread w(worker);
    std::thread n(notifier);
    w.join();
    n.join();
}
```

## Исключения

- **Исключения:** Функция не бросает исключений.
- **Безопасность в C++11:** Потокобезопасна. Может вызываться из обработчика сигнала.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<condition_variable>/notify_all|notify_all]] — уведомление всех ожидающих потоков

## Источники

- https://en.cppreference.com/w/cpp/thread/condition_variable/notify_one
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<condition_variable>/wait_until|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/notify_all|Вперёд]]
