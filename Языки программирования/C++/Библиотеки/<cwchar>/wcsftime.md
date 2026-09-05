# wcsftime

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / wcsftime

[[Языки программирования/C++/Библиотеки/cwchar/wcscspn|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wcslen|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
size_t wcsftime(wchar_t *s, size_t maxsize, const wchar_t *format, const struct tm *timeptr);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s` | Buffer |
| `maxsize` | Max |
| `format` | Format |
| `timeptr` | tm pointer |

## Vozvrashaemoe znachenie

Chars written.

## Chto delaet

Formats time wide.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* wcsftime */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/wcscspn|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wcslen|Vperyod]]
