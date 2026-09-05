# in_place_type_t

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / in_place_type_t

[[Языки программирования/C++/Библиотеки/<utility>/in_place|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/in_place_type|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<class T>
struct in_place_type_t {
    explicit in_place_type_t() = default;
};

template<class T>
inline constexpr in_place_type_t<T> in_place_type{};
```

## Параметры

| Параметр | Описание |
|---|---|
| `T` | Тип для in-place конструирования |

## Возвращаемое значение

Тег `in_place_type_t<T>` и объект `in_place_type<T>`.

## Что делает

Тег для in-place конструирования с указанием типа. Используется в `std::any::emplace<T>`, `std::variant`, `std::optional`.

## Примеры

```cpp
#include <any>
#include <iostream>

int main()
{
    std::any a(std::in_place_type<int>, 42);
    std::cout << std::any_cast<int>(a) << std::endl; // 42
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<utility>/in_place_index_t|in_place_index_t]] — с индексом

## Источники

- https://en.cppreference.com/w/cpp/utility/in_place_type
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/in_place|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/in_place_type|Вперёд]]
