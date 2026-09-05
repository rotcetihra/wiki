# putwc

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / putwc

[[Языки программирования/C++/Библиотеки/cwchar/mbsrtowcs|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/putwchar|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
wint_t putwc(wchar_t c, FILE *stream);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `c` | Wide char |
| `stream` | Stream |

## Vozvrashaemoe znachenie

Wide char or WEOF.

## Chto delaet

Writes wide char.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* putwc */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/mbsrtowcs|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/putwchar|Vperyod]]
