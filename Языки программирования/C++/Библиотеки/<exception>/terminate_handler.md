# terminate_handler

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<exception>|<exception>]] / terminate_handler

[[Языки программирования/C++/Библиотеки/<exception>/exception_ptr|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<exception>/current_exception|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <exception>
typedef void (*terminate_handler)();
```

## Возвращаемое значение

Не применимо (это тип).

## Что делает

Тип обработчика, вызываемого при `std::terminate`.

## Примеры

### Базовое использование

```cpp
std::terminate_handler old = std::set_terminate([](){
    std::cerr << "Аварийное завершение!" << std::endl;
    std::abort();
});
std::set_terminate(old);
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/exception
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<exception>/exception_ptr|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<exception>/current_exception|Вперёд]]
