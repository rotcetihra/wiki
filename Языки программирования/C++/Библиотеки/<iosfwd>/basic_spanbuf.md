# basic_spanbuf

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<iosfwd>|<iosfwd>]] / basic_spanbuf

[[Языки программирования/C++/Библиотеки/<iosfwd>/basic_stringstream|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<iosfwd>/basic_ispanstream|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iosfwd>
template<class CharT, class Traits = std::char_traits<CharT>>
class basic_spanbuf : public std::basic_streambuf<CharT, Traits>;
```

## Описание

Класс `std::basic_spanbuf` реализует буфер для работы со `std::span`.

## Исключения

- **Исключения:** См. описание родительского класса.
- **Безопасность в C++11:** Не является потокобезопасным.

## Источники

- https://en.cppreference.com/w/cpp/header/iosfwd
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<iosfwd>/basic_stringstream|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<iosfwd>/basic_ispanstream|Вперёд]]
