# set_intersection

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / set_intersection

[[Языки программирования/C++/Библиотеки/<algorithm>/set_union|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/set_difference|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt1, class InputIt2, class OutputIt>
OutputIt set_intersection(InputIt1 first1, InputIt1 last1,
                          InputIt2 first2, InputIt2 last2,
                          OutputIt d_first);

template<class InputIt1, class InputIt2, class OutputIt, class Compare>
OutputIt set_intersection(InputIt1 first1, InputIt1 last1,
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

Вычисляет пересечение двух отсортированных множеств.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v1 = {1, 2, 3, 4};
    std::vector<int> v2 = {3, 4, 5, 6};
    std::vector<int> result(2);

    auto it = std::set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(), result.begin());
    result.erase(it, result.end());
    // result: {3, 4}
}
```

## Исключения

- **Исключения:** не бросает исключений (если компаратор не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/set_union|set_union]] — объединение множеств
- [[Языки программирования/C++/Библиотеки/<algorithm>/set_difference|set_difference]] — разность множеств

## Источники

- https://en.cppreference.com/w/cpp/algorithm/set_intersection
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/set_union|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/set_difference|Вперёд]]
