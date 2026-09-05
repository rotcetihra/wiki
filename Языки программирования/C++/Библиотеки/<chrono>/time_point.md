# time_point

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<chrono>|<chrono>]] / time_point

[[Языки программирования/C++/Библиотеки/<chrono>/duration|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/system_clock|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <chrono>

template<class Clock, class Duration = typename Clock::duration>
class time_point;
```

## Описание

Представляет конкретный момент времени, привязанный к определённым часам (`Clock`).

## Конструкторы

| Конструктор | Описание |
|---|---|
| `time_point()` | Текущее время часов |
| `time_point(const Duration& d)` | Время с момента эпохи часов |

## Методы

| Метод | Описание |
|---|---|
| `time_since_epoch()` | Время с момента эпохи |
| `floor<Duration>()` | Округление вниз |
| `ceil<Duration>()` | Округление вверх |
| `round<Duration>()` | Округление к ближайшему |
| `operator+`, `operator-` | Арифметика |

## Примеры

```cpp
#include <chrono>
#include <iostream>

int main()
{
    auto now = std::chrono::system_clock::now();
    auto epoch = now.time_since_epoch();

    std::cout << std::chrono::duration_cast<std::chrono::seconds>(epoch).count()
              << std::endl; // секунды с эпохи
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<chrono>/now|now]] — текущее время

## Источники

- https://en.cppreference.com/w/cpp/chrono/time_point
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<chrono>/duration|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/system_clock|Вперёд]]
