# iswxdigit

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] / iswxdigit

[[Языки программирования/C++/Библиотеки/cwctype/iswupper|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] | [[Языки программирования/C++/Библиотеки/cwctype/iswctype|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwctype>
int iswxdigit(wint_t c);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `c` | Wide char |

## Vozvrashaemoe znachenie

Nonzero if hex digit.

## Chto delaet

Checks hex.

## Primery

### Bazovoe

```cpp
#include <cwctype>
#include <iostream>
int main() { std::iswxdigit(L'A'); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwctype
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwctype/iswupper|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] | [[Языки программирования/C++/Библиотеки/cwctype/iswctype|Vperyod]]
