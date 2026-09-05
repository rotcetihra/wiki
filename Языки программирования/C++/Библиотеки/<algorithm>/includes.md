# includes

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / includes

[[Языки программирования/C++/Библиотеки/<algorithm>/set_symmetric_difference|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/min_element|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class InputIt1, class InputIt2>
bool includes(InputIt1 first1, InputIt1 last1,
              InputIt2 first2, InputIt2 last2);

template<class InputIt1, class InputIt2, class Compare>
bool includes(InputIt1 first1, InputIt1 last1,
              InputIt2 first2, InputIt2 last2, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first1`, `last1` | Первый отсортированный диапазон |
| `first2`, `last2` | Второй отсортированный диапазон |
| `comp` | Функция сравнения |

## Возвращаемое значение

`true` если все элементы второго диапазона есть в первом.

## Что делает

Проверяет, является ли один отсортированный диапазон подмножеством другого.

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> v1 = {1, 2, 3, 4, 5};
    std::vector<int> v2 = {2, 4};

    bool result = std::includes(v1.begin(), v1.end(), v2.begin(), v2.end()); // true
}
```

## Исключения

- **Исключения:** не бросает исключений (если компаратор не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/set_union|set_union]] — объединение множеств

## Источники

- https://en.cppreference.com/w/cpp/algorithm/includes
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/set_symmetric_difference|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/min_element|Вперёд]]
