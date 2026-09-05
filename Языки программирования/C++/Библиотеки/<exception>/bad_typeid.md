# bad_typeid

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<exception>|<exception>]] / bad_typeid

[[Языки программирования/C++/Библиотеки/<exception>/bad_cast|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<exception>/bad_weak_ptr|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <exception>
#include <typeinfo>
class bad_typeid : public exception;
```

## Возвращаемое значение

Не применимо (это тип).

## Что делает

Исключение при `typeid` для nullptr.

## Примеры

### Базовое использование

```cpp
Base* p = nullptr;
try {
    const std::type_info& t = typeid(*p);
} catch (const std::bad_typeid& e) {
    std::cout << e.what() << std::endl;
}
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/exception
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<exception>/bad_cast|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<exception>/bad_weak_ptr|Вперёд]]
