# wistringstream

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<sstream>|<sstream>]] / wistringstream

[[Языки программирования/C++/Библиотеки/<sstream>/wstringbuf|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<sstream>/wostringstream|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <sstream>
using wistringstream = std::basic_istringstream<wchar_t>;
```

## Описание

`std::wistringstream` — это псевдоним типа для `std::basic_istringstream<wchar_t>`.

## Исключения

- **Исключения:** См. описание родительского класса.
- **Безопасность в C++11:** Не является потокобезопасным.

## Источники

- https://en.cppreference.com/w/cpp/header/sstream
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<sstream>/wstringbuf|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<sstream>/wostringstream|Вперёд]]
