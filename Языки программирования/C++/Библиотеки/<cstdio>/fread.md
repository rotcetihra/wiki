# fread

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] / fread

[[Языки программирования/C++/Библиотеки/cstdio/ungetc|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fwrite|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdio>
size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `ptr` | Buffer |
| `size` | Size |
| `nmemb` | Count |
| `stream` | Stream |

## Vozvrashaemoe znachenie

Items read.

## Chto delaet

Reads block.

## Primery

### Bazovoe

```cpp
#include <cstdio>
#include <iostream>
int main() { /* fread */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdio
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdio/ungetc|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fwrite|Vperyod]]
