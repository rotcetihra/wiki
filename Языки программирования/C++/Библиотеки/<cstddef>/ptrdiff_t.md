# ptrdiff_t

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cstddef>/cstddef|cstddef]] / ptrdiff_t

[[Языки программирования/C++/Библиотеки/cstddef/size_t|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstddef>/cstddef|cstddef]] | [[Языки программирования/C++/Библиотеки/cstddef/max_align_t|Vperyod]]

**Дата написания:** 05.09.2026

## Opredelenie

```cpp
#include <cstddef>
typedef /* signed */ ptrdiff_t;
```

## Opisanie

Pointer difference.

## Primery

### Bazovoe

```cpp
#include <cstddef>
#include <iostream>
int main() { int a[5]; ptrdiff_t d = &a[4] - &a[0]; }
```

## Iskljuchenija

- No exceptions.

## Pohozhie jelementy

- [[Языки программирования/C++/Библиотеки/<cstddef>/cstddef|cstddef]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cstddef
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cstddef/size_t|Nazad]] | [[Языки программирования/C++/Библиотеки/<cstddef>/cstddef|cstddef]] | [[Языки программирования/C++/Библиотеки/cstddef/max_align_t|Vperyod]]
