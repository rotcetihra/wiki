# fgets

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] / fgets

[[Языки программирования/C++/Библиотеки/cstdio/fgetc|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fputc|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdio>
char *fgets(char *str, int n, FILE *stream);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `str` | Buffer |
| `n` | Max |
| `stream` | Stream |

## Vozvrashaemoe znachenie

Pointer or NULL.

## Chto delaet

Reads line.

## Primery

### Bazovoe

```cpp
#include <cstdio>
#include <iostream>
int main() { /* fgets */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdio
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdio/fgetc|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fputc|Vperyod]]
