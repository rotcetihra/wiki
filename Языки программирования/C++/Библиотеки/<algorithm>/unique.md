# unique

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / unique

[[Языки программирования/C++/Библиотеки/<algorithm>/shuffle|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/unique_copy|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt>
ForwardIt unique(ForwardIt first, ForwardIt last);

template<class ForwardIt, class BinaryPredicate>
ForwardIt unique(ForwardIt first, ForwardIt last, BinaryPredicate p);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `p` | Бинарный предикат |

## Возвращаемое значение

Итератор на «новый конец» диапазона.

## Что делает

Удаляет все кроме первого подряд идущего элемента из каждой группы равных элементов. Диапазон должен быть отсортирован для полного удаления дубликатов.

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> v = {1, 1, 2, 2, 3, 3, 3};

    auto new_end = std::unique(v.begin(), v.end());
    v.erase(new_end, v.end());
    // v: {1, 2, 3}
}
```

## Исключения

- **Исключения:** не бросает исключений (если предикат не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/unique_copy|unique_copy]] — копирование уникальных элементов

## Источники

- https://en.cppreference.com/w/cpp/algorithm/unique
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/shuffle|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/unique_copy|Вперёд]]
