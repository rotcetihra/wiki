# declval

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / declval

[[Языки программирования/C++/Библиотеки/<utility>/move_if_noexcept|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/as_const|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<class T>
constexpr std::add_rvalue_reference_t<T> declval() noexcept;
```

## Параметры

Нет.

## Возвращаемое значение

Rvalue-ссылка на `T` (не может быть вызвана — используется только в unevaluated contexts).

## Что делает

Предоставляет выражение типа `T` для использования в unevaluated contexts (sizeof, decltype, SFINAE). Не может быть вызвана в runtime.

## Примеры

```cpp
#include <utility>
#include <type_traits>
#include <iostream>

int main()
{
    using type = decltype(std::declval<int>() + std::declval<double>());
    std::cout << std::is_same_v<type, double> << std::endl; // 1
}
```

## Исключения

- **Исключения:** не бросает исключений (никогда не вызывается).

## Похожие функции

- `sizeof` / `decltype` — unevaluated contexts

## Источники

- https://en.cppreference.com/w/cpp/utility/declval
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/move_if_noexcept|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/as_const|Вперёд]]
