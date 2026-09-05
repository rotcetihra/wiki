# basic_ispanstream

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<iosfwd>|<iosfwd>]] / basic_ispanstream

[[Языки программирования/C++/Библиотеки/<iosfwd>/basic_spanbuf|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<iosfwd>/basic_ospanstream|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iosfwd>
template<class CharT, class Traits = std::char_traits<CharT>>
class basic_ispanstream : public std::basic_istream<CharT, Traits>;
```

## Описание

Класс `std::basic_ispanstream` предоставляет функциональность входного потока для чтения из `std::span`.

## Исключения

- **Исключения:** См. описание родительского класса.
- **Безопасность в C++11:** Не является потокобезопасным.

## Источники

- https://en.cppreference.com/w/cpp/header/iosfwd
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<iosfwd>/basic_spanbuf|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<iosfwd>/basic_ospanstream|Вперёд]]
