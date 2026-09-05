# shared_mutex

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<shared_mutex>|<shared_mutex>]] / shared_mutex

[[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_timed_lock|Назад]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_timed_mutex|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <shared_mutex>

class shared_mutex;
```

## Параметры

| Параметр | Описание |
|---|---|
| — | Класс не имеет параметров конструктора (кроме конструктора по умолчанию) |

## Возвращаемое значение

Не применимо (это класс).

## Что делает

`std::shared_mutex` — это разделяемый мьютекс, поддерживающий два режима блокировки:
- **Эксклюзивный** (`lock()`, `try_lock()`) — только один поток может быть заблокирован.
- **Разделяемый** (`lock_shared()`, `try_lock_shared()`) — несколько потоков могут одновременно拥有 доступ для чтения.

Оптимален для сценариев «много читателей — один писатель». Читатели блокируются только при наличии активного писателя.

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
    data = 42;
    std::cout << "Written\n";
}

int main() {
    std::thread r1(reader), r2(reader), w(writer);
    r1.join(); r2.join(); w.join();
}
```

## Исключения

- **Исключения:** Методы блокировки могут бросать `std::system_error`.
- **Безопасность в C++11:** Копирование и перемещение запрещены. Читательские блокировки совместимы друг с другом, эксклюзивная блокировка эксклюзивна.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_timed_mutex|shared_timed_mutex]] — разделяемый мьютекс с таймаутом
- [[Языки программирования/C++/Библиотеки/<mutex>/mutex|mutex]] — эксклюзивный мьютекс

## Источники

- https://en.cppreference.com/w/cpp/thread/shared_mutex
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_timed_lock|Назад]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_timed_mutex|Вперёд]]
