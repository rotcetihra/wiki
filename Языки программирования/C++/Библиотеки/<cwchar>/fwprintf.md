# fwprintf

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / fwprintf

[[Языки программирования/C++/Библиотеки/cwchar/fwide|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/fwscanf|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
int fwprintf(FILE *stream, const wchar_t *format, ...);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `stream` | Stream |
| `format` | Format |

## Vozvrashaemoe znachenie

Chars written.

## Chto delaet

Formatted wide output.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* fwprintf */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/fwide|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/fwscanf|Vperyod]]
