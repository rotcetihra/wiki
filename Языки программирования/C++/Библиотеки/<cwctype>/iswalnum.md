# iswalnum

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] / iswalnum

[[Языки программирования/C++/Библиотеки/cwctype/WEOF|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] | [[Языки программирования/C++/Библиотеки/cwctype/iswalpha|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwctype>
int iswalnum(wint_t c);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `c` | Wide char |

## Vozvrashaemoe znachenie

Nonzero if alphanumeric.

## Chto delaet

Checks alphanumeric.

## Primery

### Bazovoe

```cpp
#include <cwctype>
#include <iostream>
int main() { std::iswalnum(L'A'); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwctype
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwctype/WEOF|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] | [[Языки программирования/C++/Библиотеки/cwctype/iswalpha|Vperyod]]
