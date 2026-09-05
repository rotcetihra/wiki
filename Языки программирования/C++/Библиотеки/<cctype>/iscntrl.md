# iscntrl

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]] / iscntrl

[[Языки программирования/C++/Библиотеки/cctype/isblank|Nazad]] | [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]] | [[Языки программирования/C++/Библиотеки/cctype/isdigit|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cctype>
int iscntrl(int c);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `c` | Symbol |

## Vozvrashaemoe znachenie

Nonzero if control.

## Chto delaet

Checks control character.

## Primery

### Bazovoe

```cpp
#include <cctype>
#include <iostream>
int main() { std::cout << std::iscntrl('\n'); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cctype
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cctype/isblank|Nazad]] | [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]] | [[Языки программирования/C++/Библиотеки/cctype/isdigit|Vperyod]]
