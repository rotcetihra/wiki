# wctrans

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] / wctrans

[[Языки программирования/C++/Библиотеки/cwctype/towctrans|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] | [[Языки программирования/C++/Библиотеки/cwctype/|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwctype>
wctrans_t wctrans(const char *property);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `property` | Property string |

## Vozvrashaemoe znachenie

Type or 0.

## Chto delaet

Gets transliteration type.

## Primery

### Bazovoe

```cpp
#include <cwctype>
#include <iostream>
int main() { std::wctrans(L'A'); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwctype
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwctype/towctrans|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] | [[Языки программирования/C++/Библиотеки/cwctype/|Vperyod]]
