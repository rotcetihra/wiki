# par_unseq

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<execution>|<execution>]] / par_unseq

[[Языки программирования/C++/Библиотеки/<execution>/par|Назад]] | [[Языки программирования/C++/Библиотеки/<execution>|Содержание]] | [[Языки программирования/C++/Библиотеки/<execution>/unseq|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <execution>

inline constexpr std::execution::parallel_unsequenced_policy par_unseq{};
```

## Параметры

Нет.

## Возвращаемое значение

Объект `parallel_unsequenced_policy`.

## Что делает

Готовый объект политики максимального параллелизма без упорядоченности.

## Примеры

```cpp
#include <execution>
#include <vector>
#include <algorithm>

int main()
{
    std::vector<int> v(10000);
    std::sort(std::execution::par_unseq, v.begin(), v.end());
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<execution>/unseq|unseq]] — без параллелизма

## Источники

- https://en.cppreference.com/w/cpp/execution/execution_policy
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<execution>/par|Назад]] | [[Языки программирования/C++/Библиотеки/<execution>|Содержание]] | [[Языки программирования/C++/Библиотеки/<execution>/unseq|Вперёд]]
