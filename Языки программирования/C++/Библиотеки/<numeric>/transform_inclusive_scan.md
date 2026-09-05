# transform_inclusive_scan

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<numeric>|<numeric>]] / transform_inclusive_scan

[[Языки программирования/C++/Библиотеки/<numeric>/exclusive_scan|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<numeric>/transform_exclusive_scan|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <numeric>
template<class InputIt, class OutputIt, class BinaryOp, class UnaryOp>
OutputIt transform_inclusive_scan(InputIt first, InputIt last, OutputIt d_first, BinaryOp b, UnaryOp u);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first` | начало |
| `last` | конец |
| `d_first` | цель |
| `b` | бинарная операция |
| `u` | унарное преобразование |

## Возвращаемое значение

Итератор на элемент за последним.

## Что делает

Инклюзивное сканирование с преобразованием (C++17).

## Примеры

### Базовое использование

```cpp
std::vector<int> v={1,2,3,4,5}, r(5);
std::transform_inclusive_scan(v.begin(),v.end(),r.begin(),std::plus<int>{},[](int x){return x*x;});
// r = {1,5,14,30,55}
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/numeric
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<numeric>/exclusive_scan|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<numeric>/transform_exclusive_scan|Вперёд]]
