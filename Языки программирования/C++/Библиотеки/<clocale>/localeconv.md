# localeconv

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<clocale>/clocale|clocale]] / localeconv

[[Языки программирования/C++/Библиотеки/clocale/setlocale|Nazad]] | [[Языки программирования/C++/Библиотеки/<clocale>/clocale|clocale]] | [[Языки программирования/C++/Библиотеки/clocale/|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <clocale>
struct lconv *localeconv(void);
```

## Parametry

| Parametr | Opisanie |
|---|---|

## Vozvrashaemoe znachenie

Pointer to lconv.

## Chto delaet

Gets locale info.

## Primery

### Bazovoe

```cpp
#include <clocale>
#include <iostream>
int main() { struct lconv *lc = std::localeconv(); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<clocale>/clocale|clocale]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/clocale
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/clocale/setlocale|Nazad]] | [[Языки программирования/C++/Библиотеки/<clocale>/clocale|clocale]] | [[Языки программирования/C++/Библиотеки/clocale/|Vperyod]]
