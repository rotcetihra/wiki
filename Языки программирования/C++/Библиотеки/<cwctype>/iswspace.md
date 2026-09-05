# iswspace

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] / iswspace

[[Языки программирования/C++/Библиотеки/cwctype/iswpunct|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] | [[Языки программирования/C++/Библиотеки/cwctype/iswupper|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwctype>
int iswspace(wint_t c);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `c` | Wide char |

## Vozvrashaemoe znachenie

Nonzero if whitespace.

## Chto delaet

Checks whitespace.

## Primery

### Bazovoe

```cpp
#include <cwctype>
#include <iostream>
int main() { std::iswspace(L'A'); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwctype
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwctype/iswpunct|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] | [[Языки программирования/C++/Библиотеки/cwctype/iswupper|Vperyod]]
