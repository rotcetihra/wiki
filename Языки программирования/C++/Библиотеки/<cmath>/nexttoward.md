# nexttoward

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<cmath>|<cmath>]] / nexttoward

[[Языки программирования/C++/Библиотеки/<cmath>/nextafter|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/exp|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <cmath>

float nexttoward(float from, long double to);
double nexttoward(double from, long double to);
long double nexttoward(long double from, long double to);
```

## Параметры

| Параметр | Описание |
|---|---|
| `from` | Исходное значение |
| `to` | Направление типа `long double` |

## Возвращаемое значение

Ближайшее representable значение к `from` в направлении `to`.

## Что делает

Аналог `nextafter`, но с направлением типа `long double`. Позволяет работать с разными типами.

## Примеры

```cpp
#include <cmath>
#include <iostream>

int main()
{
    double x = 1.0;
    double next = std::nexttoward(x, 2.0L);
    std::cout << std::hexfloat << x << " → " << next << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<cmath>/nextafter|nextafter]] — направление того же типа

## Источники

- https://en.cppreference.com/w/cpp/numeric/math/nexttoward
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<cmath>/nextafter|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/exp|Вперёд]]
