# shared_timed_mutex

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<shared_mutex>|<shared_mutex>]] / shared_timed_mutex

[[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_mutex|Назад]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_lock|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <shared_mutex>

class shared_timed_mutex;
```

## Параметры

| Параметр | Описание |
|---|---|
| — | Класс не имеет параметров конструктора (кроме конструктора по умолчанию) |

## Возвращаемое значение

Не применимо (это класс).

## Что делает

`std::shared_timed_mutex` — это разделяемый мьютекс с поддержкой таймаутов. Помимо стандартных операций `lock_shared()` и `lock()`, предоставляет методы `try_lock_for()`, `try_lock_until()`, `try_lock_shared_for()` и `try_lock_shared_until()` для блокировки с ограничением по времени.

В отличие от `std::shared_mutex`, добавлена возможность указать максимальное время ожидания блокировки.

## Примеры

### Базовое использование

```cpp
#include <shared_mutex>
#include <thread>
#include <iostream>
#include <chrono>

std::shared_timed_mutex smtx;

void timed_writer() {
    if (smtx.try_lock_for(std::chrono::milliseconds(100))) {
        std::cout << "Writer acquired\n";
        std::this_thread::sleep_for(std::chrono::milliseconds(50));
        smtx.unlock();
    } else {
        std::cout << "Writer timeout\n";
    }
}

int main() {
    std::thread t(timed_writer);
    t.join();
}
```

## Исключения

- **Исключения:** Методы блокировки могут бросать `std::system_error`.
- **Безопасность в C++11:** Копирование и перемещение запрещены.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_mutex|shared_mutex]] — разделяемый мьютекс без таймаута
- [[Языки программирования/C++/Библиотеки/<mutex>/timed_mutex|timed_mutex]] — эксклюзивный мьютекс с таймаутом

## Источники

- https://en.cppreference.com/w/cpp/thread/shared_timed_mutex
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_mutex|Назад]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<shared_mutex>/shared_lock|Вперёд]]
