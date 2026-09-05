# exchange

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / exchange

[[Языки программирования/C++/Библиотеки/<utility>/index_sequence_for|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/cmp_equal|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<class T, class U = T>
T exchange(T& obj, U&& new_value) noexcept(std::is_nothrow_move_constructible_v<T> && std::is_nothrow_assignable_v<T&, U>);
```

## Параметры

| Параметр | Описание |
|---|---|
| `obj` | Объект для замены |
| `new_value` | Новое значение |

## Возвращаемое значение

Старое значение `obj`.

## Что делает

Присваивает `new_value` объекту `obj` и возвращает его старое значение. Эквивалентно `T old = std::move(obj); obj = std::forward<U>(new_value); return old;`.

## Примеры

```cpp
#include <utility>
#include <iostream>

int main()
{
    int x = 5;
    int old = std::exchange(x, 10);
    std::cout << old << " " << x << std::endl; // 5 10
}
```

## Исключения

- **Исключения:** условно noexcept.

## Похожие функции

- `std::swap` — обмен двух объектов

## Источники

- https://en.cppreference.com/w/cpp/utility/exchange
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/index_sequence_for|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/cmp_equal|Вперёд]]
