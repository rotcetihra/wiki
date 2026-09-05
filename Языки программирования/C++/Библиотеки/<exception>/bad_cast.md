# bad_cast

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<exception>|<exception>]] / bad_cast

[[Языки программирования/C++/Библиотеки/<exception>/bad_exception|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<exception>/bad_typeid|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <exception>
#include <typeinfo>
class bad_cast : public exception;
```

## Возвращаемое значение

Не применимо (это тип).

## Что делает

Исключение при неудачном `dynamic_cast` к ссылке.

## Примеры

### Базовое использование

```cpp
struct Base { virtual ~Base() = default; };
struct Derived : Base {};
Base* p = new Derived;
try {
    Derived& d = dynamic_cast<Derived&>(*p);
} catch (const std::bad_cast& e) {
    std::cout << e.what() << std::endl;
}
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/exception
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<exception>/bad_exception|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<exception>/bad_typeid|Вперёд]]
