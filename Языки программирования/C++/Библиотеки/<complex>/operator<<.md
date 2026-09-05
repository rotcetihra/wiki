# operator<<

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<complex>|<complex>]] / operator<<

[[Языки программирования/C++/Библиотеки/<complex>/operator!=|Назад]] | [[Языки программирования/C++/Библиотеки/<complex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<complex>/operator>>|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <complex>

template<class T, class CharT, class Traits>
std::basic_ostream<CharT, Traits>&
operator<<(std::basic_ostream<CharT, Traits>& os, const complex<T>& z);
```

## Параметры

| Параметр | Описание |
|---|---|
| `os` | Выходной поток |
| `z` | Комплексное число для вывода |

## Возвращаемое значение

Ссылка на `os`.

## Что делает

Выводит комплексное число в формате `(real,imag)`.

## Примеры

```cpp
#include <complex>
#include <iostream>

int main()
{
    std::complex<double> z(3.0, 4.0);
    std::cout << z << std::endl; // (3,4)
}
```

## Исключения

- **Исключения:** может установить `failbit` при ошибке вывода.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<complex>/operator>>|operator>>]] — ввод комплексного числа

## Источники

- https://en.cppreference.com/w/cpp/numeric/complex/operator_ltlt
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<complex>/operator!=|Назад]] | [[Языки программирования/C++/Библиотеки/<complex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<complex>/operator>>|Вперёд]]
