# nth_element

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / nth_element

[[Языки программирования/C++/Библиотеки/<algorithm>/partial_sort|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/is_sorted|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class RandomIt>
void nth_element(RandomIt first, RandomIt nth, RandomIt last);

template<class RandomIt, class Compare>
void nth_element(RandomIt first, RandomIt nth, RandomIt last, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first` | Начало диапазона |
| `nth` | Итератор на позицию n-го элемента |
| `last` | Конец диапазона |
| `comp` | Функция сравнения |

## Возвращаемое значение

Не возвращает значения.

## Что делает

Переставляет элементы таким образом, что элемент на позиции `nth` будет тем элементом, который стоял бы на этой позиции после полной сортировки. Элементы перед `nth` не больше него, после — не меньше. Временная сложность O(N) в среднем.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {5, 3, 1, 4, 2};

    std::nth_element(v.begin(), v.begin() + 2, v.end());

    std::cout << "Медиана: " << v[2] << std::endl;
    // Медиана: 3
}
```

## Исключения

- **Исключения:** может бросать исключения при нехватке памяти или исключениях компаратора.
- **Безопасность в C++11:** не определено стандартом.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/partial_sort|partial_sort]] — частичная сортировка
- [[Языки программирования/C++/Библиотеки/<algorithm>/sort|sort]] — полная сортировка

## Источники

- https://en.cppreference.com/w/cpp/algorithm/nth_element
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/partial_sort|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/is_sorted|Вперёд]]
