# derived_from

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / derived_from

[[Языки программирования/C++/Библиотеки/<concepts>/same_as|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/convertible_to|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class Derived, class Base>
concept derived_from =
    std::is_base_of_v<Base, Derived> &&
    std::is_convertible_v<const volatile Derived*, const volatile Base*>;
```

## Описание

Концепт, проверяющий, что `Derived` наследуется от `Base` (включая public, protected, private наследование).

## Примеры

```cpp
#include <concepts>
#include <iostream>

struct Base {};
struct Derived : Base {};

template<std::derived_from<Base> T>
void process(T&) { }

int main() {
    Derived d;
    process(d); // OK
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/convertible_to|convertible_to]] — преобразование типов

## Источники

- https://en.cppreference.com/w/cpp/concepts/derived_from
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/same_as|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/convertible_to|Вперёд]]
