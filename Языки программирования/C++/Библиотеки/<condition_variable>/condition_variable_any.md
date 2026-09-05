# condition_variable_any

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<condition_variable>|<condition_variable>]] / condition_variable_any

[[Языки программирования/C++/Библиотеки/<condition_variable>/condition_variable|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/cv_status|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <condition_variable>

class condition_variable_any;
```

## Параметры

| Параметр | Описание |
|---|---|
| — | Класс не имеет параметров конструктора (кроме конструктора по умолчанию и перемещения) |

## Возвращаемое значение

Не применимо (это класс).

## Что делает

`std::condition_variable_any` — это универсальная переменная условия, которая может работать с любым объектом, поддерживающим операции `lock()` и `unlock()` ( Lockable). В отличие от `std::condition_variable`, которая ограничена `std::unique_lock<std::mutex>`, `condition_variable_any` работает с `std::unique_lock`, `std::shared_lock`, `std::lock_guard` и другими совместимыми обёртками.

Это делает её более гибкой, но может привести к дополнительным накладным расходам из-за полиморфного вызова виртуальных методов.

## Примеры

### Базовое использование

```cpp
#include <condition_variable>
#include <mutex>
#include <thread>
#include <iostream>

std::mutex mtx;
std::condition_variable_any cv;
bool ready = false;

void worker() {
    std::unique_lock<std::mutex> lock(mtx);
    cv.wait(lock, [] { return ready; });
    std::cout << "Worker running\n";
}

void starter() {
    {
        std::lock_guard<std::mutex> lock(mtx);
        ready = true;
    }
    cv.notify_one();
}

int main() {
    std::thread w(worker);
    std::thread s(starter);
    w.join();
    s.join();
}
```

## Исключения

- **Исключения:** Аналогично `std::condition_variable`.
- **Безопасность в C++11:** Операции `wait`, `notify_one`, `notify_all` потокобезопасны. Копирование запрещено, перемещение допустимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<condition_variable>/condition_variable|condition_variable]] — переменная условия для `std::unique_lock<std::mutex>`

## Источники

- https://en.cppreference.com/w/cpp/thread/condition_variable_any
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<condition_variable>/condition_variable|Назад]] | [[Языки программирования/C++/Библиотеки/<condition_variable>|Содержание]] | [[Языки программирования/C++/Библиотеки/<condition_variable>/cv_status|Вперёд]]
