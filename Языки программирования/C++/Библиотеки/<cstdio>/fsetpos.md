# fsetpos

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] / fsetpos

[[Языки программирования/C++/Библиотеки/cstdio/fseek|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/ftell|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdio>
int fsetpos(FILE *stream, const fpos_t *pos);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `stream` | Stream |
| `pos` | Position |

## Vozvrashaemoe znachenie

0 or nonzero.

## Chto delaet

Sets position.

## Primery

### Bazovoe

```cpp
#include <cstdio>
#include <iostream>
int main() { /* fsetpos */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdio
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdio/fseek|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/ftell|Vperyod]]
