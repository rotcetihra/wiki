# setlocale

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<clocale>/clocale|clocale]] / setlocale

[[Языки программирования/C++/Библиотеки/clocale/lconv|Nazad]] | [[Языки программирования/C++/Библиотеки/<clocale>/clocale|clocale]] | [[Языки программирования/C++/Библиотеки/clocale/localeconv|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <clocale>
char *setlocale(int category, const char *locale);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `category` | LC_* |
| `locale` | Locale string |

## Vozvrashaemoe znachenie

Pointer to locale string.

## Chto delaet

Sets locale.

## Primery

### Bazovoe

```cpp
#include <clocale>
#include <iostream>
int main() { std::setlocale(LC_ALL, ""); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<clocale>/clocale|clocale]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/clocale
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/clocale/lconv|Nazad]] | [[Языки программирования/C++/Библиотеки/<clocale>/clocale|clocale]] | [[Языки программирования/C++/Библиотеки/clocale/localeconv|Vperyod]]
