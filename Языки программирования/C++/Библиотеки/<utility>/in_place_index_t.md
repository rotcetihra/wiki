# in_place_index_t

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / in_place_index_t

[[Языки программирования/C++/Библиотеки/<utility>/in_place_type|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/in_place_index|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<size_t I>
struct in_place_index_t {
    explicit in_place_index_t() = default;
};

template<size_t I>
inline constexpr in_place_index_t<I> in_place_index{};
```

## Параметры

| Параметр | Описание |
|---|---|
| `I` | Индекс для in-place конструирования |

## Возвращаемое значение

Тег `in_place_index_t<I>` и объект `in_place_index<I>`.

## Что делает

Тег для in-place конструирования с указанием индекса. Используется в `std::variant` для выбора альтернативы по индексу.

## Примеры

```cpp
#include <variant>
#include <iostream>

int main()
{
    std::variant<int, std::string> v(std::in_place_index<1>, "hello");
    std::cout << std::get<1>(v) << std::endl; // hello
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<utility>/in_place_type_t|in_place_type_t]] — с типом

## Источники

- https://en.cppreference.com/w/cpp/utility/in_place_index
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/in_place_type|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/in_place_index|Вперёд]]
