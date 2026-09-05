# fwrite

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] / fwrite

[[Языки программирования/C++/Библиотеки/cstdio/fread|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fgetpos|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdio>
size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `ptr` | Data |
| `size` | Size |
| `nmemb` | Count |
| `stream` | Stream |

## Vozvrashaemoe znachenie

Items written.

## Chto delaet

Writes block.

## Primery

### Bazovoe

```cpp
#include <cstdio>
#include <iostream>
int main() { /* fwrite */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdio
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdio/fread|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/fgetpos|Vperyod]]
