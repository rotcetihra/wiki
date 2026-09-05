# wctomb

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / wctomb

[[Языки программирования/C++/Библиотеки/cwchar/wctob|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wmemcpy|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
int wctomb(char *s, wchar_t wc);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s` | Dest |
| `wc` | Wide char |

## Vozvrashaemoe znachenie

Bytes or -1.

## Chto delaet

Wide to multibyte.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* wctomb */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/wctob|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wmemcpy|Vperyod]]
