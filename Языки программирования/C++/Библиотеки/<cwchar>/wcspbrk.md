# wcspbrk

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / wcspbrk

[[Языки программирования/C++/Библиотеки/cwchar/wcsncpy|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wcsrchr|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
const wchar_t *wcspbrk(const wchar_t *s1, const wchar_t *s2);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s1` | String |
| `s2` | Accept |

## Vozvrashaemoe znachenie

Pointer or NULL.

## Chto delaet

Finds any of wide chars.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* wcspbrk */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/wcsncpy|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wcsrchr|Vperyod]]
