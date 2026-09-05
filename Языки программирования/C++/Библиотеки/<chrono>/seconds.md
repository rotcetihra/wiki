# seconds

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<chrono>|<chrono>]] / seconds

[[Языки программирования/C++/Библиотеки/<chrono>/minutes|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/milliseconds|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <chrono>

using seconds = std::chrono::duration</*signed integer type of at least 35 bits*/>;
```

## Описание

Тип длительности, представляющий секунды (по умолчанию `ratio<1>`).

## Примеры

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::chrono::seconds s(65);
    std::cout << s.count() << std::endl; // 65

    auto m = std::chrono::duration_cast<std::chrono::minutes>(s);
    std::cout << m.count() << std::endl; // 1
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<chrono>/milliseconds|milliseconds]] — миллисекунды

## Источники

- https://en.cppreference.com/w/cpp/chrono/duration
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<chrono>/minutes|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/milliseconds|Вперёд]]
