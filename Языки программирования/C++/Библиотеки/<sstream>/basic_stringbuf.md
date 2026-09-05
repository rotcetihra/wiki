# basic_stringbuf

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<sstream>|<sstream>]] / basic_stringbuf

 | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<sstream>/basic_istringstream|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <sstream>
template<class CharT, class Traits = std::char_traits<CharT>, class Allocator = std::allocator<CharT>>
class basic_stringbuf : public std::basic_streambuf<CharT, Traits>;
```

## Описание

Класс `std::basic_stringbuf` реализует буфер для строкового ввода-вывода. Данные хранятся в объекте `std::basic_string`.

## Исключения

- **Исключения:** См. описание родительского класса.
- **Безопасность в C++11:** Не является потокобезопасным.

## Источники

- https://en.cppreference.com/w/cpp/header/sstream
- ISO/IEC 14882:2024

 | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<sstream>/basic_istringstream|Вперёд]]
