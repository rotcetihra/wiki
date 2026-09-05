# time_point_cast

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<chrono>|<chrono>]] / time_point_cast

[[Языки программирования/C++/Библиотеки/<chrono>/duration_cast|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/hours|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <chrono>

template<class ToDuration, class Clock, class Duration>
constexpr time_point<Clock, ToDuration>
    time_point_cast(const time_point<Clock, Duration>& pt);
```

## Параметры

| Параметр | Описание |
|---|---|
| `pt` | Момент времени для преобразования |

## Возвращаемое значение

Момент времени типа `time_point<Clock, ToDuration>`.

## Что делает

Преобразует момент времени с усечением до другой точности.

## Примеры

```cpp
#include <chrono>
#include <iostream>

int main()
{
    auto now = std::chrono::system_clock::now();
    auto sec = std::chrono::time_point_cast<std::chrono::seconds>(now);

    std::cout << sec.time_since_epoch().count() << std::endl; // секунды с эпохи
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<chrono>/duration_cast|duration_cast]] — преобразование интервалов

## Источники

- https://en.cppreference.com/w/cpp/chrono/time_point_cast
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<chrono>/duration_cast|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/hours|Вперёд]]
