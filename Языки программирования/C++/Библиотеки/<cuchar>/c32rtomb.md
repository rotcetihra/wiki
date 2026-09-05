# c32rtomb

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] / c32rtomb

[[Языки программирования/C++/Библиотеки/cuchar/c16rtomb|Nazad]] | [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] | [[Языки программирования/C++/Библиотеки/cuchar/mbrtoc8|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cuchar>
size_t c32rtomb(char *s, char32_t c32, mbstate_t *ps);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s` | Dest |
| `c32` | Char |
| `ps` | State |

## Vozvrashaemoe znachenie

Bytes written.

## Chto delaet

char32_t to multibyte.

## Primery

### Bazovoe

```cpp
#include <cuchar>
#include <iostream>
int main() { /* c32rtomb */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cuchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cuchar/c16rtomb|Nazad]] | [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] | [[Языки программирования/C++/Библиотеки/cuchar/mbrtoc8|Vperyod]]
