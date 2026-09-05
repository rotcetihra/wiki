# arrival_token

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<barrier>|<barrier>]] / arrival_token

[[Языки программирования/C++/Библиотеки/<barrier>/barrier|Назад]] | [[Языки программирования/C++/Библиотеки/<barrier>|Содержание]] | [[Языки программирования/C++/Библиотеки/<barrier>/arrive_and_wait|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <barrier>

class arrival_token;
```

## Описание

`std::barrier::arrival_token` — тип токена прибытия, получаемый от `barrier::arrive()`. Позволяет отложить прохождение барьера на другом потоке.

## Методы

| Метод | Описание |
|---|---|
| `arrival_token(const arrival_token&)` | Копирующий конструктор (не available) |
| `arrival_token(arrival_token&&)` | Перемещающий конструктор |

## Примеры

```cpp
#include <barrier>
#include <iostream>

int main()
{
    std::barrier b(2);

    auto token = b.arrive();
    // token можно передать другому потоку для завершения
    b.arrive_and_wait();
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<barrier>/barrier|barrier]] — барьер синхронизации

## Источники

- https://en.cppreference.com/w/cpp/thread/barrier/arrival_token
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<barrier>/barrier|Назад]] | [[Языки программирования/C++/Библиотеки/<barrier>|Содержание]] | [[Языки программирования/C++/Библиотеки/<barrier>/arrive_and_wait|Вперёд]]
