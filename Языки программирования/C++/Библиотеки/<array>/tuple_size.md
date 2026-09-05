# tuple_size

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<array>|<array>]] / tuple_size

[[Языки программирования/C++/Библиотеки/<array>/get|Назад]] | [[Языки программирования/C++/Библиотеки/<array>|Содержание]] | [[Языки программирования/C++/Библиотеки/<array>/tuple_element|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
template<class T>
struct tuple_size;

template<class T, std::size_t N>
struct tuple_size<std::array<T, N>> : std::integral_constant<std::size_t, N> {};
```

Является вспомогательным типом для интеграции `std::array` с механизмом кортежей. Значение `value` равно `N`.

## Что делает

## Описание

Специализация `std::tuple_size` для `std::array<T, N>` позволяет получить размер массива в времени компиляции через `std::tuple_size_v<std::array<T, N>>` или `std::tuple_size<std::array<T, N>>::value`.

## Примеры

### Базовое использование

```cpp
```cpp
#include <array>
#include <iostream>
#include <tuple>

int main()
{
    using arr_t = std::array<int, 5>;
    std::cout << std::tuple_size_v<arr_t> << "\n"; // 5
}
```
```
- **Исключения:** не бросает исключений.

## Похожие типы

- [[Языки программирования/C++/Библиотеки/<tuple>|std::tuple_size]]

## Источники

- https://en.cppreference.com/w/cpp/header/<array>
- https://en.cppreference.com/w/cpp/header/<array>
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<array>/get|Назад]] | [[Языки программирования/C++/Библиотеки/<array>|Содержание]] | [[Языки программирования/C++/Библиотеки/<array>/tuple_element|Вперёд]]
