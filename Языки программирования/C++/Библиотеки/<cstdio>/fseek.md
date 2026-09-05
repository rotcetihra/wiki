# fseek

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] / fseek

[[Языки программирования/C++/Библиотеки/cstdio/fgetpos|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fsetpos|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdio>
int fseek(FILE *stream, long offset, int whence);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `stream` | Stream |
| `offset` | Offset |
| `whence` | SEEK_* |

## Vozvrashaemoe znachenie

0 or nonzero.

## Chto delaet

Sets position.

## Primery

### Bazovoe

```cpp
#include <cstdio>
#include <iostream>
int main() { /* fseek */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdio
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdio/fgetpos|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fsetpos|Vperyod]]
