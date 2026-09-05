# vfwscanf

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / vfwscanf

[[Языки программирования/C++/Библиотеки/cwchar/vfwprintf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/vswprintf|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
int vfwscanf(FILE *stream, const wchar_t *format, va_list arg);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `stream` | Stream |
| `format` | Format |
| `arg` | List |

## Vozvrashaemoe znachenie

Items read.

## Chto delaet

va_list wide input.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* vfwscanf */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/vfwprintf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/vswprintf|Vperyod]]
