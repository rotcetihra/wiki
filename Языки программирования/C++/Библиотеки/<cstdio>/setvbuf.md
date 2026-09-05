# setvbuf

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] / setvbuf

[[Языки программирования/C++/Библиотеки/cstdio/setbuf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fprintf|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdio>
int setvbuf(FILE *stream, char *buf, int mode, size_t size);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `stream` | Stream |
| `buf` | Buffer |
| `mode` | Mode |
| `size` | Size |

## Vozvrashaemoe znachenie

0 or nonzero.

## Chto delaet

Sets buffer with options.

## Primery

### Bazovoe

```cpp
#include <cstdio>
#include <iostream>
int main() { /* setvbuf */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdio
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdio/setbuf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fprintf|Vperyod]]
