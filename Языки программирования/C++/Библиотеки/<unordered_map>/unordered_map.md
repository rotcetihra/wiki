# unordered_map

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<unordered_map>|<unordered_map>]] / unordered_map

[[Языки программирования/C++/Библиотеки/<unordered_map>|Содержание]] | [[Языки программирования/C++/Библиотеки/<unordered_map>/at|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <unordered_map>

template<class Key, class T, class Hash = std::hash<Key>,
         class KeyEqual = std::equal_to<Key>,
         class Allocator = std::allocator<std::pair<const Key, T>>>
class unordered_map;
```

`std::unordered_map` — хеш-таблица. Ключи уникальны. Средняя сложность поиска — O(1). Итераторы инвалидируются при `rehash`.

## Что делает

## Параметры шаблона

| Параметр | Описание |
|---|---|
| `Key` | Тип ключей |
| `T` | Тип значений |
| `Hash` | Хеш-функция |
| `KeyEqual` | Функция сравнения ключей |
| `Allocator` | Аллокатор памяти |

## Примеры

### Базовое использование

```cpp
```cpp
#include <unordered_map>
#include <iostream>

int main()
{
    std::unordered_map<std::string, int> um;
    um["one"] = 1;
    um["two"] = 2;
    std::cout << um.at("one") << "\n"; // 1
}
```
```
- **Исключения:** `at()` выбрасывает `std::out_of_range`.
- **Безопасность в C++11:** безопасный доступ через `at()`.

## Похожие типы

- [[Языки программирования/C++/Библиотеки/<map>|<map>]]

## Источники

- https://en.cppreference.com/w/cpp/header/<unordered_map>
- https://en.cppreference.com/w/cpp/header/<unordered_map>
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<unordered_map>|Содержание]] | [[Языки программирования/C++/Библиотеки/<unordered_map>/at|Вперёд]]
