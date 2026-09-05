# unique_lock

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<mutex>|<mutex>]] / unique_lock

[[Языки программирования/C++/Библиотеки/<mutex>/scoped_lock|Назад]] | [[Языки программирования/C++/Библиотеки/<mutex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<mutex>/shared_lock|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <mutex>

template <class Mutex>
class unique_lock;
```

## Параметры

| Параметр | Описание |
|---|---|
| `Mutex` | Тип мьютекса (например, `std::mutex`, `std::timed_mutex`) |

## Возвращаемое значение

Не применимо (это класс).

## Что делает

`std::unique_lock` — это гибкая RAII-обёртка для мьютекса. В отличие от `lock_guard`, поддерживает: deferred lock (отложенную блокировку), try_lock (попытку блокировки), timed lock (блокировку с таймаутом), а также ручную блокировку/разблокировку через `lock()`, `unlock()`, `try_lock()`, `try_lock_for()`, `try_lock_until()`.

Является обязательной обёрткой для использования с `std::condition_variable`.

## Примеры

### Базовое использование

```cpp
#include <mutex>
#include <thread>
#include <iostream>

std::mutex mtx;

void worker() {
    std::unique_lock<std::mutex> lock(mtx);
    std::cout << "Locked\n";
    lock.unlock();
    std::cout << "Unlocked\n";
    lock.lock();
    std::cout << "Re-locked\n";
}

int main() {
    std::thread t(worker);
    t.join();
}
```

## Исключения

- **Исключения:** Конструктор и методы блокировки могут бросать `std::system_error`.
- **Безопасность в C++11:** Гарантирует разблокировку в деструкторе. Копирование запрещено, перемещение допустимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<mutex>/lock_guard|lock_guard]] — простая RAII-обёртка
- [[Языки программирования/C++/Библиотеки/<mutex>/shared_lock|shared_lock]] — RAII для разделяемой блокировки

## Источники

- https://en.cppreference.com/w/cpp/thread/unique_lock
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<mutex>/scoped_lock|Назад]] | [[Языки программирования/C++/Библиотеки/<mutex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<mutex>/shared_lock|Вперёд]]
