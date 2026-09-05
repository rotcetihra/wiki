# same_as

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / same_as

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/derived_from|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class T, class U>
concept same_as = std::is_same_v<T, U> && std::is_same_v<U, T>;
```

## Описание

Концепт, проверяющий идентичность типов `T` и `U`.

## Примеры

```cpp
#include <concepts>
#include <iostream>

template<std::same_as<int> T>
void print_int(T value) {
    std::cout << value << std::endl;
}

int main() {
    print_int(42); // OK
    // print_int(3.14); // Ошибка: double не satisfied same_as<int>
}
```

## Исключения

- **Исключения:** не применимо (концепт времени компиляции).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/convertible_to|convertible_to]] — преобразование типов

## Источники

- https://en.cppreference.com/w/cpp/concepts/same_as
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/derived_from|Вперёд]]
