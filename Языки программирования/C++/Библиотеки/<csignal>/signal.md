# signal

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<csignal>/csignal|csignal]] / signal

[[Языки программирования/C++/Библиотеки/csignal/sig_atomic_t|Nazad]] | [[Языки программирования/C++/Библиотеки/<csignal>/csignal|csignal]] | [[Языки программирования/C++/Библиотеки/csignal/raise|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <csignal>
void (*signal(int sig, void (*handler)(int)))(int);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `sig` | Signal number |
| `handler` | Handler |

## Vozvrashaemoe znachenie

Previous handler.

## Chto delaet

Sets signal handler.

## Primery

### Bazovoe

```cpp
#include <csignal>
#include <iostream>
void h(int s) {}
int main() { std::signal(SIGINT, h); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<csignal>/csignal|csignal]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/csignal
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/csignal/sig_atomic_t|Nazad]] | [[Языки программирования/C++/Библиотеки/<csignal>/csignal|csignal]] | [[Языки программирования/C++/Библиотеки/csignal/raise|Vperyod]]
