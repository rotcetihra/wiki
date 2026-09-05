# empty

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<array>|<array>]] / empty

[[Языки программирования/C++/Библиотеки/<array>/crend|Назад]] | [[Языки программирования/C++/Библиотеки/<array>|Содержание]] | [[Языки программирования/C++/Библиотеки/<array>/size|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
[[nodiscard]] constexpr bool empty() const noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|


## Возвращаемое значение

Возвращает `true`, если массив пуст (N == 0), иначе `false`.

## Что делает

Для `std::array` с `N > 0` всегда возвращает `false`.

## Примеры

### Базовое использование

```cpp
```cpp
#include <array>
#include <iostream>

int main()
{
    std::array<int, 0> empty_arr;
    std::array<int, 3> arr = {1, 2, 3};
    std::cout << std::boolalpha << empty_arr.empty() << "\n"; // true
    std::cout << arr.empty() << "\n";                         // false
}
```
```
- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<array>/size|size]]

## Источники

- https://en.cppreference.com/w/cpp/header/<array>
- https://en.cppreference.com/w/cpp/header/<array>
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<array>/crend|Назад]] | [[Языки программирования/C++/Библиотеки/<array>|Содержание]] | [[Языки программирования/C++/Библиотеки/<array>/size|Вперёд]]
