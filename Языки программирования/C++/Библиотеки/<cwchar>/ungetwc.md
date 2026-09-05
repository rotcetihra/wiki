# ungetwc

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / ungetwc

[[Языки программирования/C++/Библиотеки/cwchar/swscanf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/vfwprintf|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
wint_t ungetwc(wint_t c, FILE *stream);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `c` | Wide char |
| `stream` | Stream |

## Vozvrashaemoe znachenie

Wide char or WEOF.

## Chto delaet

Pushes wide char back.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* ungetwc */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/swscanf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/vfwprintf|Vperyod]]
