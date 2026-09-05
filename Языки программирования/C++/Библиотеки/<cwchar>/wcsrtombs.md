# wcsrtombs

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / wcsrtombs

[[Языки программирования/C++/Библиотеки/cwchar/wcsrchr|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wcsspn|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
size_t wcsrtombs(char *dest, const wchar_t **src, size_t len, mbstate_t *ps);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `dest` | Dest |
| `src` | Source |
| `len` | Max |
| `ps` | State |

## Vozvrashaemoe znachenie

Bytes.

## Chto delaet

Wide to multibyte.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* wcsrtombs */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/wcsrchr|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wcsspn|Vperyod]]
