# ERANGE

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cerrno>/cerrno|cerrno]] / ERANGE

[[Языки программирования/C++/Библиотеки/cerrno/EILSEQ|Nazad]] | [[Языки программирования/C++/Библиотеки/<cerrno>/cerrno|cerrno]] | [[Языки программирования/C++/Библиотеки/cerrno/|Vperyod]]

**Дата написания:** 05.09.2026

## Opredelenie

```cpp
#include <cerrno>
#define ERANGE
```

## Opisanie

Range error.

## Primery

### Bazovoe

```cpp
#include <cerrno>
#include <cmath>
int main() { errno = 0; std::pow(10.0, 1000.0); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie jelementy

- [[Языки программирования/C++/Библиотеки/<cerrno>/cerrno|cerrno]]
- [[Языки программирования/C++/Библиотеки/<cerrno>/errno|errno]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cerrno
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cerrno/EILSEQ|Nazad]] | [[Языки программирования/C++/Библиотеки/<cerrno>/cerrno|cerrno]] | [[Языки программирования/C++/Библиотеки/cerrno/|Vperyod]]
