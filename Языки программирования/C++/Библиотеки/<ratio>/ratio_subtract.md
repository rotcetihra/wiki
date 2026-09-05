# ratio_subtract

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<ratio>|<ratio>]] / ratio_subtract

[[Языки программирования/C++/Библиотеки/<ratio>/ratio_add|Назад]] | [[Языки программирования/C++/Библиотеки/<ratio>|Содержание]] | [[Языки программирования/C++/Библиотеки/<ratio>/ratio_multiply|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <ratio>

template<class R1, class R2>
using ratio_subtract = /* typename */;
```

## Параметры

| Параметр | Описание |
|---|---|
| `R1` | Уменьшаемое |
| `R2` | Вычитаемое |

## Возвращаемое значение

Новый тип `std::ratio`, представляющий разность `R1 - R2`.

## Что делает

Вычитает одну рациональную константу из другой.

## Примеры

```cpp
#include <ratio>
#include <iostream>

int main()
{
    using r1 = std::ratio<1, 2>;
    using r2 = std::ratio<1, 4>;
    using diff = std::ratio_subtract<r1, r2>;
    std::cout << diff::num << "/" << diff::den << std::endl; // 1/4
}
```

## Исключения

- **Исключения:** операция времени компиляции.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<ratio>/ratio_add|ratio_add]] — сложение

## Источники

- https://en.cppreference.com/w/cpp/numeric/ratio/ratio_subtract
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<ratio>/ratio_add|Назад]] | [[Языки программирования/C++/Библиотеки/<ratio>|Содержание]] | [[Языки программирования/C++/Библиотеки/<ratio>/ratio_multiply|Вперёд]]
