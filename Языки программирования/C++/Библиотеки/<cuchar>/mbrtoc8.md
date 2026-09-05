# mbrtoc8

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] / mbrtoc8

[[Языки программирования/C++/Библиотеки/cuchar/c32rtomb|Nazad]] | [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] | [[Языки программирования/C++/Библиотеки/cuchar/c8rtomb|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cuchar>
size_t mbrtoc8(char *pc8, const char *s, size_t n, mbstate_t *ps);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `pc8` | Dest |
| `s` | Source |
| `n` | Max |
| `ps` | State |

## Vozvrashaemoe znachenie

Bytes consumed.

## Chto delaet

Multibyte to char8_t.

## Primery

### Bazovoe

```cpp
#include <cuchar>
#include <iostream>
int main() { /* mbrtoc8 */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cuchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cuchar/c32rtomb|Nazad]] | [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] | [[Языки программирования/C++/Библиотеки/cuchar/c8rtomb|Vperyod]]
