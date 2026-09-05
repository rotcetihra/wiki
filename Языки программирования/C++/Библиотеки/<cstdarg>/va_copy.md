# va_copy

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]] / va_copy

[[Языки программирования/C++/Библиотеки/cstdarg/va_end|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]] | [[Языки программирования/C++/Библиотеки/cstdarg/|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdarg>
void va_copy(va_list dest, va_list src);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `dest` | Dest |
| `src` | Source |

## Vozvrashaemoe znachenie

Nothing.

## Chto delaet

Copies list.

## Primery

### Bazovoe

```cpp
#include <cstdarg>
void f(int n, ...) { va_list a, b; va_start(a, n); va_copy(b, a); va_end(a); va_end(b); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstdarg
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstdarg/va_end|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]] | [[Языки программирования/C++/Библиотеки/cstdarg/|Vperyod]]
