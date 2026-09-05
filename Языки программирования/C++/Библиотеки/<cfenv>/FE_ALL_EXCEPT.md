# FE_ALL_EXCEPT

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] / FE_ALL_EXCEPT

[[Языки программирования/C++/Библиотеки/cfenv/|Nazad]] | [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] | [[Языки программирования/C++/Библиотеки/cfenv/FE_DOWNWARD|Vperyod]]

**Дата написания:** 05.09.2026

## Opredelenie

```cpp
#include <cfenv>
#define FE_ALL_EXCEPT (FE_DIVBYZERO|FE_INEXACT|FE_INVALID|FE_OVERFLOW|FE_UNDERFLOW)
```

## Opisanie

All exceptions mask.

## Primery

### Bazovoe

```cpp
#include <cfenv>
#include <iostream>
int main() { std::cout << FE_ALL_EXCEPT; }
```

## Iskljuchenija

- No exceptions.

## Pohozhie jelementy

- [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cfenv
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cfenv/|Nazad]] | [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] | [[Языки программирования/C++/Библиотеки/cfenv/FE_DOWNWARD|Vperyod]]
