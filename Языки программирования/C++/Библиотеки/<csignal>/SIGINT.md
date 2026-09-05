# SIGINT

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<csignal>/csignal|csignal]] / SIGINT

[[Языки программирования/C++/Библиотеки/csignal/|Nazad]] | [[Языки программирования/C++/Библиотеки/<csignal>/csignal|csignal]] | [[Языки программирования/C++/Библиотеки/csignal/SIGSEGV|Vperyod]]

**Дата написания:** 05.09.2026

## Opredelenie

```cpp
#include <csignal>
#define SIGINT
```

## Opisanie



## Primery

### Bazovoe

```cpp
#include <csignal>
#include <iostream>
int main() { std::signal(SIGINT, 0); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie jelementy

- [[Языки программирования/C++/Библиотеки/<csignal>/csignal|csignal]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/csignal
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/csignal/|Nazad]] | [[Языки программирования/C++/Библиотеки/<csignal>/csignal|csignal]] | [[Языки программирования/C++/Библиотеки/csignal/SIGSEGV|Vperyod]]
