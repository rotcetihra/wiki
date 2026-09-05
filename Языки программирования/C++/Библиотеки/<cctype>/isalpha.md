# isalpha

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]] / isalpha

[[Языки программирования/C++/Библиотеки/cctype/isalnum|Nazad]] | [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]] | [[Языки программирования/C++/Библиотеки/cctype/isblank|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cctype>
int isalpha(int c);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `c` | Symbol |

## Vozvrashaemoe znachenie

Nonzero if letter.

## Chto delaet

Checks letter.

## Primery

### Bazovoe

```cpp
#include <cctype>
#include <iostream>
int main() { std::cout << std::isalpha('A'); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cctype
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cctype/isalnum|Nazad]] | [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]] | [[Языки программирования/C++/Библиотеки/cctype/isblank|Vperyod]]
