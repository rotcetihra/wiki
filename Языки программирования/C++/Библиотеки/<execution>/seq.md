# seq

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<execution>|<execution>]] / seq

[[Языки программирования/C++/Библиотеки/<execution>/unsequenced_policy|Назад]] | [[Языки программирования/C++/Библиотеки/<execution>|Содержание]] | [[Языки программирования/C++/Библиотеки/<execution>/par|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <execution>

inline constexpr std::execution::sequenced_policy seq{};
```

## Параметры

Нет.

## Возвращаемое значение

Объект `sequenced_policy`.

## Что делает

Готовый объект политики последовательного выполнения. Используется как первый аргумент параллельных алгоритмов.

## Примеры

```cpp
#include <execution>
#include <vector>
#include <algorithm>

int main()
{
    std::vector<int> v = {5, 3, 1, 4, 2};
    std::sort(std::execution::seq, v.begin(), v.end());
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<execution>/par|par]] — параллельная политика

## Источники

- https://en.cppreference.com/w/cpp/execution/execution_policy
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<execution>/unsequenced_policy|Назад]] | [[Языки программирования/C++/Библиотеки/<execution>|Содержание]] | [[Языки программирования/C++/Библиотеки/<execution>/par|Вперёд]]
