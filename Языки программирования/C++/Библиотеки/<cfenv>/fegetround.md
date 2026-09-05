# fegetround

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] / fegetround

[[Языки программирования/C++/Библиотеки/cfenv/fetestexcept|Nazad]] | [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] | [[Языки программирования/C++/Библиотеки/cfenv/fesetround|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cfenv>
int fegetround(void);
```

## Parametry

| Parametr | Opisanie |
|---|---|

## Vozvrashaemoe znachenie

Current rounding mode.

## Chto delaet

Gets rounding mode.

## Primery

### Bazovoe

```cpp
#include <cfenv>
#include <iostream>
int main() { std::fegetround(); return 0; }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cfenv
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cfenv/fetestexcept|Nazad]] | [[Языки программирования/C++/Библиотеки/<cfenv>/cfenv|cfenv]] | [[Языки программирования/C++/Библиотеки/cfenv/fesetround|Vperyod]]
