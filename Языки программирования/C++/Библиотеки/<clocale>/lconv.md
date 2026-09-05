# lconv

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<clocale>/clocale|clocale]] / lconv

[[Языки программирования/C++/Библиотеки/clocale/|Nazad]] | [[Языки программирования/C++/Библиотеки/<clocale>/clocale|clocale]] | [[Языки программирования/C++/Библиотеки/clocale/setlocale|Vperyod]]

**Дата написания:** 05.09.2026

## Opredelenie

```cpp
#include <clocale>
struct lconv { char *decimal_point; ... };
```

## Opisanie

Localeconv structure.

## Primery

### Bazovoe

```cpp
#include <clocale>
#include <iostream>
int main() { struct lconv *lc = std::localeconv(); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie jelementy

- [[Языки программирования/C++/Библиотеки/<clocale>/clocale|clocale]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/clocale
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/clocale/|Nazad]] | [[Языки программирования/C++/Библиотеки/<clocale>/clocale|clocale]] | [[Языки программирования/C++/Библиотеки/clocale/setlocale|Vperyod]]
