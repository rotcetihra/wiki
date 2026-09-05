# vswprintf

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / vswprintf

[[Языки программирования/C++/Библиотеки/cwchar/vfwscanf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/vswscanf|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
int vswprintf(wchar_t *s, size_t n, const wchar_t *format, va_list arg);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s` | Buffer |
| `n` | Size |
| `format` | Format |
| `arg` | List |

## Vozvrashaemoe znachenie

Chars written.

## Chto delaet

va_list wide to string.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* vswprintf */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/vfwscanf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/vswscanf|Vperyod]]
