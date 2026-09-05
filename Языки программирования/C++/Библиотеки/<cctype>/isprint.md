# isprint

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]] / isprint

[[Языки программирования/C++/Библиотеки/cctype/islower|Nazad]] | [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]] | [[Языки программирования/C++/Библиотеки/cctype/ispunct|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cctype>
int isprint(int c);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `c` | Symbol |

## Vozvrashaemoe znachenie

Nonzero if printable.

## Chto delaet

Checks printable.

## Primery

### Bazovoe

```cpp
#include <cctype>
#include <iostream>
int main() { std::cout << std::isprint('A'); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cctype
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cctype/islower|Nazad]] | [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]] | [[Языки программирования/C++/Библиотеки/cctype/ispunct|Vperyod]]
