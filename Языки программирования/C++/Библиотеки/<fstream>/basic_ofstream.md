# basic_ofstream

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<fstream>|<fstream>]] / basic_ofstream

[[Языки программирования/C++/Библиотеки/<fstream>/basic_ifstream|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<fstream>/basic_fstream|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <fstream>
template<class CharT, class Traits = std::char_traits<CharT>>
class basic_ofstream : public std::basic_ostream<CharT, Traits>;
```

## Описание

Класс `std::basic_ofstream` предоставляет функциональность выходного потока для записи данных в файлы.

## Исключения

- **Исключения:** См. описание родительского класса.
- **Безопасность в C++11:** Не является потокобезопасным.

## Источники

- https://en.cppreference.com/w/cpp/header/fstream
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<fstream>/basic_ifstream|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<fstream>/basic_fstream|Вперёд]]
