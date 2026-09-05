# par

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<execution>|<execution>]] / par

[[Языки программирования/C++/Библиотеки/<execution>/seq|Назад]] | [[Языки программирования/C++/Библиотеки/<execution>|Содержание]] | [[Языки программирования/C++/Библиотеки/<execution>/par_unseq|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <execution>

inline constexpr std::execution::parallel_policy par{};
```

## Параметры

Нет.

## Возвращаемое значение

Объект `parallel_policy`.

## Что делает

Готовый объект политики параллельного выполнения.

## Примеры

```cpp
#include <execution>
#include <vector>
#include <algorithm>

int main()
{
    std::vector<int> v(10000);
    std::sort(std::execution::par, v.begin(), v.end());
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<execution>/par_unseq|par_unseq]] — параллельно без порядка

## Источники

- https://en.cppreference.com/w/cpp/execution/execution_policy
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<execution>/seq|Назад]] | [[Языки программирования/C++/Библиотеки/<execution>|Содержание]] | [[Языки программирования/C++/Библиотеки/<execution>/par_unseq|Вперёд]]
