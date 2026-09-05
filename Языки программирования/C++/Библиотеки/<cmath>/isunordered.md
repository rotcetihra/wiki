# isunordered

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<cmath>|<cmath>]] / isunordered

[[Языки программирования/C++/Библиотеки/<cmath>/islessgreater|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <cmath>

bool isunordered(float x, float y);
bool isunordered(double x, double y);
bool isunordered(long double x, long double y);
```

## Параметры

| Параметр | Описание |
|---|---|
| `x` | Левый операнд |
| `y` | Правый операнд |

## Возвращаемое значение

`true`, если хотя бы один из аргументов — NaN.

## Что делает

Проверяет, являются ли аргументы неупорядоченными (хотя бы один — NaN).

## Примеры

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << std::isunordered(NAN, 1.0) << std::endl;  // 1
    std::cout << std::isunordered(1.0, 2.0) << std::endl;  // 0
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<cmath>/isnan|isnan]] — проверка на NaN

## Источники

- https://en.cppreference.com/w/cpp/numeric/math/isunordered
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<cmath>/islessgreater|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>|Вперёд]]
