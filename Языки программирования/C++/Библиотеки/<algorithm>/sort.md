# sort

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / sort

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/stable_sort|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class RandomIt>
void sort(RandomIt first, RandomIt last);

template<class RandomIt, class Compare>
void sort(RandomIt first, RandomIt last, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Итераторы определяющие диапазон для сортировки |
| `comp` | Функция сравнения. Должен возвращать true если первый аргумент должен идти раньше второго |

## Возвращаемое значение

Не возвращает значения.

## Что делает

Сортирует элементы в диапазоне `[first, last)` в порядке возрастания. Алгоритм нестабилен — равные элементы могут менять порядок. Использует алгоритм IntroSort (комбинация QuickSort, HeapSort и InsertionSort) с временной сложностью O(N log N).

## Примеры

### Базовое использование

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {5, 3, 1, 4, 2};

    std::sort(v.begin(), v.end());

    for (int x : v)
        std::cout << x << " ";
    // Вывод: 1 2 3 4 5
}
```

### С пользовательским компаратором

```cpp
std::vector<int> v = {5, 3, 1, 4, 2};
std::sort(v.begin(), v.end(), std::greater<int>());
// v: {5, 4, 3, 2, 1}
```

## Исключения

- **Исключения:** может бросать исключения при нехватке памяти (`std::bad_alloc`) или исключениях, брошенных компаратором.
- **Безопасность в C++11:** не определено стандартом — зависит от реализации.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/stable_sort|stable_sort]] — устойчивая сортировка
- [[Языки программирования/C++/Библиотеки/<algorithm>/partial_sort|partial_sort]] — частичная сортировка

## Источники

- https://en.cppreference.com/w/cpp/algorithm/sort
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/reverse_iterator|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/stable_sort|Вперёд]]
