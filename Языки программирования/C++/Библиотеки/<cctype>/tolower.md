# tolower

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]] / tolower

[[Языки программирования/C++/Библиотеки/cctype/isxdigit|Nazad]] | [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]] | [[Языки программирования/C++/Библиотеки/cctype/toupper|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cctype>
int tolower(int c);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `c` | Symbol |

## Vozvrashaemoe znachenie

Converted character.

## Chto delaet

Converts to lowercase.

## Primery

### Bazovoe

```cpp
#include <cctype>
#include <iostream>
int main() { std::cout << (char)std::tolower('A'); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cctype
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cctype/isxdigit|Nazad]] | [[Языки программирования/C++/Библиотеки/<cctype>/cctype|cctype]] | [[Языки программирования/C++/Библиотеки/cctype/toupper|Vperyod]]
