# is_partitioned

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / is_partitioned

[[Языки программирования/C++/Библиотеки/<algorithm>/partition_copy|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/stable_partition|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt, class UnaryPredicate>
bool is_partitioned(InputIt first, InputIt last, UnaryPredicate p);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `p` | Унарный предикат |

## Возвращаемое значение

`true` если диапазон разбит предикатом `p`.

## Что делает

Проверяет, что все элементы, для которых `p` возвращает `true`, идут перед элементами, для которых `p` возвращает `false`.

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> v = {2, 4, 6, 1, 3, 5};

    bool result = std::is_partitioned(v.begin(), v.end(), [](int x){ return x % 2 == 0; }); // true
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/partition|partition]] — разбиение

## Источники

- https://en.cppreference.com/w/cpp/algorithm/is_partitioned
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/partition_copy|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/stable_partition|Вперёд]]
