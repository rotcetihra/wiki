# now

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<chrono>|<chrono>]] / now

[[Языки программирования/C++/Библиотеки/<chrono>/high_resolution_clock|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/duration_cast|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <chrono>

static time_point now() noexcept;
```

## Описание

Возвращает текущее время для данного типа часов (`system_clock::now()`, `steady_clock::now()` и т.д.).

## Примеры

```cpp
#include <chrono>
#include <iostream>

int main()
{
    auto now = std::chrono::steady_clock::now();
    auto ns = std::chrono::duration_cast<std::chrono::nanoseconds>(
        now.time_since_epoch()).count();
    std::cout << "Наносекунды с эпохи: " << ns << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений (`noexcept`).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<chrono>/system_clock|system_clock]] — системные часы
- [[Языки программирования/C++/Библиотеки/<chrono>/steady_clock|steady_clock]] — монотонные часы

## Источники

- https://en.cppreference.com/w/cpp/chrono/system_clock/now
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<chrono>/high_resolution_clock|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/duration_cast|Вперёд]]
