# operator-

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<complex>|<complex>]] / operator-

[[Языки программирования/C++/Библиотеки/<complex>/operator+|Назад]] | [[Языки программирования/C++/Библиотеки/<complex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<complex>/operator*|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <complex>

template<class T>
complex<T> operator-(const complex<T>& lhs, const complex<T>& rhs);
template<class T>
complex<T> operator-(const T& lhs, const complex<T>& rhs);
template<class T>
complex<T> operator-(const complex<T>& lhs, const T& rhs);
template<class T>
complex<T> operator-(const complex<T>& v); // унарный минус
```

## Параметры

| Параметр | Описание |
|---|---|
| `lhs` | Левый операнд |
| `rhs` | Правый операнд |
| `v` | Комплексное число (унарный минус) |

## Возвращаемое значение

Результат вычитания или унарного отрицания.

## Что делает

Вычитает одно комплексное число из другого или комплексное число из скаляра. Унарный минус возвращает `complex(-real(v), -imag(v))`.

## Примеры

```cpp
#include <complex>
#include <iostream>

int main()
{
    std::complex<double> z1(3.0, 4.0);
    std::complex<double> z2(1.0, -2.0);
    std::cout << z1 - z2 << std::endl;  // (2,6)
    std::cout << -z1 << std::endl;       // (-3,-4)
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<complex>/operator+|operator+]] — сложение

## Источники

- https://en.cppreference.com/w/cpp/numeric/complex/operator-
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<complex>/operator+|Назад]] | [[Языки программирования/C++/Библиотеки/<complex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<complex>/operator*|Вперёд]]
