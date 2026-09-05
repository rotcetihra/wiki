# mktime

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] / mktime

[[Языки программирования/C++/Библиотеки/ctime/localtime|Nazad]] | [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] | [[Языки программирования/C++/Библиотеки/ctime/strftime|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <ctime>
time_t mktime(struct tm *timeptr);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `timeptr` | Pointer to tm |

## Vozvrashaemoe znachenie

time_t value.

## Chto delaet

Converts tm to time_t.

## Primery

### Bazovoe

```cpp
#include <ctime>
#include <iostream>
int main() { /* mktime */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/ctime
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/ctime/localtime|Nazad]] | [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] | [[Языки программирования/C++/Библиотеки/ctime/strftime|Vperyod]]
