# high_resolution_clock

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<chrono>|<chrono>]] / high_resolution_clock

[[Языки программирования/C++/Библиотеки/<chrono>/steady_clock|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/now|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <chrono>

struct high_resolution_clock;
```

## Описание

Часы с максимально доступным разрешением. Может быть псевдонимом для `system_clock` или `steady_clock`.

## Методы

| Метод | Описание |
|---|---|
| `now()` | Текущее время |
| `is_steady` | Может быть `true` или `false` |

## Примеры

```cpp
#include <chrono>
#include <iostream>

int main()
{
    auto start = std::chrono::high_resolution_clock::now();

    // Нагрузка
    volatile double x = 0;
    for (int i = 0; i < 1000000; ++i)
        x += 1.0;

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
    std::cout << "Время: " << elapsed.count() << " нс" << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<chrono>/steady_clock|steady_clock]] — монотонные часы

## Источники

- https://en.cppreference.com/w/cpp/chrono/high_resolution_clock
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<chrono>/steady_clock|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/now|Вперёд]]
