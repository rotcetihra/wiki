# basic_istringstream

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<sstream>|<sstream>]] / basic_istringstream

[[Языки программирования/C++/Библиотеки/<sstream>/basic_stringbuf|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<sstream>/basic_ostringstream|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <sstream>
template<class CharT, class Traits = std::char_traits<CharT>, class Allocator = std::allocator<CharT>>
class basic_istringstream : public std::basic_istream<CharT, Traits>;
```

## Описание

Класс `std::basic_istringstream` предоставляет функциональность входного потока для чтения данных из строки.

## Исключения

- **Исключения:** См. описание родительского класса.
- **Безопасность в C++11:** Не является потокобезопасным.

## Источники

- https://en.cppreference.com/w/cpp/header/sstream
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<sstream>/basic_stringbuf|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<sstream>/basic_ostringstream|Вперёд]]
