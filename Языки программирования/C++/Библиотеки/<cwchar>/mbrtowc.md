# mbrtowc

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / mbrtowc

[[Языки программирования/C++/Библиотеки/cwchar/mbrlen|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/mbsinit|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
size_t mbrtowc(wchar_t *pwc, const char *s, size_t n, mbstate_t *ps);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `pwc` | Dest |
| `s` | Source |
| `n` | Max |
| `ps` | State |

## Vozvrashaemoe znachenie

Bytes, 0, or (size_t)-1.

## Chto delaet

Multibyte to wchar_t.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* mbrtowc */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/mbrlen|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/mbsinit|Vperyod]]
