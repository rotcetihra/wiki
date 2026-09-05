# asctime

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] / asctime

[[Языки программирования/C++/Библиотеки/ctime/tm|Nazad]] | [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] | [[Языки программирования/C++/Библиотеки/ctime/clock|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <ctime>
char *asctime(const struct tm *timeptr);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `timeptr` | Pointer to tm |

## Vozvrashaemoe znachenie

Pointer to string.

## Chto delaet

Converts tm to string.

## Primery

### Bazovoe

```cpp
#include <ctime>
#include <iostream>
int main() { /* asctime */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/ctime
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/ctime/tm|Nazad]] | [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] | [[Языки программирования/C++/Библиотеки/ctime/clock|Vperyod]]
