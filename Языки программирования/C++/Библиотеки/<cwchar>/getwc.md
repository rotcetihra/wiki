# getwc

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / getwc

[[Языки программирования/C++/Библиотеки/cwchar/fwscanf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/getwchar|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
wint_t getwc(FILE *stream);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `stream` | Stream |

## Vozvrashaemoe znachenie

Wide char or WEOF.

## Chto delaet

Reads wide char.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* getwc */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/fwscanf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/getwchar|Vperyod]]
