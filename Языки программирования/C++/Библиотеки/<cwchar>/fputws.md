# fputws

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / fputws

[[Языки программирования/C++/Библиотеки/cwchar/fputwc|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/fwide|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
int fputws(const wchar_t *str, FILE *stream);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `str` | String |
| `stream` | Stream |

## Vozvrashaemoe znachenie

Non-negative or EOF.

## Chto delaet

Writes wide string.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* fputws */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/fputwc|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/fwide|Vperyod]]
