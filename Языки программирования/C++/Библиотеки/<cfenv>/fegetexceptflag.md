# fegetexceptflag

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] / fegetexceptflag

[[Языки программирования/C++/Библиотеки/cfenv/feclearexcept|Nazad]] | [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] | [[Языки программирования/C++/Библиотеки/cfenv/feraiseexcept|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cfenv>
int fegetexceptflag(fexcept_t *flagp, int excepts);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `flagp` | Pointer |
| `excepts` | Mask |

## Vozvrashaemoe znachenie

0 on success.

## Chto delaet

Gets exception flags.

## Primery

### Bazovoe

```cpp
#include <cfenv>
#include <iostream>
int main() { /* fegetexceptflag */ return 0; }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cfenv
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cfenv/feclearexcept|Nazad]] | [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] | [[Языки программирования/C++/Библиотеки/cfenv/feraiseexcept|Vperyod]]
