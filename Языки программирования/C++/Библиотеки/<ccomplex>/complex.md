# complex

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<ccomplex>/ccomplex|ccomplex]] / complex

[[Языки программирования/C++/Библиотеки/ccomplex/|Nazad]] | [[Языки программирования/C++/Библиотеки/<ccomplex>/ccomplex|ccomplex]] | [[Языки программирования/C++/Библиотеки/ccomplex/|Vperyod]]

**Дата написания:** 05.09.2026

## Opredelenie

```cpp
#include <ccomplex>
typedef struct { double real; double imag; } complex;
```

## Opisanie

Обёртка над C `complex`.

## Primery

### Bazovoe

```cpp
#include <complex>
#include <iostream>

int main() {
    std::complex<double> z(1.0, 2.0);
    std::cout << z << "\n";
    return 0;
}
```

## Iskljuchenija

- Tipy ne brosayut iskljuchenij.

## Pohozhie jelementy

- [[Языки программирования/C++/Библиотеки/<ccomplex>/ccomplex|ccomplex]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/ccomplex
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/ccomplex/|Nazad]] | [[Языки программирования/C++/Библиотеки/<ccomplex>/ccomplex|ccomplex]] | [[Языки программирования/C++/Библиотеки/ccomplex/|Vperyod]]
