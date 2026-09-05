# memcmp

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstring>/cstring|cstring]] / memcmp

[[Языки программирования/C++/Библиотеки/cstring/memchr|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstring>/cstring|cstring]] | [[Языки программирования/C++/Библиотеки/cstring/memcpy|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstring>
int memcmp(const void *s1, const void *s2, size_t n);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s1` | Ptr1 |
| `s2` | Ptr2 |
| `n` | Count |

## Vozvrashaemoe znachenie

Negative, 0, positive.

## Chto delaet

Compares blocks.

## Primery

### Bazovoe

```cpp
#include <cstring>
#include <iostream>
int main() { /* memcmp */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstring>/cstring|cstring]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstring
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstring/memchr|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstring>/cstring|cstring]] | [[Языки программирования/C++/Библиотеки/cstring/memcpy|Vperyod]]
