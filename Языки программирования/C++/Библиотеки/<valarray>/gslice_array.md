# gslice_array

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<valarray>|<valarray>]] / gslice_array

[[Языки программирования/C++/Библиотеки/<valarray>/gslice|Назад]] | [[Языки программирования/C++/Библиотеки/<valarray>|Содержание]] | [[Языки программирования/C++/Библиотеки/<valarray>/mask_array|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <valarray>

template<class T>
class gslice_array;
```

## Параметры

| Параметр | Описание |
|---|---|
| `T` | Тип элементов |

## Возвращаемое значение

Класс-адаптер для доступа к элементам `valarray` через `gslice`.

## Что делает

Предоставляет доступ к подмножеству элементов `valarray`, определённому `gslice`.

## Примеры

```cpp
#include <valarray>
#include <iostream>

int main()
{
    std::valarray<int> v = {0,1,2,3,4,5,6,7,8,9};
    std::valarray<size_t> sizes = {2};
    std::valarray<size_t> strides = {3};
    v[std::gslice(0, sizes, strides)] = 99;
    for (int x : v) std::cout << x << " "; // 99 1 2 99 4 5 99 7 8 99
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<valarray>/slice_array|slice_array]] — для одномерного среза

## Источники

- https://en.cppreference.com/w/cpp/numeric/valarray/gslice_array
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<valarray>/gslice|Назад]] | [[Языки программирования/C++/Библиотеки/<valarray>|Содержание]] | [[Языки программирования/C++/Библиотеки/<valarray>/mask_array|Вперёд]]
