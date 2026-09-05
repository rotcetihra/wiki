# is_sorted

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / is_sorted

[[Языки программирования/C++/Библиотеки/<algorithm>/nth_element|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/is_sorted_until|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt>
bool is_sorted(ForwardIt first, ForwardIt last);

template<class ForwardIt, class Compare>
bool is_sorted(ForwardIt first, ForwardIt last, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Итераторы определяющие диапазон |
| `comp` | Функция сравнения |

## Возвращаемое значение

`true` если диапазон отсортирован, `false` в противном случае.

## Что делает

Проверяет, отсортирован ли диапазон в порядке возрастания (или по компаратору `comp`). Временная сложность O(N).

## Примеры

```cpp
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> v1 = {1, 2, 3, 4, 5};
    std::vector<int> v2 = {5, 3, 1, 4, 2};

    bool b1 = std::is_sorted(v1.begin(), v1.end()); // true
    bool b2 = std::is_sorted(v2.begin(), v2.end()); // false
}
```

## Исключения

- **Исключения:** не бросает исключений (если компаратор не бросает).
- **Безопасность в C++11:** безопасна в многопоточной среде (read-only).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/is_sorted_until|is_sorted_until]] — первый неотсортированный элемент

## Источники

- https://en.cppreference.com/w/cpp/algorithm/is_sorted
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/nth_element|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/is_sorted_until|Вперёд]]
