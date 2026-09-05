# swap

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / swap

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/forward|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<class T>
void swap(T& a, T& b) noexcept(std::is_nothrow_move_constructible_v<T> && std::is_nothrow_move_assignable_v<T>);

template<class T, size_t N>
void swap(T (&a)[N], T (&b)[N]) noexcept(std::is_nothrow_swappable_v<T>);
```

## Параметры

| Параметр | Описание |
|---|---|
| `a` | Первое значение |
| `b` | Второе значение |

## Возвращаемое значение

Нет.

## Что делает

Обменивает значения `a` и `b`. Для массивов — поэлементный обмен.

## Примеры

```cpp
#include <utility>
#include <iostream>

int main()
{
    int a = 1, b = 2;
    std::swap(a, b);
    std::cout << a << " " << b << std::endl; // 2 1
}
```

## Исключения

- **Исключения:** условно noexcept (зависит от типа).

## Похожие функции

- `std::iter_swap` — обмен через итераторы

## Источники

- https://en.cppreference.com/w/cpp/utility/swap
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/forward|Вперёд]]
