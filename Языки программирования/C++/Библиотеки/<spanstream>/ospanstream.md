# ospanstream

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<spanstream>|<spanstream>]] / ospanstream

[[Языки программирования/C++/Библиотеки/<spanstream>/ispanstream|Назад]] | [[Языки программирования/C++/Библиотеки/<spanstream>|Содержание]] | [[Языки программирования/C++/Библиотеки/<spanstream>/spanbuf|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <spanstream>

template<class CharT, class Traits = std::char_traits<CharT>>
class basic_ospanstream;

using ospanstream = basic_ospanstream<char>;
```

`std::ospanstream` — выходной поток, записывающий данные в `std::span`. Наследует `std::basic_ostream`.

## Что делает



## Примеры

### Базовое использование

```cpp
// Пример использования ospanstream
```



## Источники

- https://en.cppreference.com/w/cpp/header/<spanstream>
- https://en.cppreference.com/w/cpp/header/<spanstream>
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<spanstream>/ispanstream|Назад]] | [[Языки программирования/C++/Библиотеки/<spanstream>|Содержание]] | [[Языки программирования/C++/Библиотеки/<spanstream>/spanbuf|Вперёд]]
