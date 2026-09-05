# steady_clock

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<chrono>|<chrono>]] / steady_clock

[[Языки программирования/C++/Библиотеки/<chrono>/system_clock|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/high_resolution_clock|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <chrono>

struct steady_clock;
```

## Описание

Монотонные часы — время никогда не уменьшается. Идеальны для измерения интервалов времени и бенчмарков.

## Методы

| Метод | Описание |
|---|---|
| `now()` | Текущее время |
| `is_steady` | `true` — часы монотонны |

## Примеры

```cpp
#include <chrono>
#include <iostream>

int main()
{
    auto start = std::chrono::steady_clock::now();

    // Нагрузка
    volatile double x = 0;
    for (int i = 0; i < 100000000; ++i)
        x += 1.0;

    auto end = std::chrono::steady_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    std::cout << "Время: " << elapsed.count() << " мс" << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<chrono>/system_clock|system_clock]] — системные часы
- [[Языки программирования/C++/Библиотеки/<chrono>/high_resolution_clock|high_resolution_clock]] — часы максимального разрешения

## Источники

- https://en.cppreference.com/w/cpp/chrono/steady_clock
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<chrono>/system_clock|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/high_resolution_clock|Вперёд]]
