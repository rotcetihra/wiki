# ratio_greater

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<ratio>|<ratio>]] / ratio_greater

[[Языки программирования/C++/Библиотеки/<ratio>/ratio_less_equal|Назад]] | [[Языки программирования/C++/Библиотеки/<ratio>|Содержание]] | [[Языки программирования/C++/Библиотеки/<ratio>/ratio_greater_equal|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <ratio>

template<class R1, class R2>
struct ratio_greater;
```

## Параметры

| Параметр | Описание |
|---|---|
| `R1` | Первый операнд |
| `R2` | Второй операнд |

## Возвращаемое значение

`std::true_type`, если `R1 > R2`.

## Что делает

Проверяет, больше ли первая рациональная константа второй.

## Примеры

```cpp
#include <ratio>
#include <iostream>

int main()
{
    using r1 = std::ratio<3, 4>;
    using r2 = std::ratio<1, 2>;
    std::cout << std::ratio_greater<r1, r2>::value << std::endl; // 1
}
```

## Исключения

- **Исключения:** операция времени компиляции.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<ratio>/ratio_less|ratio_less]] — меньше

## Источники

- https://en.cppreference.com/w/cpp/numeric/ratio/ratio_greater
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<ratio>/ratio_less_equal|Назад]] | [[Языки программирования/C++/Библиотеки/<ratio>|Содержание]] | [[Языки программирования/C++/Библиотеки/<ratio>/ratio_greater_equal|Вперёд]]
