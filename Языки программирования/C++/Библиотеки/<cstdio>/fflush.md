# fflush

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] / fflush

[[Языки программирования/C++/Библиотеки/cstdio/fclose|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fopen|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdio>
int fflush(FILE *stream);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `stream` | Stream or NULL |

## Vozvrashaemoe znachenie

0 or EOF.

## Chto delaet

Flushes buffer.

## Primery

### Bazovoe

```cpp
#include <cstdio>
#include <iostream>
int main() { /* fflush */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdio
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdio/fclose|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fopen|Vperyod]]
