# tuple_element

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<array>|<array>]] / tuple_element

[[Языки программирования/C++/Библиотеки/<array>/tuple_size|Назад]] | [[Языки программирования/C++/Библиотеки/<array>|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
template<std::size_t I, class T>
struct tuple_element;

template<std::size_t I, class T, std::size_t N>
struct tuple_element<I, std::array<T, N>> {
    using type = T;
};
```

Вспомогательный тип для работы с `std::array` как с кортежем. Используется с `std::tuple_element_t<I, array<T, N>>`.

## Что делает

## Описание

Специализация `std::tuple_element` для `std::array<T, N>` позволяет получить тип элемента по индексу `I` в времени компиляции. Все элементы `std::array` имеют одинаковый тип `T`, поэтому `tuple_element<I, array<T, N>>::type` всегда равен `T`.

## Примеры

### Базовое использование

```cpp
```cpp
#include <array>
#include <iostream>
#include <tuple>

int main()
{
    using arr_t = std::array<double, 3>;
    std::tuple_element_t<0, arr_t> x = 1.5; // double
    std::cout << x << "\n";
}
```
```
- **Исключения:** не бросает исключений.

## Похожие типы

- [[Языки программирования/C++/Библиотеки/<tuple>|std::tuple_element]]

## Источники

- https://en.cppreference.com/w/cpp/header/<array>
- https://en.cppreference.com/w/cpp/header/<array>
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<array>/tuple_size|Назад]] | [[Языки программирования/C++/Библиотеки/<array>|Содержание]]
