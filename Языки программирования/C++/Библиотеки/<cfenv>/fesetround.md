# fesetround

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] / fesetround

[[Языки программирования/C++/Библиотеки/cfenv/fegetround|Nazad]] | [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] | [[Языки программирования/C++/Библиотеки/cfenv/|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cfenv>
int fesetround(int round);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `round` | FE_* |

## Vozvrashaemoe znachenie

Previous rounding mode.

## Chto delaet

Sets rounding mode.

## Primery

### Bazovoe

```cpp
#include <cfenv>
#include <iostream>
int main() { /* fesetround */ return 0; }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cfenv
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cfenv/fegetround|Nazad]] | [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] | [[Языки программирования/C++/Библиотеки/cfenv/|Vperyod]]
