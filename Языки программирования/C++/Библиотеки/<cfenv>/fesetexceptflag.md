# fesetexceptflag

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] / fesetexceptflag

[[Языки программирования/C++/Библиотеки/cfenv/feraiseexcept|Nazad]] | [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] | [[Языки программирования/C++/Библиотеки/cfenv/fetestexcept|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cfenv>
int fesetexceptflag(const fexcept_t *flagp, int excepts);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `flagp` | Pointer |
| `excepts` | Mask |

## Vozvrashaemoe znachenie

0 on success.

## Chto delaet

Sets exception flags.

## Primery

### Bazovoe

```cpp
#include <cfenv>
#include <iostream>
int main() { /* fesetexceptflag */ return 0; }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cfenv
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cfenv/feraiseexcept|Nazad]] | [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] | [[Языки программирования/C++/Библиотеки/cfenv/fetestexcept|Vperyod]]
