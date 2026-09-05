# swprintf

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / swprintf

[[Языки программирования/C++/Библиотеки/cwchar/putwchar|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/swscanf|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
int swprintf(wchar_t *s, size_t n, const wchar_t *format, ...);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s` | Buffer |
| `n` | Size |
| `format` | Format |

## Vozvrashaemoe znachenie

Chars written.

## Chto delaet

Wide formatted to string.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* swprintf */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/putwchar|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/swscanf|Vperyod]]
