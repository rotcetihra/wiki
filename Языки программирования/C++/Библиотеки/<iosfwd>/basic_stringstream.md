# basic_stringstream

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<iosfwd>|<iosfwd>]] / basic_stringstream

[[Языки программирования/C++/Библиотеки/<iosfwd>/basic_ostringstream|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<iosfwd>/basic_spanbuf|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iosfwd>
template<class CharT, class Traits = std::char_traits<CharT>, class Allocator = std::allocator<CharT>>
class basic_stringstream : public std::basic_iostream<CharT, Traits>;
```

## Описание

Класс `std::basic_stringstream` предоставляет функциональность двунаправленного потока для чтения и записи данных в строку.

## Исключения

- **Исключения:** См. описание родительского класса.
- **Безопасность в C++11:** Не является потокобезопасным.

## Источники

- https://en.cppreference.com/w/cpp/header/iosfwd
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<iosfwd>/basic_ostringstream|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<iosfwd>/basic_spanbuf|Вперёд]]
