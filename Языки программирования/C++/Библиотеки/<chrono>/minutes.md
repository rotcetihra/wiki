# minutes

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<chrono>|<chrono>]] / minutes

[[Языки программирования/C++/Библиотеки/<chrono>/hours|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/seconds|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <chrono>

using minutes = std::chrono::duration</*signed integer type of at least 29 bits*/, std::ratio<60>>;
```

## Описание

Тип длительности, представляющий минуты.

## Примеры

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::chrono::minutes m(90);
    std::cout << m.count() << std::endl; // 90

    auto h = std::chrono::duration_cast<std::chrono::hours>(m);
    std::cout << h.count() << std::endl; // 1
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<chrono>/hours|hours]] — часы

## Источники

- https://en.cppreference.com/w/cpp/chrono/duration
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<chrono>/hours|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/seconds|Вперёд]]
