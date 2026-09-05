# nanoseconds

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<chrono>|<chrono>]] / nanoseconds

[[Языки программирования/C++/Библиотеки/<chrono>/microseconds|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <chrono>

using nanoseconds = std::chrono::duration</*signed integer type of at least 64 bits*/, std::nano>;
```

## Описание

Тип длительности, представляющий наносекунды.

## Примеры

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::chrono::nanoseconds ns(1000000);
    std::cout << ns.count() << std::endl; // 1000000

    auto us = std::chrono::duration_cast<std::chrono::microseconds>(ns);
    std::cout << us.count() << std::endl; // 1000
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<chrono>/microseconds|microseconds]] — микросекунды

## Источники

- https://en.cppreference.com/w/cpp/chrono/duration
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<chrono>/microseconds|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<compare>|Вперёд]]
