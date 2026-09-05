# ungetc

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] / ungetc

[[Языки программирования/C++/Библиотеки/cstdio/putchar|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fread|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdio>
int ungetc(int c, FILE *stream);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `c` | Char |
| `stream` | Stream |

## Vozvrashaemoe znachenie

Char or EOF.

## Chto delaet

Pushes char back.

## Primery

### Bazovoe

```cpp
#include <cstdio>
#include <iostream>
int main() { /* ungetc */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdio
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdio/putchar|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fread|Vperyod]]
