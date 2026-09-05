# current_exception

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<exception>|<exception>]] / current_exception

[[Языки программирования/C++/Библиотеки/<exception>/terminate_handler|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<exception>/rethrow_exception|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <exception>
exception_ptr current_exception() noexcept;
```

## Возвращаемое значение

Значение `std::exception_ptr` или `nullptr`.

## Что делает

Возвращает указатель на текущее обрабатываемое исключение.

## Примеры

### Базовое использование

```cpp
std::exception_ptr eptr;
try { throw std::runtime_error("ошибка"); }
catch (...) { eptr = std::current_exception(); }
```

## Исключения

- **Исключения:** Не бросает исключений (`noexcept`).
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/exception
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<exception>/terminate_handler|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<exception>/rethrow_exception|Вперёд]]
