# remove

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / remove

[[Языки программирования/C++/Библиотеки/<algorithm>/generate_n|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/remove_if|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class ForwardIt, class T>
ForwardIt remove(ForwardIt first, ForwardIt last, const T& value);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Диапазон итераторов |
| `value` | Значение для удаления |

## Возвращаемое значение

Итератор на «новый конец» диапазона без удалённых элементов.

## Что делает

Удаляет все элементы, равные `value`, из диапазона. Элементы сдвигаются, возвращаемый итератор указывает на конец оставшихся элементов.

## Примеры

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 2, 3, 2, 4, 2};

    auto new_end = std::remove(v.begin(), v.end(), 2);
    v.erase(new_end, v.end());
    // v: {1, 3, 4}
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/remove_if|remove_if]] — удаление по предикату
- [[Языки программирования/C++/Библиотеки/<algorithm>/remove_copy|remove_copy]] — копирование без удалённых

## Источники

- https://en.cppreference.com/w/cpp/algorithm/remove
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/generate_n|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/remove_if|Вперёд]]
