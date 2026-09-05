# vfscanf

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] / vfscanf

[[Языки программирования/C++/Библиотеки/cstdio/vfprintf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/vprintf|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdio>
int vfscanf(FILE *stream, const char *format, va_list ap);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `stream` | Stream |
| `format` | Format |
| `ap` | List |

## Vozvrashaemoe znachenie

Items read.

## Chto delaet

va_list input from file.

## Primery

### Bazovoe

```cpp
#include <cstdio>
#include <iostream>
int main() { /* vfscanf */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdio
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdio/vfprintf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/vprintf|Vperyod]]
