# basic_ifstream

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<fstream>|<fstream>]] / basic_ifstream

[[Языки программирования/C++/Библиотеки/<fstream>/basic_filebuf|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<fstream>/basic_ofstream|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <fstream>
template<class CharT, class Traits = std::char_traits<CharT>>
class basic_ifstream : public std::basic_istream<CharT, Traits>;
```

## Описание

Класс `std::basic_ifstream` предоставляет функциональность входного потока для чтения данных из файлов.

## Исключения

- **Исключения:** См. описание родительского класса.
- **Безопасность в C++11:** Не является потокобезопасным.

## Источники

- https://en.cppreference.com/w/cpp/header/fstream
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<fstream>/basic_filebuf|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<fstream>/basic_ofstream|Вперёд]]
