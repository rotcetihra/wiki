# merge

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / merge

[[Языки программирования/C++/Библиотеки/<algorithm>/equal_range|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/inplace_merge|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt1, class InputIt2, class OutputIt>
OutputIt merge(InputIt1 first1, InputIt1 last1,
               InputIt2 first2, InputIt2 last2,
               OutputIt d_first);

template<class InputIt1, class InputIt2, class OutputIt, class Compare>
OutputIt merge(InputIt1 first1, InputIt1 last1,
               InputIt2 first2, InputIt2 last2,
               OutputIt d_first, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first1`, `last1` | Первый отсортированный диапазон |
| `first2`, `last2` | Второй отсортированный диапазон |
| `d_first` | Начало выходного диапазона |
| `comp` | Функция сравнения |

## Возвращаемое значение

Итератор за последний элемент выходного диапазона.

## Что делает

Сливает два отсортированных диапазона в один отсортированный выходной диапазон. Временная сложность O(N).

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v1 = {1, 3, 5};
    std::vector<int> v2 = {2, 4, 6};
    std::vector<int> result(6);

    std::merge(v1.begin(), v1.end(), v2.begin(), v2.end(), result.begin());
    // result: {1, 2, 3, 4, 5, 6}
}
```

## Исключения

- **Исключения:** может бросать исключения при нехватке памяти.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/inplace_merge|inplace_merge]] — слияние на месте

## Источники

- https://en.cppreference.com/w/cpp/algorithm/merge
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/equal_range|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/inplace_merge|Вперёд]]
