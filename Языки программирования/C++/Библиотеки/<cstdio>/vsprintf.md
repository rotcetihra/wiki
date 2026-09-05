# vsprintf

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] / vsprintf

[[Языки программирования/C++/Библиотеки/cstdio/vsnprintf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/vsscanf|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdio>
int vsprintf(char *str, const char *format, va_list ap);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `str` | Buffer |
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
int main() { /* vsprintf */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdio
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdio/vsnprintf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdio>/cstdio|cstdio]] | [[Языки программирования/C++/Библиотеки/cstdio/vsscanf|Vperyod]]
