# mbrlen

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / mbrlen

[[Языки программирования/C++/Библиотеки/cwchar/getwchar|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/mbrtowc|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
size_t mbrlen(const char *s, size_t n, mbstate_t *ps);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s` | String |
| `n` | Max |
| `ps` | State |

## Vozvrashaemoe znachenie

Bytes, 0, or (size_t)-1.

## Chto delaet

Wide char length.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* mbrlen */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/getwchar|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/mbrtowc|Vperyod]]
