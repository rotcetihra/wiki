# towctrans

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] / towctrans

[[Языки программирования/C++/Библиотеки/cwctype/towupper|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] | [[Языки программирования/C++/Библиотеки/cwctype/wctrans|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwctype>
wint_t towctrans(wint_t c, wctrans_t desc);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `c` | Wide char |
| `desc` | Type |

## Vozvrashaemoe znachenie

Transformed wide char.

## Chto delaet

Transliterates wide char.

## Primery

### Bazovoe

```cpp
#include <cwctype>
#include <iostream>
int main() { std::towctrans(L'A'); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwctype
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwctype/towupper|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] | [[Языки программирования/C++/Библиотеки/cwctype/wctrans|Vperyod]]
