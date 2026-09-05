# fgetpos

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] / fgetpos

[[Языки программирования/C++/Библиотеки/cstdio/fwrite|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fseek|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdio>
int fgetpos(FILE *stream, fpos_t *pos);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `stream` | Stream |
| `pos` | Position |

## Vozvrashaemoe znachenie

0 or nonzero.

## Chto delaet

Gets position.

## Primery

### Bazovoe

```cpp
#include <cstdio>
#include <iostream>
int main() { /* fgetpos */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdio
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdio/fwrite|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fseek|Vperyod]]
