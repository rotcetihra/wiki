# wctype

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] / wctype

[[Языки программирования/C++/Библиотеки/cwctype/iswctype|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] | [[Языки программирования/C++/Библиотеки/cwctype/towlower|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwctype>
wctype_t wctype(const char *property);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `property` | Property string |

## Vozvrashaemoe znachenie

Type or 0.

## Chto delaet

Gets class type.

## Primery

### Bazovoe

```cpp
#include <cwctype>
#include <iostream>
int main() { std::wctype(L'A'); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwctype
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwctype/iswctype|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwctype>/cwctype|cwctype]] | [[Языки программирования/C++/Библиотеки/cwctype/towlower|Vperyod]]
