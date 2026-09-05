# localtime

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] / localtime

[[Языки программирования/C++/Библиотеки/ctime/gmtime|Nazad]] | [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] | [[Языки программирования/C++/Библиотеки/ctime/mktime|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <ctime>
struct tm *localtime(const time_t *timer);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `timer` | Pointer to time_t |

## Vozvrashaemoe znachenie

Pointer to tm (local).

## Chto delaet

Converts to local time.

## Primery

### Bazovoe

```cpp
#include <ctime>
#include <iostream>
int main() { /* localtime */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/ctime
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/ctime/gmtime|Nazad]] | [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] | [[Языки программирования/C++/Библиотеки/ctime/mktime|Vperyod]]
