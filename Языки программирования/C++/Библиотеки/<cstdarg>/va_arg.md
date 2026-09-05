# va_arg

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]] / va_arg

[[Языки программирования/C++/Библиотеки/cstdarg/va_start|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]] | [[Языки программирования/C++/Библиотеки/cstdarg/va_end|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdarg>
type va_arg(va_list ap, type);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `ap` | List |
| `type` | Type |

## Vozvrashaemoe znachenie

Next argument.

## Chto delaet

Extracts argument.

## Primery

### Bazovoe

```cpp
#include <cstdarg>
#include <iostream>
void f(int n, ...) { va_list args; va_start(args, n); int v = va_arg(args, int); va_end(args); }
```

## Iskljuchenija

- Undefined if wrong type.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdarg
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdarg/va_start|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]] | [[Языки программирования/C++/Библиотеки/cstdarg/va_end|Vperyod]]
