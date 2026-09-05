# operator==

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<complex>|<complex>]] / operator==

[[Языки программирования/C++/Библиотеки/<complex>/operator/|Назад]] | [[Языки программирования/C++/Библиотеки/<complex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<complex>/operator!=|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <complex>

template<class T>
bool operator==(const complex<T>& lhs, const complex<T>& rhs);
```

## Параметры

| Параметр | Описание |
|---|---|
| `lhs` | Левый операнд |
| `rhs` | Правый операнд |

## Возвращаемое значение

`true`, если `real(lhs) == real(rhs) && imag(lhs) == imag(rhs)`.

## Что делает

Проверяет два комплексных числа на равенство поэлементно.

## Примеры

```cpp
#include <complex>
#include <iostream>

int main()
{
    std::complex<double> z1(3.0, 4.0);
    std::complex<double> z2(3.0, 4.0);
    std::cout << std::boolalpha << (z1 == z2) << std::endl; // true
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<complex>/operator!=|operator!=]] — проверка неравенства

## Источники

- https://en.cppreference.com/w/cpp/numeric/complex/operator_cmp
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<complex>/operator/|Назад]] | [[Языки программирования/C++/Библиотеки/<complex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<complex>/operator!=|Вперёд]]
