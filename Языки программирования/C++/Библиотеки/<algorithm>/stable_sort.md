# stable_sort

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / stable_sort

[[Языки программирования/C++/Библиотеки/<algorithm>/sort|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/partial_sort|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class RandomIt>
void stable_sort(RandomIt first, RandomIt last);

template<class RandomIt, class Compare>
void stable_sort(RandomIt first, RandomIt last, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Итераторы определяющие диапазон для сортировки |
| `comp` | Функция сравнения |

## Возвращаемое значение

Не возвращает значения.

## Что делает

Сортирует элементы в диапазоне `[first, last)` в порядке возрастания, сохраняя относительный порядок равных элементов (стабильная сортировка). Временная сложность O(N log² N).

## Примеры

### Базовое использование

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<std::pair<int, char>> v = {{1,'a'}, {2,'b'}, {1,'c'}, {2,'d'}};

    std::stable_sort(v.begin(), v.end());

    for (auto& p : v)
        std::cout << p.first << p.second << " ";
    // Вывод: 1a 1c 2b 2d — порядок равных элементов сохранён
}
```

## Исключения

- **Исключения:** может бросать исключения при нехватке памяти или исключениях компаратора.
- **Безопасность в C++11:** не определено стандартом.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/sort|sort]] — нестабильная сортировка
- [[Языки программирования/C++/Библиотеки/<algorithm>/partial_sort|partial_sort]] — частичная сортировка

## Источники

- https://en.cppreference.com/w/cpp/algorithm/stable_sort
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/sort|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/partial_sort|Вперёд]]
