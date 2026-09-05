# in_place_type

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / in_place_type

[[Языки программирования/C++/Библиотеки/<utility>/in_place_type_t|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/in_place_index_t|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<class T>
inline constexpr in_place_type_t<T> in_place_type{};
```

## Параметры

| Параметр | Описание |
|---|---|
| `T` | Тип для in-place конструирования |

## Возвращаемое значение

Объект `in_place_type_t<T>`.

## Что делает

Объект тега для in-place конструирования с указанием типа.

## Примеры

```cpp
#include <variant>
#include <iostream>

int main()
{
    std::variant<int, std::string> v(std::in_place_type<std::string>, 5, 'a');
    std::cout << std::get<std::string>(v) << std::endl; // "aaaaa"
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<utility>/in_place_index|in_place_index]] — с индексом

## Источники

- https://en.cppreference.com/w/cpp/utility/in_place_type
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/in_place_type_t|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/in_place_index_t|Вперёд]]
