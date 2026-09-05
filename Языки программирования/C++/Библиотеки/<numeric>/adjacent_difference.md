# adjacent_difference

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<numeric>|<numeric>]] / adjacent_difference

[[Языки программирования/C++/Библиотеки/<numeric>/inner_product|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<numeric>/partial_sum|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <numeric>
template<class InputIt, class OutputIt>
OutputIt adjacent_difference(InputIt first, InputIt last, OutputIt d_first);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first` | начало |
| `last` | конец |
| `d_first` | цель |

## Возвращаемое значение

Итератор на элемент за последним.

## Что делает

Вычисляет разностный ряд.

## Примеры

### Базовое использование

```cpp
std::vector<int> v={2,4,6,8,10}, r(5);
std::adjacent_difference(v.begin(),v.end(),r.begin());
// r = {2,2,2,2,2}
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/numeric
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<numeric>/inner_product|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<numeric>/partial_sum|Вперёд]]
