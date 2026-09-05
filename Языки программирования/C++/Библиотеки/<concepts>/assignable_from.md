# assignable_from

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<concepts>|<concepts>]] / assignable_from

[[Языки программирования/C++/Библиотеки/<concepts>/unsigned_integral|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/swappable|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <concepts>

template<class LHS, class RHS>
concept assignable_from =
    std::is_lvalue_reference_v<LHS> &&
    std::is_same_v<std::remove_reference_t<LHS>, std::remove_reference_t<RHS>> &&
    requires(LHS lhs, RHS&& rhs) {
        { lhs = std::forward<RHS>(rhs) } -> std::same_as<LHS>;
    };
```

## Описание

Концепт, проверяющий, что значение типа `RHS` можно присвоить ссылке на `LHS`.

## Примеры

```cpp
#include <concepts>
#include <string>

template<std::assignable_from<std::string> T>
void assign_str(T& dest, const std::string& src) {
    dest = src;
}
```

## Исключения

- **Исключения:** не применимо.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<concepts>/swappable|swappable]] — обмениваемость

## Источники

- https://en.cppreference.com/w/cpp/concepts/assignable_from
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<concepts>/unsigned_integral|Назад]] | [[Языки программирования/C++/Библиотеки/<concepts>|Содержание]] | [[Языки программирования/C++/Библиотеки/<concepts>/swappable|Вперёд]]
