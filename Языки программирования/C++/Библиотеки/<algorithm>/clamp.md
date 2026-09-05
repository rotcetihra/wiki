# clamp

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<algorithm>|<algorithm>]] / clamp

[[Языки программирования/C++/Библиотеки/<algorithm>/minmax_element|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/all_of|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <algorithm>

template<class T>
constexpr const T& clamp(const T& v, const T& lo, const T& hi);

template<class T, class Compare>
constexpr const T& clamp(const T& v, const T& lo, const T& hi, Compare comp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `v` | Значение для ограничения |
| `lo` | Нижняя граница |
| `hi` | Верхняя граница |
| `comp` | Функция сравнения |

## Возвращаемое значение

`v`, `lo` или `hi` — значение, попадающее в диапазон `[lo, hi]`.

## Что делает

Ограничивает значение `v` диапазоном `[lo, hi]`. Если `v < lo`, возвращает `lo`; если `v > hi`, возвращает `hi`. Если `lo > hi`, поведение не определено.

## Примеры

```cpp
#include <algorithm>
#include <iostream>

int main()
{
    int x = 15;
    int result = std::clamp(x, 0, 10);
    std::cout << result << std::endl; // 10
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<algorithm>/min_element|min_element]] — минимальный элемент
- [[Языки программирования/C++/Библиотеки/<algorithm>/max_element|max_element]] — максимальный элемент

## Источники

- https://en.cppreference.com/w/cpp/algorithm/clamp
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<algorithm>/minmax_element|Назад]] | [[Языки программирования/C++/Библиотеки/<algorithm>|Содержание]] | [[Языки программирования/C++/Библиотеки/<algorithm>/all_of|Вперёд]]
