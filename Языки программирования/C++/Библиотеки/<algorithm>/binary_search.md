# binary_search

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / binary_search

[[Языки программирования/C++/Библиотеки/<algorithm>/is_sorted_until|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/lower_bound|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt, class T>
bool binary_search(ForwardIt first, ForwardIt last, const T& value);

template<class ForwardIt, class T, class Compare>
bool binary_search(ForwardIt first, ForwardIt last, const T& value, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Отсортированный диапазон итераторов |
| `value` | Искомое значение |
| `comp` | Функция сравнения |

## Возвращаемое значение

`true` если элемент найден, `false` в противном случае.

## Что делает

Выполняет бинарный поиск в отсортированном диапазоне. Временная сложность O(log N).

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> v = {1, 2, 3, 4, 5};

    bool found = std::binary_search(v.begin(), v.end(), 3); // true
    bool not_found = std::binary_search(v.begin(), v.end(), 6); // false
}
```

## Исключения

- **Исключения:** не бросает исключений (если компаратор не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/lower_bound|lower_bound]] — нижняя граница
- [[Языки программирования/C++/Библиотеки/<algorithm>/upper_bound|upper_bound]] — верхняя граница

## Источники

- https://en.cppreference.com/w/cpp/algorithm/binary_search
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/is_sorted_until|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/lower_bound|Вперёд]]
