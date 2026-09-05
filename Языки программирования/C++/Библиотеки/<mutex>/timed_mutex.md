# timed_mutex

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<mutex>|<mutex>]] / timed_mutex

[[Языки программирования/C++/Библиотеки/<mutex>/recursive_mutex|Назад]] | [[Языки программирования/C++/Библиотеки/<mutex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<mutex>/recursive_timed_mutex|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <mutex>

class timed_mutex;
```

## Параметры

| Параметр | Описание |
|---|---|
| — | Класс не имеет параметров конструктора (кроме конструктора по умолчанию) |

## Возвращаемое значение

Не применимо (это класс).

## Что делает

`std::timed_mutex` — это мьютекс с поддержкой таймаутов. Помимо стандартных операций `lock()`, `try_lock()` и `unlock()`, предоставляет методы `try_lock_for()` и `try_lock_until()`, которые позволяют указать максимальное время ожидания блокировки.

Например, `try_lock_for(std::chrono::seconds(1))` пытается заблокировать мьютекс в течение одной секунды. Если за это время блокировка не удалась, возвращается `false`.

## Примеры

### Базовое использование

```cpp
#include <mutex>
#include <thread>
#include <iostream>
#include <chrono>

std::timed_mutex tmtx;

void worker() {
    if (tmtx.try_lock_for(std::chrono::milliseconds(100))) {
        std::cout << "Locked\n";
        std::this_thread::sleep_for(std::chrono::milliseconds(50));
        tmtx.unlock();
    } else {
        std::cout << "Failed to lock\n";
    }
}

int main() {
    std::thread t1(worker);
    std::thread t2(worker);
    t1.join();
    t2.join();
}
```

## Исключения

- **Исключения:** `lock()` и `try_lock_for()` бросают `std::system_error` при ошибке блокировки.
- **Безопасность в C++11:** Копирование и перемещение запрещены. Не является рекурсивным.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<mutex>/mutex|mutex]] — мьютекс без таймаута
- [[Языки программирования/C++/Библиотеки/<mutex>/recursive_timed_mutex|recursive_timed_mutex]] — рекурсивный мьютекс с таймаутом

## Источники

- https://en.cppreference.com/w/cpp/thread/timed_mutex
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<mutex>/recursive_mutex|Назад]] | [[Языки программирования/C++/Библиотеки/<mutex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<mutex>/recursive_timed_mutex|Вперёд]]
