# ratio_multiply

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<ratio>|<ratio>]] / ratio_multiply

[[Языки программирования/C++/Библиотеки/<ratio>/ratio_subtract|Назад]] | [[Языки программирования/C++/Библиотеки/<ratio>|Содержание]] | [[Языки программирования/C++/Библиотеки/<ratio>/ratio_divide|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <ratio>

template<class R1, class R2>
using ratio_multiply = /* typename */;
```

## Параметры

| Параметр | Описание |
|---|---|
| `R1` | Первый множитель |
| `R2` | Второй множитель |

## Возвращаемое значение

Новый тип `std::ratio`, представляющий произведение `R1 * R2`.

## Что делает

Умножает две рациональные константы.

## Примеры

```cpp
#include <ratio>
#include <iostream>

int main()
{
    using r1 = std::ratio<2, 3>;
    using r2 = std::ratio<3, 4>;
    using prod = std::ratio_multiply<r1, r2>;
    std::cout << prod::num << "/" << prod::den << std::endl; // 1/2
}
```

## Исключения

- **Исключения:** операция времени компиляции.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<ratio>/ratio_divide|ratio_divide]] — деление

## Источники

- https://en.cppreference.com/w/cpp/numeric/ratio/ratio_multiply
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<ratio>/ratio_subtract|Назад]] | [[Языки программирования/C++/Библиотеки/<ratio>|Содержание]] | [[Языки программирования/C++/Библиотеки/<ratio>/ratio_divide|Вперёд]]
