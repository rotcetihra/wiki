# duration_cast

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<chrono>|<chrono>]] / duration_cast

[[Языки программирования/C++/Библиотеки/<chrono>/now|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/time_point_cast|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <chrono>

template<class ToDuration, class Rep, class Period>
constexpr ToDuration duration_cast(const duration<Rep, Period>& d);
```

## Параметры

| Параметр | Описание |
|---|---|
| `d` | Длительность для преобразования |

## Возвращаемое значение

Длительность типа `ToDuration`.

## Что делает

Преобразует длительность из одного типа в другой с усечением (без округления).

## Примеры

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::chrono::milliseconds ms(1500);

    auto sec = std::chrono::duration_cast<std::chrono::seconds>(ms);
    std::cout << sec.count() << std::endl; // 1 (усечение)

    auto min = std::chrono::duration_cast<std::chrono::minutes>(ms);
    std::cout << min.count() << std::endl; // 0
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<chrono>/duration|duration]] — временной интервал

## Источники

- https://en.cppreference.com/w/cpp/chrono/duration_cast
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<chrono>/now|Назад]] | [[Языки программирования/C++/Библиотеки/<chrono>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>/time_point_cast|Вперёд]]
