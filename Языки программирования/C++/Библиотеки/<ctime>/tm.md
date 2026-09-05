# tm

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] / tm

[[Языки программирования/C++/Библиотеки/ctime/time_t|Nazad]] | [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] | [[Языки программирования/C++/Библиотеки/ctime/|Vperyod]]

**Дата написания:** 05.09.2026

## Opredelenie

```cpp
#include <ctime>
struct tm { int tm_sec; int tm_min; int tm_hour; int tm_mday; int tm_mon; int tm_year; int tm_wday; int tm_yday; int tm_isdst; };
```

## Opisanie

Time structure.

## Primery

### Bazovoe

```cpp
#include <ctime>
#include <iostream>
int main() { tm t; }
```

## Iskljuchenija

- No exceptions.

## Pohozhie jelementy

- [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/ctime
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/ctime/time_t|Nazad]] | [[Языки программирования/C++/Библиотеки/<ctime>/ctime|ctime]] | [[Языки программирования/C++/Библиотеки/ctime/|Vperyod]]
