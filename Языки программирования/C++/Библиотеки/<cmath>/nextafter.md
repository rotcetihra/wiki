# nextafter

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<cmath>|<cmath>]] / nextafter

[[Языки программирования/C++/Библиотеки/<cmath>/nan|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/nexttoward|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <cmath>

float nextafter(float from, float to);
double nextafter(double from, double to);
long double nextafter(long double from, long double to);
```

## Параметры

| Параметр | Описание |
|---|---|
| `from` | Исходное значение |
| `to` | Направление |

## Возвращаемое значение

Ближайшее representable значение к `from` в направлении `to`.

## Что делает

Возвращает следующее representable значение в направлении от `from` к `to`. Если `from == to`, возвращает `from`.

## Примеры

```cpp
#include <cmath>
#include <iostream>

int main()
{
    double x = 1.0;
    double next = std::nextafter(x, 2.0);
    std::cout << std::hexfloat << x << " → " << next << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<cmath>/nexttoward|nexttoward]] — направление `long double`

## Источники

- https://en.cppreference.com/w/cpp/numeric/math/nextafter
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<cmath>/nan|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/nexttoward|Вперёд]]
