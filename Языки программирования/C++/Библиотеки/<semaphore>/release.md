# release

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<semaphore>|<semaphore>]] / release

[[Языки программирования/C++/Библиотеки/<semaphore>/acquire|Назад]] | [[Языки программирования/C++/Библиотеки/<semaphore>|Содержание]] | [[Языки программирования/C++/Библиотеки/<semaphore>/try_acquire|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <semaphore>

void release(std::ptrdiff_t update = 1);
```

## Параметры

| Параметр | Описание |
|---|---|
| `update` | Количество, на которое увеличивается счётчик (по умолчанию 1) |

## Возвращаемое значение

Не возвращает значения (`void`).

## Что делает

Увеличивает внутренний счётчик семафора на величину `update`. Если несколько потоков заблокированы в `acquire()`, один из них разблокируется. Операция выполняется атомарно.

Вызывается после освобождения ресурса для уведомления других потоков о возможности захвата.

## Примеры

### Базовое использование

```cpp
#include <semaphore>
#include <thread>
#include <iostream>

std::counting_semaphore<1> sem(0);

void waiter() {
    sem.acquire();
    std::cout << "Acquired\n";
}

void notifier() {
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    sem.release();
}

int main() {
    std::thread w(waiter), n(notifier);
    w.join(); n.join();
}
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасна.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<semaphore>/acquire|acquire]] — захват семафора
- [[Языки программирования/C++/Библиотеки/<semaphore>/try_acquire|try_acquire]] — попытка захвата

## Источники

- https://en.cppreference.com/w/cpp/atomic/counting_semaphore/release
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<semaphore>/acquire|Назад]] | [[Языки программирования/C++/Библиотеки/<semaphore>|Содержание]] | [[Языки программирования/C++/Библиотеки/<semaphore>/try_acquire|Вперёд]]
