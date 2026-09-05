# unseq

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<execution>|<execution>]] / unseq

[[Языки программирования/C++/Библиотеки/<execution>/par_unseq|Назад]] | [[Языки программирования/C++/Библиотеки/<execution>|Содержание]] | [[Языки программирования/C++/Библиотеки/<execution>/is_execution_policy|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <execution>

inline constexpr std::execution::unsequenced_policy unseq{};
```

## Параметры

Нет.

## Возвращаемое значение

Объект `unsequenced_policy`.

## Что делает

Готовый объект политики выполнения без упорядоченности (но в одном потоке).

## Примеры

```cpp
#include <execution>
#include <vector>
#include <algorithm>

int main()
{
    std::vector<int> v = {5, 3, 1, 4, 2};
    std::for_each(std::execution::unseq, v.begin(), v.end(), [](int& x){ x *= 2; });
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<execution>/seq|seq]] — с упорядоченностью

## Источники

- https://en.cppreference.com/w/cpp/execution/execution_policy
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<execution>/par_unseq|Назад]] | [[Языки программирования/C++/Библиотеки/<execution>|Содержание]] | [[Языки программирования/C++/Библиотеки/<execution>/is_execution_policy|Вперёд]]
