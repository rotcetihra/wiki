# wcstoul

[[Языки программирования/C++/Библиотеки|Biblioteki]] / [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] / wcstoul

[[Языки программирования/C++/Библиотеки/cwchar/wcstol|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wcswcs|Vperyod]]

**Дата написания:** 05.09.2026

## Prototip

```cpp
#include <cwchar>
unsigned long wcstoul(const wchar_t *str, wchar_t **endptr, int base);
```

## Parametry

| Parametr | Opisanie |
|---|---|
| `str` | String |
| `endptr` | End pointer |
| `base` | Base |

## Vozvrashaemoe znachenie

Unsigned long.

## Chto delaet

Wide to unsigned long.

## Primery

### Bazovoe

```cpp
#include <cwchar>
#include <iostream>
int main() { /* wcstoul */ }
```

## Iskljuchenija

- No exceptions.

## Pohozhie funkcii

- [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]]

## Istochniki

- https://en.cppreference.com/w/cpp/header/cwchar
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/cwchar/wcstol|Nazad]] | [[Языки программирования/C++/Библиотеки/<cwchar>/cwchar|cwchar]] | [[Языки программирования/C++/Библиотеки/cwchar/wcswcs|Vperyod]]
