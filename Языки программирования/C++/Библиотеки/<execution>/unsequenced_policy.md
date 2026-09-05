# unsequenced_policy

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<execution>|<execution>]] / unsequenced_policy

[[Языки программирования/C++/Библиотеки/<execution>/parallel_unsequenced_policy|Назад]] | [[Языки программирования/C++/Библиотеки/<execution>|Содержание]] | [[Языки программирования/C++/Библиотеки/<execution>/seq|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <execution>

class unsequenced_policy;
```

## Параметры

Нет.

## Возвращаемое значение

Политика, указывающая на выполнение без упорядоченности (но в одном потоке).

## Что делает

Позволяет компилятору переупорядочивать операции для оптимизации, но без параллелизма.

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

- [[Языки программирования/C++/Библиотеки/<execution>/sequenced_policy|sequenced_policy]] — с упорядоченностью

## Источники

- https://en.cppreference.com/w/cpp/execution/execution_policy
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<execution>/parallel_unsequenced_policy|Назад]] | [[Языки программирования/C++/Библиотеки/<execution>|Содержание]] | [[Языки программирования/C++/Библиотеки/<execution>/seq|Вперёд]]
