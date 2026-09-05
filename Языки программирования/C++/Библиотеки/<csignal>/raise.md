# raise

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<csignal>/csignal|csignal]] / raise

[[Языки программирования/C++/Библиотеки/csignal/signal|Nazad]] | [[Языки программирования/C++/Библиотеки/<csignal>/csignal|csignal]] | [[Языки программирования/C++/Библиотеки/csignal/|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <csignal>
int raise(int sig);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `sig` | Signal number |

## Vozvrashaemoe znachenie

0 on success.

## Chto delaet

Generates signal.

## Primery

### Bazovoe

```cpp
#include <csignal>
#include <iostream>
int main() { std::raise(SIGINT); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<csignal>/csignal|csignal]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/csignal
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/csignal/signal|Nazad]] | [[Языки программирования/C++/Библиотеки/<csignal>/csignal|csignal]] | [[Языки программирования/C++/Библиотеки/csignal/|Vperyod]]
