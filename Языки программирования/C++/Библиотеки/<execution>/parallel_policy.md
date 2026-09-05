# parallel_policy

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<execution>|<execution>]] / parallel_policy

[[Языки программирования/C++/Библиотеки/<execution>/sequenced_policy|Назад]] | [[Языки программирования/C++/Библиотеки/<execution>|Содержание]] | [[Языки программирования/C++/Библиотеки/<execution>/parallel_unsequenced_policy|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <execution>

class parallel_policy;
```

## Параметры

Нет.

## Возвращаемое значение

Политика, указывающая на параллельное выполнение с сохранением порядка элементов.

## Что делает

Указывает, что алгоритм может выполнять операции параллельно, но порядок элементов сохраняется.

## Примеры

```cpp
#include <execution>
#include <vector>
#include <algorithm>

int main()
{
    std::vector<int> v = {5, 3, 1, 4, 2};
    std::sort(std::execution::par, v.begin(), v.end());
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<execution>/parallel_unsequenced_policy|parallel_unsequenced_policy]] — параллельно без порядка

## Источники

- https://en.cppreference.com/w/cpp/execution/execution_policy
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<execution>/sequenced_policy|Назад]] | [[Языки программирования/C++/Библиотеки/<execution>|Содержание]] | [[Языки программирования/C++/Библиотеки/<execution>/parallel_unsequenced_policy|Вперёд]]
