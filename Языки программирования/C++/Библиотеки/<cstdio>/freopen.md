# freopen

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] / freopen

[[Языки программирования/C++/Библиотеки/cstdio/fopen|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/setbuf|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdio>
FILE *freopen(const char *f, const char *mode, FILE *stream);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `f` | File |
| `mode` | Mode |
| `stream` | Stream |

## Vozvrashaemoe znachenie

Pointer or NULL.

## Chto delaet

Reopens file.

## Primery

### Bazovoe

```cpp
#include <cstdio>
#include <iostream>
int main() { /* freopen */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdio
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdio/fopen|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/setbuf|Vperyod]]
