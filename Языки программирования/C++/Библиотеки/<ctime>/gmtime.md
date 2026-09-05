# gmtime

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] / gmtime

[[Языки программирования/C++/Библиотеки/ctime/gmtime|Nazad]] | [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] | [[Языки программирования/C++/Библиотеки/ctime/localtime|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <ctime>
struct tm *gmtime(const time_t *timer);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `timer` | Pointer to time_t |

## Vozvrashaemoe znachenie

Pointer to tm.

## Chto delaet

Converts to UTC.

## Primery

### Bazovoe

```cpp
#include <ctime>
#include <iostream>
int main() { /* gmtime */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/ctime
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/ctime/gmtime|Nazad]] | [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] | [[Языки программирования/C++/Библиотеки/ctime/localtime|Vperyod]]
