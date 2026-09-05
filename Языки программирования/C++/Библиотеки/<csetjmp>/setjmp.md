# setjmp

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<csetjmp>/csetjmp|csetjmp]] / setjmp

[[Языки программирования/C++/Библиотеки/csetjmp/jmp_buf|Nazad]] | [[Языки программирования/C++/Библиотеки/<csetjmp>/csetjmp|csetjmp]] | [[Языки программирования/C++/Библиотеки/csetjmp/longjmp|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <csetjmp>
int setjmp(jmp_buf env);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `env` | Buffer |

## Vozvrashaemoe znachenie

0 on first call, nonzero from longjmp.

## Chto delaet

Saves context.

## Primery

### Bazovoe

```cpp
#include <csetjmp>
#include <iostream>
jmp_buf env;
int main() { if (setjmp(env) == 0) {} }
```

## Iskljuchenija

- Undefined if function returned.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<csetjmp>/csetjmp|csetjmp]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/csetjmp
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/csetjmp/jmp_buf|Nazad]] | [[Языки программирования/C++/Библиотеки/<csetjmp>/csetjmp|csetjmp]] | [[Языки программирования/C++/Библиотеки/csetjmp/longjmp|Vperyod]]
