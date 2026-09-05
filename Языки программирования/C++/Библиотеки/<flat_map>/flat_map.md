# flat_map

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<flat_map>|<flat_map>]] / flat_map

[[Языки программирования/C++/Библиотеки/<flat_map>|Содержание]] | [[Языки программирования/C++/Библиотеки/<flat_map>/at|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <flat_map>

template<class Key, class T, class Compare = std::less<Key>,
         class KeyContainer = std::vector<Key>,
         class MappedContainer = std::vector<T>>
class flat_map;
```

`std::flat_map` — плоская ( массивная ) ассоциативная карта. Ключи хранятся в отсортированном порядке. Поиск — бинарный O(log n). Поддерживает итерацию в порядке ключей.

## Что делает

## Параметры шаблона

| Параметр | Описание |
|---|---|
| `Key` | Тип ключей |
| `T` | Тип значений |
| `Compare` | Функция сравнения ключей |
| `KeyContainer` | Контейнер для ключей |
| `MappedContainer` | Контейнер для значений |

## Примеры

### Базовое использование

```cpp
```cpp
#include <flat_map>
#include <iostream>

int main()
{
    std::flat_map<std::string, int> fm;
    fm["one"] = 1;
    fm["two"] = 2;
    std::cout << fm.at("one") << "\n"; // 1
}
```
```
- **Исключения:** `at()` выбрасывает `std::out_of_range`.
- **Безопасность в C++11:** безопасный доступ через `at()`.

## Похожие типы

- [[Языки программирования/C++/Библиотеки/<map>|<map>]]

## Источники

- https://en.cppreference.com/w/cpp/header/<flat_map>
- https://en.cppreference.com/w/cpp/header/<flat_map>
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<flat_map>|Содержание]] | [[Языки программирования/C++/Библиотеки/<flat_map>/at|Вперёд]]
