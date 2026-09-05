# pow

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<complex>|<complex>]] / pow

[[Языки программирования/C++/Библиотеки/<complex>/log10|Назад]] | [[Языки программирования/C++/Библиотеки/<complex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<complex>/sqrt|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <complex>

template<class T>
complex<T> pow(const complex<T>& base, const complex<T>& exp);
template<class T>
complex<T> pow(const complex<T>& base, const T& exp);
template<class T>
complex<T> pow(const T& base, const complex<T>& exp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `base` | Основание |
| `exp` | Показатель степени |

## Возвращаемое значение

Комплексное число `base` в степени `exp`: `exp(exp * log(base))`.

## Что делает

Возводит комплексное число в комплексную или вещественную степень.

## Примеры

```cpp
#include <complex>
#include <iostream>

int main()
{
    std::complex<double> z(0.0, 1.0);
    std::cout << std::pow(z, 2) << std::endl; // (-1,0)
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<complex>/sqrt|sqrt]] — квадратный корень

## Источники

- https://en.cppreference.com/w/cpp/numeric/complex/pow
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<complex>/log10|Назад]] | [[Языки программирования/C++/Библиотеки/<complex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<complex>/sqrt|Вперёд]]
