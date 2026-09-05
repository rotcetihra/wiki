# condition_variable

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<condition_variable>|<condition_variable>]] / condition_variable

[[Языки программирования/C++/Библиотеки/<condition_variable>/cv_status|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/condition_variable_any|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <condition_variable>

class condition_variable;
```

## Параметры

| Параметр | Описание |
|---|---|
| — | Класс не имеет параметров конструктора (кроме конструктора по умолчанию и перемещения) |

## Возвращаемое значение

Не применимо (это класс).

## Что делает

`std::condition_variable` — это примитив синхронизации, используемый для блокировки одного или нескольких потоков до тех пор, пока другой поток не выполнит уведомление с помощью функции `notify_one()` или `notify_all()`. Переменная условия работает совместно с `std::mutex`: поток блокирует мьютекс, проверяет условие и, если условие не выполнено, вызывает `wait()`, который разблокирует мьютекс и приостанавливает поток до уведомления.

Класс `std::condition_variable` может использоваться только с `std::unique_lock<std::mutex>`, в отличие от `std::condition_variable_any`, которая работает с любым блокируемым объектом.

## Примеры

### Базовое использование

```cpp
#include <condition_variable>
#include <mutex>
#include <thread>
#include <iostream>
#include <queue>

std::mutex mtx;
std::condition_variable cv;
std::queue<int> data_queue;
bool finished = false;

void producer() {
    for (int i = 0; i < 5; ++i) {
        std::lock_guard<std::mutex> lock(mtx);
        data_queue.push(i);
        std::cout << "Produced: " << i << "\n";
    }
    {
        std::lock_guard<std::mutex> lock(mtx);
        finished = true;
    }
    cv.notify_all();
}

void consumer() {
    while (true) {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, [] { return !data_queue.empty() || finished; });
        while (!data_queue.empty()) {
            std::cout << "Consumed: " << data_queue.front() << "\n";
            data_queue.pop();
        }
        if (finished) break;
    }
}

int main() {
    std::thread prod(producer);
    std::thread cons(consumer);
    prod.join();
    cons.join();
}
```

## Исключения

- **Исключения:** `condition_variable` не предоставляет自己的 исключения. Ошибки синхронизации приводят к неопределённому поведению.
- **Безопасность в C++11:** Операции `wait`, `notify_one`, `notify_all` потокобезопасны. Копирование запрещено, перемещение допустимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<condition_variable>/condition_variable_any|condition_variable_any]] — универсальная переменная условия для любого блокируемого объекта

## Источники

- https://en.cppreference.com/w/cpp/thread/condition_variable
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<condition_variable>/cv_status|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/condition_variable_any|Вперёд]]
