# operator>>

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<complex>|<complex>]] / operator>>

[[Языки программирования/C++/Библиотеки/<complex>/operator<<|Назад]] | [[Языки программирования/C++/Библиотеки/<complex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<complex>/cos|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <complex>

template<class T, class CharT, class Traits>
std::basic_istream<CharT, Traits>&
operator>>(std::basic_istream<CharT, Traits>& is, complex<T>& z);
```

## Параметры

| Параметр | Описание |
|---|---|
| `is` | Входной поток |
| `z` | Комплексное число для чтения |

## Возвращаемое значение

Ссылка на `is`.

## Что делает

Читает комплексное число из потока. Ожидает формат `(real,imag)` или `real`.

## Примеры

```cpp
#include <complex>
#include <iostream>

int main()
{
    std::complex<double> z;
    std::cin >> z; // ввод: (3,4)
    std::cout << z << std::endl; // (3,4)
}
```

## Исключения

- **Исключения:** может установить `failbit` при ошибке чтения.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<complex>/operator<<|operator<<]] — вывод комплексного числа

## Источники

- https://en.cppreference.com/w/cpp/numeric/complex/operator_gtgt
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<complex>/operator<<|Назад]] | [[Языки программирования/C++/Библиотеки/<complex>|Содержание]] | [[Языки программирования/C++/Библиотеки/<complex>/cos|Вперёд]]
