# exception_ptr

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<exception>|<exception>]] / exception_ptr

[[Языки программирования/C++/Библиотеки/<exception>/nested_exception|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<exception>/terminate_handler|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <exception>
typedef /* unspecified */ exception_ptr;
```

## Возвращаемое значение

Не применимо (это тип).

## Что делает

Тип для хранения и передачи исключений между потоками.

## Примеры

### Базовое использование

```cpp
std::exception_ptr eptr;
try {
    throw std::runtime_error("ошибка");
} catch (...) {
    eptr = std::current_exception();
}
if (eptr) {
    try { std::rethrow_exception(eptr); }
    catch (const std::exception& e) { std::cout << e.what() << std::endl; }
}
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен для передачи.

## Источники

- https://en.cppreference.com/w/cpp/header/exception
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<exception>/nested_exception|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<exception>/terminate_handler|Вперёд]]
