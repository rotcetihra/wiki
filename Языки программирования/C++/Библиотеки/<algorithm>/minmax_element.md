# minmax_element

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / minmax_element

[[Языки программирования/C++/Библиотеки/<algorithm>/max_element|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/clamp|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt>
std::pair<ForwardIt, ForwardIt>
    minmax_element(ForwardIt first, ForwardIt last);

template<class ForwardIt, class Compare>
std::pair<ForwardIt, ForwardIt>
    minmax_element(ForwardIt first, ForwardIt last, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `comp` | Функция сравнения |

## Возвращаемое значение

Пара итераторов `{наименьший, наибольший}`.

## Что делает

Находит минимальный и максимальный элементы за один проход. Количество сравнений: max(3/2(N-1), 0).

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {5, 3, 1, 4, 2};

    auto [min_it, max_it] = std::minmax_element(v.begin(), v.end());
    std::cout << "Мин: " << *min_it << ", Макс: " << *max_it << std::endl;
    // Мин: 1, Макс: 5
}
```

## Исключения

- **Исключения:** не бросает исключений (если компаратор не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/min_element|min_element]] — минимальный элемент
- [[Языки программирования/C++/Библиотеки/<algorithm>/max_element|max_element]] — максимальный элемент

## Источники

- https://en.cppreference.com/w/cpp/algorithm/minmax_element
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/max_element|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/clamp|Вперёд]]
