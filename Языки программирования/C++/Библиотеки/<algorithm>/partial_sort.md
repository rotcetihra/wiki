# partial_sort

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / partial_sort

[[Языки программирования/C++/Библиотеки/<algorithm>/stable_sort|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/nth_element|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class RandomIt>
void partial_sort(RandomIt first, RandomIt middle, RandomIt last);

template<class RandomIt, class Compare>
void partial_sort(RandomIt first, RandomIt middle, RandomIt last, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first` | Начало диапазона |
| `middle` | Конец отсортированной части |
| `last` | Конец диапазона |
| `comp` | Функция сравнения |

## Возвращаемое значение

Не возвращает значения.

## Что делает

Сортирует N = middle - first наименьших элементов из диапазона `[first, last)`. Остальные элементы остаются в unspecified порядке. Эффективнее полной сортировки, если нужны только первые N элементов.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {5, 3, 1, 4, 2};

    std::partial_sort(v.begin(), v.begin() + 3, v.end());

    for (int x : v)
        std::cout << x << " ";
    // Вывод: 1 2 3 5 4 — первые 3 элемента отсортированы
}
```

## Исключения

- **Исключения:** может бросать исключения при нехватке памяти или исключениях компаратора.
- **Безопасность в C++11:** не определено стандартом.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/sort|sort]] — полная сортировка
- [[Языки программирования/C++/Библиотеки/<algorithm>/nth_element|nth_element]] — нахождение n-го элемента

## Источники

- https://en.cppreference.com/w/cpp/algorithm/partial_sort
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/stable_sort|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/nth_element|Вперёд]]
