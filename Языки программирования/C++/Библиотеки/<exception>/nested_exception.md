# nested_exception

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<exception>|<exception>]] / nested_exception

[[Языки программирования/C++/Библиотеки/<exception>/bad_weak_ptr|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<exception>/exception_ptr|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <exception>
class nested_exception;
```

## Возвращаемое значение

Не применимо (это тип).

## Что делает

Класс для построения цепочки исключений.

## Примеры

### Базовое использование

```cpp
try {
    try {
        throw std::runtime_error("ошибка");
    } catch (...) {
        std::throw_with_nested(std::runtime_error("контекст"));
    }
} catch (const std::exception& e) {
    std::cout << e.what() << std::endl;
    try { std::rethrow_if_nested(e); }
    catch (const std::exception& inner) {
        std::cout << "  -> " << inner.what() << std::endl;
    }
}
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/exception
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<exception>/bad_weak_ptr|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<exception>/exception_ptr|Вперёд]]
