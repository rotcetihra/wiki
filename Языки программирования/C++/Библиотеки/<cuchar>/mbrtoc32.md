# mbrtoc32

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] / mbrtoc32

[[Языки программирования/C++/Библиотеки/cuchar/mbrtoc16|Nazad]] | [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] | [[Языки программирования/C++/Библиотеки/cuchar/c16rtomb|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cuchar>
size_t mbrtoc32(char32_t *pc32, const char *s, size_t n, mbstate_t *ps);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `pc32` | Dest |
| `s` | Source |
| `n` | Max |
| `ps` | State |

## Vozvrashaemoe znachenie

Bytes consumed.

## Chto delaet

Multibyte to char32_t.

## Primery

### Bazovoe

```cpp
#include <cuchar>
#include <iostream>
int main() { /* mbrtoc32 */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cuchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cuchar/mbrtoc16|Nazad]] | [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] | [[Языки программирования/C++/Библиотеки/cuchar/c16rtomb|Vperyod]]
