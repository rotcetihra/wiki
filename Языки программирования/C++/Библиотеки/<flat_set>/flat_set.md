# flat_set

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<flat_set>|<flat_set>]] / flat_set

[[Языки программирования/C++/Библиотеки/<flat_set>|Содержание]] | [[Языки программирования/C++/Библиотеки/<flat_set>/insert|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <flat_set>

template<class Key, class Compare = std::less<Key>,
         class KeyContainer = std::vector<Key>>
class flat_set;
```

`std::flat_set` — плоское множество. Элементы хранятся в отсортированном порядке. Поиск — бинарный O(log n).

## Что делает

## Параметры шаблона

| Параметр | Описание |
|---|---|
| `Key` | Тип элементов |
| `Compare` | Функция сравнения |
| `KeyContainer` | Контейнер для хранения элементов |

## Примеры

### Базовое использование

```cpp
```cpp
#include <flat_set>
#include <iostream>

int main()
{
    std::flat_set<int> fs = {5, 3, 1, 4, 2};
    for (int x : fs) std::cout << x << ' '; // 1 2 3 4 5
}
```
```
- **Исключения:** вставка может выбросить `std::bad_alloc`.
- **Безопасность в C++11:** безопасный доступ.

## Похожие типы

- [[Языки программирования/C++/Библиотеки/<set>|<set>]]

## Источники

- https://en.cppreference.com/w/cpp/header/<flat_set>
- https://en.cppreference.com/w/cpp/header/<flat_set>
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<flat_set>|Содержание]] | [[Языки программирования/C++/Библиотеки/<flat_set>/insert|Вперёд]]
