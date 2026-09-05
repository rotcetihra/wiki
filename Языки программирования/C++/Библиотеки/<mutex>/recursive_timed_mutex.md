# recursive_timed_mutex

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<mutex>|<mutex>]] / recursive_timed_mutex

[[Языки программирования/C++/Библиотеки/<mutex>/timed_mutex|Назад]] | [[Языки программирования/C++/Библиотеки/<mutex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<mutex>/lock_guard|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <mutex>

class recursive_timed_mutex;
```

## Параметры

| Параметр | Описание |
|---|---|
| — | Класс не имеет параметров конструктора (кроме конструктора по умолчанию) |

## Возвращаемое значение

Не применимо (это класс).

## Что делает

`std::recursive_timed_mutex` — это рекурсивный мьютекс с поддержкой таймаутов. Объединяет возможности `std::recursive_mutex` (многократная блокировка одним потоком) и `std::timed_mutex` (блокировка с ограничением по времени).

Может быть заблокирован одним потоком несколько раз. Каждая блокировка увеличивает внутренний счётчик. Методы `try_lock_for()` и `try_lock_until()` позволяют указать максимальное время ожидания.

## Примеры

### Базовое использование

```cpp
#include <mutex>
#include <thread>
#include <iostream>
#include <chrono>

std::recursive_timed_mutex rmtx;

void recursive_func(int n) {
    if (rmtx.try_lock_for(std::chrono::milliseconds(100))) {
        std::lock_guard<std::recursive_timed_mutex> lock(rmtx, std::adopt_lock);
        std::cout << "Depth: " << n << "\n";
        if (n > 0) recursive_func(n - 1);
    }
}

int main() {
    std::thread t(recursive_func, 3);
    t.join();
}
```

## Исключения

- **Исключения:** `lock()` и `try_lock_for()` бросают `std::system_error` при ошибке блокировки.
- **Безопасность в C++11:** Копирование и перемещение запрещены. Рекурсивная блокировка безопасна.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<mutex>/recursive_mutex|recursive_mutex]] — рекурсивный мьютекс без таймаута
- [[Языки программирования/C++/Библиотеки/<mutex>/timed_mutex|timed_mutex]] — мьютекс с таймаутом без рекурсии

## Источники

- https://en.cppreference.com/w/cpp/thread/recursive_timed_mutex
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<mutex>/timed_mutex|Назад]] | [[Языки программирования/C++/Библиотеки/<mutex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<mutex>/lock_guard|Вперёд]]
