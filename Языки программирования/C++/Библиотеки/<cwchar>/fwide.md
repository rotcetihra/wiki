# fwide

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / fwide

[[Языки программирования/C++/Библиотеки/cwchar/fputws|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/fwprintf|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
int fwide(FILE *stream, int mode);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `stream` | Stream |
| `mode` | Mode |

## Vozvrashaemoe znachenie

Positive/negative/zero.

## Chto delaet

Sets wide orientation.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* fwide */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/fputws|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/fwprintf|Vperyod]]
