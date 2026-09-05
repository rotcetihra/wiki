# duration

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<chrono>|<chrono>]] / duration

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/time_point|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <chrono>

template<class Rep, class Period = std::ratio<1>>
class duration;
```

## Описание

Шаблон `std::duration` представляет временной интервал. `Rep` — тип представления (по умолчанию `double`), `Period` — отношение единицы времени к секунде.

## Конструкторы

| Конструктор | Описание |
|---|---|
| `duration()` | Значение по умолчанию (0) |
| `duration(const Rep& rep)` | Из числового значения |
| `duration(const duration& other)` | Копирующий конструктор |

## Методы

| Метод | Описание |
|---|---|
| `count()` | Возвращает числовое значение |
| `zero()` | Нулевая длительность |
| `min()` | Минимальная длительность |
| `max()` | Максимальная длительность |

## Примеры

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::chrono::seconds s(42);
    std::cout << s.count() << std::endl; // 42

    std::chrono::milliseconds ms = std::chrono::seconds(2);
    std::cout << ms.count() << std::endl; // 2000

    auto d = std::chrono::hours(1) + std::chrono::minutes(30);
    std::cout << std::chrono::duration_cast<std::chrono::minutes>(d).count()
              << std::endl; // 90
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<chrono>/duration_cast|duration_cast]] — преобразование интервалов

## Источники

- https://en.cppreference.com/w/cpp/chrono/duration
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/time_point|Вперёд]]
