# try_acquire_for

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<semaphore>|<semaphore>]] / try_acquire_for

[[Языки программирования/C++/Библиотеки/<semaphore>/try_acquire|Назад]] | [[Языки программирования/C++/Библиотеки/<semaphore>|Содержание]] | [[Языки программирования/C++/Библиотеки/<semaphore>/binary_semaphore|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <semaphore>

template <class Rep, class Period>
bool try_acquire_for(const std::chrono::duration<Rep, Period>& rel_time);
```

## Параметры

| Параметр | Описание |
|---|---|
| `rel_time` | Относительный таймаут ожидания |

## Возвращаемое значение

`true` — если захват выполнен успешно, `false` — если истёк таймаут.

## Что делает

Пытается уменьшить внутренний счётчик семафора на 1 с ограничением по времени. Если счётчик больше нуля, уменьшает его и возвращает `true`. Если счётчик равен нулю, блокирует поток на указанное время. Если за это время счётчик не увеличится, возвращает `false`.

Комбинирует возможности `acquire()` и `try_acquire()` с таймаутом.

## Примеры

### Базовое использование

```cpp
#include <semaphore>
#include <thread>
#include <iostream>
#include <chrono>

std::counting_semaphore<1> sem(0);

int main() {
    if (sem.try_acquire_for(std::chrono::milliseconds(100))) {
        std::cout << "Acquired\n";
    } else {
        std::cout << "Timeout\n";
    }
}
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасна.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<semaphore>/acquire|acquire]] — захват без таймаута
- [[Языки программирования/C++/Библиотеки/<semaphore>/try_acquire|try_acquire]] — попытка захвата без ожидания

## Источники

- https://en.cppreference.com/w/cpp/atomic/counting_semaphore/try_acquire_for
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<semaphore>/try_acquire|Назад]] | [[Языки программирования/C++/Библиотеки/<semaphore>|Содержание]] | [[Языки программирования/C++/Библиотеки/<semaphore>/binary_semaphore|Вперёд]]
