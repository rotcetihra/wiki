# acquire

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<semaphore>|<semaphore>]] / acquire

[[Языки программирования/C++/Библиотеки/<semaphore>/counting_semaphore|Назад]] | [[Языки программирования/C++/Библиотеки/<semaphore>|Содержание]] | [[Языки программирования/C++/Библиотеки/<semaphore>/release|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <semaphore>

void acquire();
```

## Параметры

| Параметр | Описание |
|---|---|
| — | Параметров нет |

## Возвращаемое значение

Не возвращает значения (`void`).

## Что делает

Уменьшает внутренний счётчик семафора на 1. Если счётчик равен нулю, блокирует поток до тех пор, пока другой поток не вызовет `release()`. Гарантирует, что операция выполнится атомарно.

После успешного вызова поток получает доступ к ресурсу, защищённому семафором.

## Примеры

### Базовое использование

```cpp
#include <semaphore>
#include <thread>
#include <iostream>

std::counting_semaphore<2> sem(2);

void worker(int id) {
    sem.acquire();
    std::cout << "Worker " << id << " started\n";
    std::this_thread::sleep_for(std::chrono::milliseconds(200));
    std::cout << "Worker " << id << " finished\n";
    sem.release();
}

int main() {
    std::thread t[4];
    for (int i = 0; i < 4; ++i) t[i] = std::thread(worker, i);
    for (auto& x : t) x.join();
}
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасна.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<semaphore>/release|release]] — освобождение семафора
- [[Языки программирования/C++/Библиотеки/<semaphore>/try_acquire|try_acquire]] — попытка захвата без ожидания

## Источники

- https://en.cppreference.com/w/cpp/atomic/counting_semaphore/acquire
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<semaphore>/counting_semaphore|Назад]] | [[Языки программирования/C++/Библиотеки/<semaphore>|Содержание]] | [[Языки программирования/C++/Библиотеки/<semaphore>/release|Вперёд]]
