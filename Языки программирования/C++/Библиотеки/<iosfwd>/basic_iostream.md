# basic_iostream

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<iosfwd>|<iosfwd>]] / basic_iostream

[[Языки программирования/C++/Библиотеки/<iosfwd>/basic_ostream|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<iosfwd>/basic_filebuf|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <iosfwd>
template<class CharT, class Traits = std::char_traits<CharT>>
class basic_iostream : public std::basic_istream<CharT, Traits>, public std::basic_ostream<CharT, Traits>;
```

## Описание

Класс `std::basic_iostream` является базовым классом для двунаправленных потоков. Он наследует `std::basic_istream` и `std::basic_ostream`.

## Исключения

- **Исключения:** См. описание родительского класса.
- **Безопасность в C++11:** Не является потокобезопасным.

## Источники

- https://en.cppreference.com/w/cpp/header/iosfwd
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<iosfwd>/basic_ostream|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<iosfwd>/basic_filebuf|Вперёд]]
