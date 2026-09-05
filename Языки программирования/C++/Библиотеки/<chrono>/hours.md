# hours

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<chrono>|<chrono>]] / hours

[[Языки программирования/C++/Библиотеки/<chrono>/time_point_cast|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/minutes|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <chrono>

using hours = std::chrono::duration</*signed integer type of at least 23 bits*/, std::ratio<3600>>;
```

## Описание

Тип длительности, представляющий часы.

## Примеры

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::chrono::hours h(2);
    std::cout << h.count() << std::endl; // 2

    auto mins = std::chrono::duration_cast<std::chrono::minutes>(h);
    std::cout << mins.count() << std::endl; // 120
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<chrono>/duration|duration]] — базовый тип длительности

## Источники

- https://en.cppreference.com/w/cpp/chrono/duration
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<chrono>/time_point_cast|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/minutes|Вперёд]]
