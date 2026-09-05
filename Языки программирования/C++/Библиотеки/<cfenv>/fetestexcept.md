# fetestexcept

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] / fetestexcept

[[Языки программирования/C++/Библиотеки/cfenv/fesetexceptflag|Nazad]] | [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] | [[Языки программирования/C++/Библиотеки/cfenv/fegetround|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cfenv>
int fetestexcept(int excepts);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `excepts` | Mask |

## Vozvrashaemoe znachenie

Mask of set exceptions.

## Chto delaet

Tests exceptions.

## Primery

### Bazovoe

```cpp
#include <cfenv>
#include <iostream>
int main() { /* fetestexcept */ return 0; }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cfenv
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cfenv/fesetexceptflag|Nazad]] | [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] | [[Языки программирования/C++/Библиотеки/cfenv/fegetround|Vperyod]]
