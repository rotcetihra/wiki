# vfprintf

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] / vfprintf

[[Языки программирования/C++/Библиотеки/cstdio/sscanf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/vfscanf|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdio>
int vfprintf(FILE *stream, const char *format, va_list ap);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `stream` | Stream |
| `format` | Format |
| `ap` | List |

## Vozvrashaemoe znachenie

Chars written.

## Chto delaet

va_list output to file.

## Primery

### Bazovoe

```cpp
#include <cstdio>
#include <iostream>
int main() { /* vfprintf */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdio
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdio/sscanf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/vfscanf|Vperyod]]
