# exclusive_scan

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<numeric>|<numeric>]] / exclusive_scan

[[Языки программирования/C++/Библиотеки/<numeric>/inclusive_scan|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<numeric>/transform_inclusive_scan|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <numeric>
template<class InputIt, class OutputIt>
OutputIt exclusive_scan(InputIt first, InputIt last, OutputIt d_first);
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

Эксклюзивное префиксное сканирование (C++17).

## Примеры

### Базовое использование

```cpp
std::vector<int> v={1,2,3,4,5}, r(5);
std::exclusive_scan(v.begin(),v.end(),r.begin());
// r = {0,1,3,6,10}
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/numeric
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<numeric>/inclusive_scan|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<numeric>/transform_inclusive_scan|Вперёд]]
