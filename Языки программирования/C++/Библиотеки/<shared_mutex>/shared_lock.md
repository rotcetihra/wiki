# shared_lock

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<shared_mutex>|<shared_mutex>]] / shared_lock

[[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_timed_mutex|Назад]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_timed_lock|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <shared_mutex>

template <class Mutex>
class shared_lock;
```

## Параметры

| Параметр | Описание |
|---|---|
| `Mutex` | Тип разделяемого мьютекса (например, `std::shared_mutex`, `std::shared_timed_mutex`) |

## Возвращаемое значение

Не применимо (это класс).

## Что делает

`std::shared_lock` — это RAII-обёртка для разделяемого (shared) захвата мьютекса. Позволяет нескольким потокам одновременно拥有 доступ для чтения. В отличие от `std::unique_lock`, который обеспечивает эксклюзивный доступ.

Поддерживает deferred lock, try_lock, timed lock, а также ручную блокировку/разблокировку через `lock()`, `unlock()`, `try_lock()`, `try_lock_for()`, `try_lock_until()`.

## Примеры

### Базовое использование

```cpp
#include <shared_mutex>
#include <thread>
#include <iostream>

std::shared_mutex smtx;
int data = 0;

void reader() {
    std::shared_lock<std::shared_mutex> lock(smtx);
    std::cout << "Read: " << data << "\n";
}

void writer() {
    std::unique_lock<std::shared_mutex> lock(smtx);
    data = 100;
}

int main() {
    std::thread r1(reader), r2(reader), w(writer);
    r1.join(); r2.join(); w.join();
}
```

## Исключения

- **Исключения:** Конструктор и методы блокировки могут бросать `std::system_error`.
- **Безопасность в C++11:** Гарантирует разблокировку в деструкторе. Копирование запрещено, перемещение допустимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<mutex>/unique_lock|unique_lock]] — RAII для эксклюзивной блокировки
- [[Языки программирования/C++/Библиотеки/<mutex>/shared_lock|shared_lock]] — обёртка из `<mutex>`

## Источники

- https://en.cppreference.com/w/cpp/thread/shared_lock
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_timed_mutex|Назад]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_timed_lock|Вперёд]]
