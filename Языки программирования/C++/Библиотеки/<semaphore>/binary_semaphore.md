# binary_semaphore

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<semaphore>|<semaphore>]] / binary_semaphore

[[Языки программирования/C++/Библиотеки/<semaphore>/try_acquire_for|Назад]] | [[Языки программирования/C++/Библиотеки/<semaphore>|Содержание]] | [[Языки программирования/C++/Библиотеки/<semaphore>/counting_semaphore|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <semaphore>

using binary_semaphore = counting_semaphore<1>;
```

## Параметры

| Параметр | Описание |
|---|---|
| — | Алиас для `counting_semaphore<1>` |

## Возвращаемое значение

Не применимо (это алиас типа).

## Что делает

`std::binary_semaphore` — это семафор с максимальным значением 1. Эквивалентен классическому бинарному семафору. Может находиться в двух состояниях: «доступен» (счётчик > 0) и «занят» (счётчик == 0).

Функционально аналогичен мьютексу, но имеет другую семантику: семафор не имеет владельца потока и может быть освобождён любым потоком.

## Примеры

### Базовое использование

```cpp
#include <semaphore>
#include <thread>
#include <iostream>

std::binary_semaphore signal(0);

void waiter() {
    signal.acquire();
    std::cout << "Signal received\n";
}

void notifier() {
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    signal.release();
}

int main() {
    std::thread w(waiter), n(notifier);
    w.join(); n.join();
}
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Операции потокобезопасны. Копирование и перемещение запрещены.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<semaphore>/counting_semaphore|counting_semaphore]] — счётный семафор
- [[Языки программирования/C++/Библиотеки/<mutex>/mutex|mutex]] — мьютекс

## Источники

- https://en.cppreference.com/w/cpp/atomic/binary_semaphore
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<semaphore>/try_acquire_for|Назад]] | [[Языки программирования/C++/Библиотеки/<semaphore>|Содержание]] | [[Языки программирования/C++/Библиотеки/<semaphore>/counting_semaphore|Вперёд]]
