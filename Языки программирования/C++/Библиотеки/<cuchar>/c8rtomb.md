# c8rtomb

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] / c8rtomb

[[Языки программирования/C++/Библиотеки/cuchar/mbrtoc8|Nazad]] | [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] | [[Языки программирования/C++/Библиотеки/cuchar/|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cuchar>
size_t c8rtomb(char *s, char8_t c8, mbstate_t *ps);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s` | Dest |
| `c8` | Char |
| `ps` | State |

## Vozvrashaemoe znachenie

Bytes written.

## Chto delaet

char8_t to multibyte.

## Primery

### Bazovoe

```cpp
#include <cuchar>
#include <iostream>
int main() { /* c8rtomb */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cuchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cuchar/mbrtoc8|Nazad]] | [[Языки программирования/C++/Библиотеки/<cuchar>/cuchar|cuchar]] | [[Языки программирования/C++/Библиотеки/cuchar/|Vperyod]]
