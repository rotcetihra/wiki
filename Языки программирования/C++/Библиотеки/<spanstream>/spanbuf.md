# spanbuf

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<spanstream>|<spanstream>]] / spanbuf

[[Языки программирования/C++/Библиотеки/<spanstream>/ospanstream|Назад]] | [[Языки программирования/C++/Библиотеки/<spanstream>|Содержание]] | [[Языки программирования/C++/Библиотеки/<spanstream>/spanstreambuf|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <spanstream>

template<class CharT, class Traits = std::char_traits<CharT>>
class basic_spanbuf;

using spanbuf = basic_spanbuf<char>;
```

`std::spanbuf` — буфер потока, использующий `std::span` как буфер. Наследует `std::basic_streambuf`.

## Что делает



## Примеры

### Базовое использование

```cpp
// Пример использования spanbuf
```



## Источники

- https://en.cppreference.com/w/cpp/header/<spanstream>
- https://en.cppreference.com/w/cpp/header/<spanstream>
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<spanstream>/ospanstream|Назад]] | [[Языки программирования/C++/Библиотеки/<spanstream>|Содержание]] | [[Языки программирования/C++/Библиотеки/<spanstream>/spanstreambuf|Вперёд]]
