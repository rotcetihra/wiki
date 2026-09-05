# mbrtoc16

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] / mbrtoc16

[[Языки программирования/C++/Библиотеки/cuchar/size_t|Nazad]] | [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] | [[Языки программирования/C++/Библиотеки/cuchar/mbrtoc32|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cuchar>
size_t mbrtoc16(char16_t *pc16, const char *s, size_t n, mbstate_t *ps);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `pc16` | Dest |
| `s` | Source |
| `n` | Max |
| `ps` | State |

## Vozvrashaemoe znachenie

Bytes consumed.

## Chto delaet

Multibyte to char16_t.

## Primery

### Bazovoe

```cpp
#include <cuchar>
#include <iostream>
int main() { /* mbrtoc16 */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cuchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cuchar/size_t|Nazad]] | [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] | [[Языки программирования/C++/Библиотеки/cuchar/mbrtoc32|Vperyod]]
