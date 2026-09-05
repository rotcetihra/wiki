# wmemcpy

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / wmemcpy

[[Языки программирования/C++/Библиотеки/cwchar/wctomb|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wmemmove|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
wchar_t *wmemcpy(wchar_t *dest, const wchar_t *src, size_t n);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `dest` | Dest |
| `src` | Src |
| `n` | Count |

## Vozvrashaemoe znachenie

dest.

## Chto delaet

Copies wide block.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* wmemcpy */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/wctomb|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wmemmove|Vperyod]]
