# max_element

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / max_element

[[Языки программирования/C++/Библиотеки/<algorithm>/min_element|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/minmax_element|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt>
ForwardIt max_element(ForwardIt first, ForwardIt last);

template<class ForwardIt, class Compare>
ForwardIt max_element(ForwardIt first, ForwardIt last, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `comp` | Функция сравнения |

## Возвращаемое значение

Итератор на наибольший элемент в диапазоне.

## Что делает

Находит итератор на наибольший элемент в диапазоне `[first, last)`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {5, 3, 1, 4, 2};

    auto it = std::max_element(v.begin(), v.end());
    std::cout << "Максимум: " << *it << std::endl; // 5
}
```

## Исключения

- **Исключения:** не бросает исключений (если компаратор не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/min_element|min_element]] — минимальный элемент
- [[Языки программирования/C++/Библиотеки/<algorithm>/minmax_element|minmax_element]] — минимальный и максимальный

## Источники

- https://en.cppreference.com/w/cpp/algorithm/max_element
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/min_element|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/minmax_element|Вперёд]]
