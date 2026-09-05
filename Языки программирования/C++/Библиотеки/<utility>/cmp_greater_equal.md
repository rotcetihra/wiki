# cmp_greater_equal

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / cmp_greater_equal

[[Языки программирования/C++/Библиотеки/<utility>/cmp_less_equal|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/in_range|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<class T, class U>
constexpr bool cmp_greater_equal(T t, U u) noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `t` | Первое значение |
| `u` | Второе значение |

## Возвращаемое значение

`true`, если `t >= u`.

## Что делает

Безопасное сравнение «больше или равно» для знаковых и беззнаковых типов.

## Примеры

```cpp
#include <utility>
#include <iostream>

int main()
{
    int a = 5;
    unsigned int b = 3;
    std::cout << std::cmp_greater_equal(a, b) << std::endl; // 1
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<utility>/cmp_less_equal|cmp_less_equal]] — безопасное <=

## Источники

- https://en.cppreference.com/w/cpp/utility/int/cmp_greater_equal
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/cmp_less_equal|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/in_range|Вперёд]]
