# wcrtomb

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / wcrtomb

[[Языки программирования/C++/Библиотеки/cwchar/vwscanf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wcscat|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
size_t wcrtomb(char *s, wchar_t wc, mbstate_t *ps);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `s` | Dest |
| `wc` | Wide char |
| `ps` | State |

## Vozvrashaemoe znachenie

Bytes written.

## Chto delaet

wchar_t to multibyte.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* wcrtomb */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/vwscanf|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wcscat|Vperyod]]
