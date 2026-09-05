# ratio_less_equal

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<ratio>|<ratio>]] / ratio_less_equal

[[Языки программирования/C++/Библиотеки/<ratio>/ratio_less|Назад]] | [[Языки программирования/C++/Библиотеки/<ratio>|Содержание]] | [[Языки программирования/C++/Библиотеки/<ratio>/ratio_greater|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <ratio>

template<class R1, class R2>
struct ratio_less_equal;
```

## Параметры

| Параметр | Описание |
|---|---|
| `R1` | Первый операнд |
| `R2` | Второй операнд |

## Возвращаемое значение

`std::true_type`, если `R1 <= R2`.

## Что делает

Проверяет, меньше или равна ли первая рациональная константа второй.

## Примеры

```cpp
#include <ratio>
#include <iostream>

int main()
{
    using r1 = std::ratio<1, 2>;
    using r2 = std::ratio<1, 2>;
    std::cout << std::ratio_less_equal<r1, r2>::value << std::endl; // 1
}
```

## Исключения

- **Исключения:** операция времени компиляции.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<ratio>/ratio_greater_equal|ratio_greater_equal]] — больше или равно

## Источники

- https://en.cppreference.com/w/cpp/numeric/ratio/ratio_less_equal
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<ratio>/ratio_less|Назад]] | [[Языки программирования/C++/Библиотеки/<ratio>|Содержание]] | [[Языки программирования/C++/Библиотеки/<ratio>/ratio_greater|Вперёд]]
