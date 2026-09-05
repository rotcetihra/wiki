# va_start

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]] / va_start

[[Языки программирования/C++/Библиотеки/cstdarg/va_list|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]] | [[Языки программирования/C++/Библиотеки/cstdarg/va_arg|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdarg>
void va_start(va_list ap, parmN);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `ap` | List |
| `parmN` | Last param |

## Vozvrashaemoe znachenie

Nothing.

## Chto delaet

Initializes list.

## Primery

### Bazovoe

```cpp
#include <cstdarg>
void f(int n, ...) { va_list args; va_start(args, n); va_end(args); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdarg
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdarg/va_list|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]] | [[Языки программирования/C++/Библиотеки/cstdarg/va_arg|Vperyod]]
