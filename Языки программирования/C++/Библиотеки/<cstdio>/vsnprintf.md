# vsnprintf

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] / vsnprintf

[[Языки программирования/C++/Библиотеки/cstdio/vscanf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/vsprintf|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdio>
int vsnprintf(char *str, size_t size, const char *format, va_list ap);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `str` | Buffer |
| `size` | Size |
| `format` | Format |
| `ap` | List |

## Vozvrashaemoe znachenie

Chars written.

## Chto delaet

va_list to string.

## Primery

### Bazovoe

```cpp
#include <cstdio>
#include <iostream>
int main() { /* vsnprintf */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdio
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdio/vscanf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/vsprintf|Vperyod]]
