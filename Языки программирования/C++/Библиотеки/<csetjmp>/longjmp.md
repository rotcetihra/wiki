# longjmp

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<csetjmp>/csetjmp|csetjmp]] / longjmp

[[Языки программирования/C++/Библиотеки/csetjmp/setjmp|Nazad]] | [[Языки программирования/C++/Библиотеки/<csetjmp>/csetjmp|csetjmp]] | [[Языки программирования/C++/Библиотеки/csetjmp/|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <csetjmp>
void longjmp(jmp_buf env, int val);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `env` | Buffer |
| `val` | Value |

## Vozvrashaemoe znachenie

Does not return.

## Chto delaet

Restores context.

## Primery

### Bazovoe

```cpp
#include <csetjmp>
#include <iostream>
jmp_buf env;
void fail() { longjmp(env, 1); }
```

## Iskljuchenija

- Undefined behavior.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<csetjmp>/csetjmp|csetjmp]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/csetjmp
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/csetjmp/setjmp|Nazad]] | [[Языки программирования/C++/Библиотеки/<csetjmp>/csetjmp|csetjmp]] | [[Языки программирования/C++/Библиотеки/csetjmp/|Vperyod]]
