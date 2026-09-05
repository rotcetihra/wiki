# convertible_to

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / convertible_to

[[Языки программирования/C++/Библиотеки/<concepts>/derived_from|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/integral|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class From, class To>
concept convertible_to =
    std::is_convertible_v<From, To> &&
    requires {
        static_cast<To>(std::declval<From>());
    };
```

## Описание

Концепт, проверяющий, что тип `From` преобразуется в `To` через `static_cast`.

## Примеры

```cpp
#include <concepts>

template<std::convertible_to<double> T>
double to_double(T value) {
    return static_cast<double>(value);
}

int main() {
    to_double(42);     // OK
    to_double(3.14f);  // OK
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/same_as|same_as]] — идентичность типов

## Источники

- https://en.cppreference.com/w/cpp/concepts/convertible_to
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/derived_from|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/integral|Вперёд]]
