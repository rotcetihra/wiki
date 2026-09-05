# is_sorted_until

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / is_sorted_until

[[Языки программирования/C++/Библиотеки/<algorithm>/is_sorted|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/binary_search|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt>
ForwardIt is_sorted_until(ForwardIt first, ForwardIt last);

template<class ForwardIt, class Compare>
ForwardIt is_sorted_until(ForwardIt first, ForwardIt last, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Итераторы определяющие диапазон |
| `comp` | Функция сравнения |

## Возвращаемое значение

Итератор на последний элемент отсортированной последовательности.

## Что делает

Находит максимальный отсортированный префикс диапазона `[first, last)`. Возвращает итератор на элемент, следующий за последним отсортированным элементом.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 5, 3, 4};

    auto it = std::is_sorted_until(v.begin(), v.end());
    std::cout << "Отсортировано до: " << std::distance(v.begin(), it) << " элементов\n";
    // Отсортировано до: 3 элементов
}
```

## Исключения

- **Исключения:** не бросает исключений (если компаратор не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/is_sorted|is_sorted]] — проверка отсортированности

## Источники

- https://en.cppreference.com/w/cpp/algorithm/is_sorted_until
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/is_sorted|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/binary_search|Вперёд]]
