# basic_spanstream

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<iosfwd>|<iosfwd>]] / basic_spanstream

[[Языки программирования/C++/Библиотеки/<iosfwd>/basic_ospanstream|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | 

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iosfwd>
template<class CharT, class Traits = std::char_traits<CharT>>
class basic_spanstream : public std::basic_iostream<CharT, Traits>;
```

## Описание

Класс `std::basic_spanstream` предоставляет функциональность двунаправленного потока для чтения и записи через `std::span`.

## Исключения

- **Исключения:** См. описание родительского класса.
- **Безопасность в C++11:** Не является потокобезопасным.

## Источники

- https://en.cppreference.com/w/cpp/header/iosfwd
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<iosfwd>/basic_ospanstream|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | 
