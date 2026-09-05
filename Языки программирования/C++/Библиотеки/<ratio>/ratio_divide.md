# ratio_divide

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<ratio>|<ratio>]] / ratio_divide

[[Языки программирования/C++/Библиотеки/<ratio>/ratio_multiply|Назад]] | [[Языки программирования/C++/Библиотеки/<ratio>|Содержание]] | [[Языки программирования/C++/Библиотеки/<ratio>/ratio_equal|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <ratio>

template<class R1, class R2>
using ratio_divide = /* typename */;
```

## Параметры

| Параметр | Описание |
|---|---|
| `R1` | Делимое |
| `R2` | Делитель |

## Возвращаемое значение

Новый тип `std::ratio`, представляющий частное `R1 / R2`.

## Что делает

Делит одну рациональную константу на другую.

## Примеры

```cpp
#include <ratio>
#include <iostream>

int main()
{
    using r1 = std::ratio<1, 2>;
    using r2 = std::ratio<1, 4>;
    using quot = std::ratio_divide<r1, r2>;
    std::cout << quot::num << "/" << quot::den << std::endl; // 2/1
}
```

## Исключения

- **Исключения:** операция времени компиляции.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<ratio>/ratio_multiply|ratio_multiply]] — умножение

## Источники

- https://en.cppreference.com/w/cpp/numeric/ratio/ratio_divide
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<ratio>/ratio_multiply|Назад]] | [[Языки программирования/C++/Библиотеки/<ratio>|Содержание]] | [[Языки программирования/C++/Библиотеки/<ratio>/ratio_equal|Вперёд]]
