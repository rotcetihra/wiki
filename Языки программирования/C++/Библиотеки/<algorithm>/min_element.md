# min_element

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / min_element

[[Языки программирования/C++/Библиотеки/<algorithm>/includes|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/max_element|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt>
ForwardIt min_element(ForwardIt first, ForwardIt last);

template<class ForwardIt, class Compare>
ForwardIt min_element(ForwardIt first, ForwardIt last, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `comp` | Функция сравнения |

## Возвращаемое значение

Итератор на наименьший элемент в диапазоне.

## Что делает

Находит итератор на наименьший элемент в диапазоне `[first, last)`. Если диапазон пуст, возвращает `last`.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {5, 3, 1, 4, 2};

    auto it = std::min_element(v.begin(), v.end());
    std::cout << "Минимум: " << *it << std::endl; // 1
}
```

## Исключения

- **Исключения:** не бросает исключений (если компаратор не бросает).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/max_element|max_element]] — максимальный элемент
- [[Языки программирования/C++/Библиотеки/<algorithm>/minmax_element|minmax_element]] — минимальный и максимальный

## Источники

- https://en.cppreference.com/w/cpp/algorithm/min_element
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/includes|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/max_element|Вперёд]]
