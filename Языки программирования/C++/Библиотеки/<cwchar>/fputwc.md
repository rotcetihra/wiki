# fputwc

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / fputwc

[[Языки программирования/C++/Библиотеки/cwchar/fgetws|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/fputws|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
wint_t fputwc(wchar_t c, FILE *stream);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `c` | Wide char |
| `stream` | Stream |

## Vozvrashaemoe znachenie

Wide char or WEOF.

## Chto delaet

Writes wide char.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* fputwc */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/fgetws|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/fputws|Vperyod]]
