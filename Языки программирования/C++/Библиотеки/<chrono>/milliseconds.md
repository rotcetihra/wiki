# milliseconds

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<chrono>|<chrono>]] / milliseconds

[[Языки программирования/C++/Библиотеки/<chrono>/seconds|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/microseconds|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <chrono>

using milliseconds = std::chrono::duration</*signed integer type of at least 45 bits*/, std::milli>;
```

## Описание

Тип длительности, представляющий миллисекунды.

## Примеры

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::chrono::milliseconds ms(1500);
    std::cout << ms.count() << std::endl; // 1500

    auto s = std::chrono::duration_cast<std::chrono::seconds>(ms);
    std::cout << s.count() << std::endl; // 1
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<chrono>/microseconds|microseconds]] — микросекунды

## Источники

- https://en.cppreference.com/w/cpp/chrono/duration
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<chrono>/seconds|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/microseconds|Вперёд]]
