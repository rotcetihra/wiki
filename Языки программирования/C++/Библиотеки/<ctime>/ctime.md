# ctime

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] / ctime

[[Языки программирования/C++/Библиотеки/ctime/clock|Nazad]] | [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] | [[Языки программирования/C++/Библиотеки/ctime/difftime|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <ctime>
char *ctime(const time_t *timer);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `timer` | Pointer to time_t |

## Vozvrashaemoe znachenie

Pointer to string.

## Chto delaet

Converts time_t to string.

## Primery

### Bazovoe

```cpp
#include <ctime>
#include <iostream>
int main() { /* ctime */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/ctime
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/ctime/clock|Nazad]] | [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] | [[Языки программирования/C++/Библиотеки/ctime/difftime|Vperyod]]
