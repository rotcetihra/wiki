# constructible_from

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / constructible_from

[[Языки программирования/C++/Библиотеки/<concepts>/destructible|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/default_initializable|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class T, class... Args>
concept constructible_from =
    std::destructible<T> &&
    std::is_constructible_v<T, Args...>;
```

## Описание

Концепт, проверяющий, что объект типа `T` может быть сконструирован из аргументов `Args...`.

## Примеры

```cpp
#include <concepts>
#include <string>

template<std::constructible_from<std::string, const char*>>
void create_str() {
    std::string s("hello");
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/destructible|destructible]] — деструктурируемость

## Источники

- https://en.cppreference.com/w/cpp/concepts/constructible_from
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/destructible|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/default_initializable|Вперёд]]
