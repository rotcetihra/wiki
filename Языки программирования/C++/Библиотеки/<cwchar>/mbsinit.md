# mbsinit

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / mbsinit

[[Языки программирования/C++/Библиотеки/cwchar/mbrtowc|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/mbsrtowcs|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
int mbsinit(const mbstate_t *ps);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `ps` | State |

## Vozvrashaemoe znachenie

Nonzero if initial.

## Chto delaet

Checks initial state.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* mbsinit */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/mbrtowc|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/mbsrtowcs|Vperyod]]
