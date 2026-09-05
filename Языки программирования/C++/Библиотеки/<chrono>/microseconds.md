# microseconds

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<chrono>|<chrono>]] / microseconds

[[Языки программирования/C++/Библиотеки/<chrono>/milliseconds|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/nanoseconds|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <chrono>

using microseconds = std::chrono::duration</*signed integer type of at least 55 bits*/, std::micro>;
```

## Описание

Тип длительности, представляющий микросекунды.

## Примеры

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::chrono::microseconds us(5000);
    std::cout << us.count() << std::endl; // 5000

    auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(us);
    std::cout << ms.count() << std::endl; // 5
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<chrono>/nanoseconds|nanoseconds]] — наносекунды

## Источники

- https://en.cppreference.com/w/cpp/chrono/duration
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<chrono>/milliseconds|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/nanoseconds|Вперёд]]
