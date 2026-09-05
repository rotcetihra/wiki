# fgetws

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / fgetws

[[Языки программирования/C++/Библиотеки/cwchar/fgetwc|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/fputwc|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
wchar_t *fgetws(wchar_t *str, int n, FILE *stream);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `str` | Buffer |
| `n` | Max |
| `stream` | Stream |

## Vozvrashaemoe znachenie

Pointer or NULL.

## Chto delaet

Reads wide line.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* fgetws */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/fgetwc|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/fputwc|Vperyod]]
