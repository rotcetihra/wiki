# va_end

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]] / va_end

[[Языки программирования/C++/Библиотеки/cstdarg/va_arg|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]] | [[Языки программирования/C++/Библиотеки/cstdarg/va_copy|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cstdarg>
void va_end(va_list ap);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `ap` | List |

## Vozvrashaemoe znachenie

Nothing.

## Chto delaet

Ends list.

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

[[Языки программирования/C++/Библиотеки/cstdarg/va_arg|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstdarg>/cstdarg|cstdarg]] | [[Языки программирования/C++/Библиотеки/cstdarg/va_copy|Vperyod]]
