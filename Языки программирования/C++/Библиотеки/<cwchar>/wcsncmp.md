# wcsncmp

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / wcsncmp

[[Языки программирования/C++/Библиотеки/cwchar/wcsncat|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wcsncpy|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
int wcsncmp(const wchar_t *s1, const wchar_t *s2, size_t n);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s1` | String1 |
| `s2` | String2 |
| `n` | Max |

## Vozvrashaemoe znachenie

Negative, 0, positive.

## Chto delaet

Compare with limit.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* wcsncmp */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/wcsncat|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wcsncpy|Vperyod]]
