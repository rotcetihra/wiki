# source_location

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<source_location>|<source_location>]] / source_location

[[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<source_location>/current|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <source_location>
class source_location;
```

## Возвращаемое значение

Не применимо (это тип).

## Что делает

Информация о месте в коде (файл, строка, функция).

## Примеры

### Базовое использование

```cpp
void log(const char* msg, std::source_location loc = std::source_location::current()) {
    std::cout << loc.file_name() << ":" << loc.line() << ": " << msg;
}
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/source_location
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<source_location>/current|Вперёд]]
