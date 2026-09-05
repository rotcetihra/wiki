# unordered_set

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<unordered_set>|<unordered_set>]] / unordered_set

[[Языки программирования/C++/Библиотеки/<unordered_set>|Содержание]] | [[Языки программирования/C++/Библиотеки/<unordered_set>/insert|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <unordered_set>

template<class Key, class Hash = std::hash<Key>,
         class KeyEqual = std::equal_to<Key>,
         class Allocator = std::allocator<Key>>
class unordered_set;
```

`std::unordered_set` — множество на основе хеш-таблицы. Элементы уникальны. Средняя сложность поиска — O(1).

## Что делает

## Параметры шаблона

| Параметр | Описание |
|---|---|
| `Key` | Тип элементов |
| `Hash` | Хеш-функция |
| `KeyEqual` | Функция сравнения |
| `Allocator` | Аллокатор памяти |

## Примеры

### Базовое использование

```cpp
```cpp
#include <unordered_set>
#include <iostream>

int main()
{
    std::unordered_set<int> us = {5, 3, 1, 4, 2};
    for (int x : us) std::cout << x << ' ';
    std::cout << "\n";
}
```
```
- **Исключения:** вставка может выбросить `std::bad_alloc`.
- **Безопасность в C++11:** безопасный доступ через итераторы.

## Похожие типы

- [[Языки программирования/C++/Библиотеки/<set>|<set>]]

## Источники

- https://en.cppreference.com/w/cpp/header/<unordered_set>
- https://en.cppreference.com/w/cpp/header/<unordered_set>
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<unordered_set>|Содержание]] | [[Языки программирования/C++/Библиотеки/<unordered_set>/insert|Вперёд]]
