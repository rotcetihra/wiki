# shared_timed_lock

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<shared_mutex>|<shared_mutex>]] / shared_timed_lock

[[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_lock|Назад]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_mutex|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <shared_mutex>

template <class Mutex>
class shared_lock;  // shared_timed_lock — это алиас
```

## Параметры

| Параметр | Описание |
|---|---|
| `Mutex` | Тип разделяемого мьютекса с поддержкой таймаутов |

## Возвращаемое значение

Не применимо (это класс).

## Что делает

`std::shared_timed_lock` — это RAII-обёртка для разделяемого захвата разделяемого мьютекса с поддержкой таймаутов. По сути является `std::shared_lock` с дополнительными методами `try_lock_for()` и `try_lock_until()`.

Позволяет ограничить время ожидания разделяемой блокировки. Если мьютекс не доступен, поток блокируется на указанное время.

## Примеры

### Базовое использование

```cpp
#include <shared_mutex>
#include <thread>
#include <iostream>
#include <chrono>

std::shared_timed_mutex smtx;

void timed_reader() {
    std::shared_timed_lock lock(smtx, std::chrono::milliseconds(100));
    if (lock.owns_lock()) {
        std::cout << "Read acquired\n";
    } else {
        std::cout << "Read timeout\n";
    }
}

int main() {
    std::thread t(timed_reader);
    t.join();
}
```

## Исключения

- **Исключения:** Конструктор и методы блокировки могут бросать `std::system_error`.
- **Безопасность в C++11:** Гарантирует разблокировку в деструкторе. Копирование запрещено, перемещение допустимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_lock|shared_lock]] — обёртка без таймаута
- [[Языки программирования/C++/Библиотеки/<mutex>/unique_lock|unique_lock]] — RAII для эксклюзивной блокировки

## Источники

- https://en.cppreference.com/w/cpp/thread/shared_lock
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_lock|Назад]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_mutex|Вперёд]]
