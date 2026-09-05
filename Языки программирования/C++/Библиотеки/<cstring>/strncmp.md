# strncmp

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstring>/cstring|cstring]] / strncmp

[[Языки программирования/C++/Библиотеки/cstring/strncat|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstring>/cstring|cstring]] | [[Языки программирования/C++/Библиотеки/cstring/strncpy|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstring>
int strncmp(const char *s1, const char *s2, size_t n);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s1` | String1 |
| `s2` | String2 |
| `n` | Max |

## Vozvrashaemoe znachenie

Negative, 0, positive.

## Chto delaet

Compare with limit.

## Primery

### Bazovoe

```cpp
#include <cstring>
#include <iostream>
int main() { /* strncmp */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstring>/cstring|cstring]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstring
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstring/strncat|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstring>/cstring|cstring]] | [[Языки программирования/C++/Библиотеки/cstring/strncpy|Vperyod]]
