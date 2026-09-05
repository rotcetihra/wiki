# vswscanf

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / vswscanf

[[Языки программирования/C++/Библиотеки/cwchar/vswprintf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/vwprintf|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
int vswscanf(const wchar_t *s, const wchar_t *format, va_list arg);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s` | String |
| `format` | Format |
| `arg` | List |

## Vozvrashaemoe znachenie

Items read.

## Chto delaet

va_list wide from string.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* vswscanf */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/vswprintf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/vwprintf|Vperyod]]
