# notify_all_at_thread_exit

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<condition_variable>|<condition_variable>]] / notify_all_at_thread_exit

[[Языки программирования/C++/Библиотеки/<condition_variable>/notify_all|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/cv_status|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <condition_variable>

void notify_all_at_thread_exit(
    std::condition_variable& cond,
    std::unique_lock<std::mutex>& lock);
```

## Параметры

| Параметр | Описание |
|---|---|
| `cond` | Переменная условия для уведомления |
| `lock` | Заблокированный `unique_lock`, который будет разблокирован в деструкторе |

## Возвращаемое значение

Не возвращает значения (`void`).

## Что делает

Регистрирует уведомление переменной условия `cond` и разблокировку `lock`, которые произойдут при завершении текущего потока (при выходе из потока или при уничтожении `std::thread` без `join`/`detach`). Уведомление отправляется всем ожидающим потокам (аналог `notify_all`).

Это удобно для реализации паттерна «master-slave», когда главный поток должен дождаться завершения всех рабочих потоков и получить уведомление.

## Примеры

### Базовое использование

```cpp
#include <condition_variable>
#include <mutex>
#include <thread>
#include <iostream>

std::mutex mtx;
std::condition_variable cv;
bool finished = false;

void worker() {
    std::unique_lock<std::mutex> lock(mtx);
    // Регистрация уведомления при завершении потока
    notify_all_at_thread_exit(cv, std::move(lock));
    // Работа потока...
    std::cout << "Worker finished\n";
}

void waiter() {
    std::unique_lock<std::mutex> lock(mtx);
    cv.wait(lock, [] { return finished; });
    std::cout << "All workers done\n";
}

int main() {
    std::thread w(worker);
    std::thread wait_thread(waiter);
    w.join();
    wait_thread.join();
}
```

## Исключения

- **Исключения:** Функция не бросает исключений.
- **Безопасность в C++11:** Должна вызываться из потока, для которого registrado уведомление. `lock` должен быть заблокирован.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<condition_variable>/notify_all|notify_all]] — уведомление всех потоков в текущий момент

## Источники

- https://en.cppreference.com/w/cpp/thread/condition_variable/notify_all_at_thread_exit
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<condition_variable>/notify_all|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/cv_status|Вперёд]]
