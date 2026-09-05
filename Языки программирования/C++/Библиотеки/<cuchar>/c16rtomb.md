# c16rtomb

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] / c16rtomb

[[Языки программирования/C++/Библиотеки/cuchar/mbrtoc32|Nazad]] | [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] | [[Языки программирования/C++/Библиотеки/cuchar/c32rtomb|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cuchar>
size_t c16rtomb(char *s, char16_t c16, mbstate_t *ps);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s` | Dest |
| `c16` | Char |
| `ps` | State |

## Vozvrashaemoe znachenie

Bytes written.

## Chto delaet

char16_t to multibyte.

## Primery

### Bazovoe

```cpp
#include <cuchar>
#include <iostream>
int main() { /* c16rtomb */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cuchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cuchar/mbrtoc32|Nazad]] | [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] | [[Языки программирования/C++/Библиотеки/cuchar/c32rtomb|Vperyod]]
