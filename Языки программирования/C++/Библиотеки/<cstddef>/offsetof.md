# offsetof

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstddef>/cstddef|cstddef]] / offsetof

[[Языки программирования/C++/Библиотеки/cstddef/max_align_t|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstddef>/cstddef|cstddef]] | [[Языки программирования/C++/Библиотеки/cstddef/|Vperyod]]

**Дата написания:** 05.09.2026

## Opredelenie

```cpp
#include <cstddef>
#define offsetof(type, member)
```

## Opisanie

Returns offset of member.

## Primery

### Bazovoe

```cpp
#include <cstddef>
#include <iostream>
struct S { int x; int y; };
int main() { std::cout << offsetof(S, y); }
```

## Iskljuchenija

- No exceptions.

## Pohozhie jelementy

- [[Языки программирования/C++/Библиотеки/<cstddef>/cstddef|cstddef]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstddef
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstddef/max_align_t|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstddef>/cstddef|cstddef]] | [[Языки программирования/C++/Библиотеки/cstddef/|Vperyod]]
