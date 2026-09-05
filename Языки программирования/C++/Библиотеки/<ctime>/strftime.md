# strftime

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] / strftime

[[Языки программирования/C++/Библиотеки/ctime/mktime|Nazad]] | [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] | [[Языки программирования/C++/Библиотеки/ctime/time|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <ctime>
size_t strftime(char *s, size_t maxsize, const char *format, const struct tm *timeptr);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s` | Buffer |
| `maxsize` | Max |
| `format` | Format |
| `timeptr` | Pointer to tm |

## Vozvrashaemoe znachenie

Number of chars.

## Chto delaet

Formats time.

## Primery

### Bazovoe

```cpp
#include <ctime>
#include <iostream>
int main() { /* strftime */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/ctime
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/ctime/mktime|Nazad]] | [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] | [[Языки программирования/C++/Библиотеки/ctime/time|Vperyod]]
