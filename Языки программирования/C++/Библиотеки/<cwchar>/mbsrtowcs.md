# mbsrtowcs

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / mbsrtowcs

[[Языки программирования/C++/Библиотеки/cwchar/mbsinit|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/putwc|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
size_t mbsrtowcs(wchar_t *dest, const char **src, size_t len, mbstate_t *ps);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `dest` | Dest |
| `src` | Source |
| `len` | Max |
| `ps` | State |

## Vozvrashaemoe znachenie

Wide chars.

## Chto delaet

Multibyte to wide.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* mbsrtowcs */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/mbsinit|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/putwc|Vperyod]]
