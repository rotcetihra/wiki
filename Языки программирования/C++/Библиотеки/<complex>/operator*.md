# operator*

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<complex>|<complex>]] / operator*

[[Языки программирования/C++/Библиотеки/<complex>/operator-|Назад]] | [[Языки программирования/C++/Библиотеки/<complex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<complex>/operator/|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <complex>

template<class T>
complex<T> operator*(const complex<T>& lhs, const complex<T>& rhs);
template<class T>
complex<T> operator*(const T& lhs, const complex<T>& rhs);
template<class T>
complex<T> operator*(const complex<T>& lhs, const T& rhs);
```

## Параметры

| Параметр | Описание |
|---|---|
| `lhs` | Левый операнд |
| `rhs` | Правый операнд |

## Возвращаемое значение

Произведение двух комплексных чисел по формуле `(a+bi)(c+di) = (ac−bd) + (ad+bc)i`.

## Что делает

Умножает два комплексных числа или комплексное число на скаляр.

## Примеры

```cpp
#include <complex>
#include <iostream>

int main()
{
    std::complex<double> z1(3.0, 4.0);
    std::complex<double> z2(1.0, -2.0);
    std::cout << z1 * z2 << std::endl; // (11,-2)
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<complex>/operator/|operator/]] — деление

## Источники

- https://en.cppreference.com/w/cpp/numeric/complex/operator*
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<complex>/operator-|Назад]] | [[Языки программирования/C++/Библиотеки/<complex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<complex>/operator/|Вперёд]]
