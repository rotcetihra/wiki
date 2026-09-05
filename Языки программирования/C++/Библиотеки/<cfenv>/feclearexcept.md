# feclearexcept

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] / feclearexcept

[[Языки программирования/C++/Библиотеки/cfenv/|Nazad]] | [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] | [[Языки программирования/C++/Библиотеки/cfenv/fegetexceptflag|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cfenv>
int feclearexcept(int excepts);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `excepts` | Mask |

## Vozvrashaemoe znachenie

0 on success.

## Chto delaet

Clears exceptions.

## Primery

### Bazovoe

```cpp
#include <cfenv>
#include <iostream>
int main() { /* feclearexcept */ return 0; }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cfenv
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cfenv/|Nazad]] | [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] | [[Языки программирования/C++/Библиотеки/cfenv/fegetexceptflag|Vperyod]]
