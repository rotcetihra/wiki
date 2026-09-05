# assert

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cassert>/cassert|cassert]] / assert

[[Языки программирования/C++/Библиотеки/cassert/|Nazad]] | [[Языки программирования/C++/Библиотеки/<cassert>/cassert|cassert]] | [[Языки программирования/C++/Библиотеки/cassert/|Vperyod]]

**Дата написания:** 05.09.2026

## Opredelenie

```cpp
#include <cassert>
#define assert(expression) // implementation-defined
```

## Opisanie

`assert` проверяет выражение. При ложи выводит `abort()`. При `NDEBUG` — пуст.

## Primery

### Bazovoe

```cpp
#include <cassert>
#include <iostream>

int main() {
    int x = 5;
    assert(x == 5);
    return 0;
}
```

## Iskljuchenija

- Ne brosayut iskljuchenij — vyzyvaet `abort()`.

## Pohozhie jelementy

- [[Языки программирования/C++/Библиотеки/<cassert>/cassert|cassert]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cassert
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cassert/|Nazad]] | [[Языки программирования/C++/Библиотеки/<cassert>/cassert|cassert]] | [[Языки программирования/C++/Библиотеки/cassert/|Vperyod]]
