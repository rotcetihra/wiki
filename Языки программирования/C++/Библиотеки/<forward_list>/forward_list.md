# forward_list

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<forward_list>|<forward_list>]] / forward_list

[[Языки программирования/C++/Библиотеки/<forward_list>|Содержание]] | [[Языки программирования/C++/Библиотеки/<forward_list>/insert_after|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <forward_list>

template<class T, class Allocator = std::allocator<T>>
class forward_list;
```

`std::forward_list` — односвязный список. Элементы хранятся в узлах, связанных одним указателем. Поддерживает одностороннюю итерацию. Вставка/удаление в начало — O(1). Не имеет метода `size()` для экономии памяти.

## Что делает

## Параметры шаблона

| Параметр | Описание |
|---|---|
| `T` | Тип элементов |
| `Allocator` | Аллокатор памяти |

## Примеры

### Базовое использование

```cpp
```cpp
#include <forward_list>
#include <iostream>

int main()
{
    std::forward_list<int> fl = {1, 2, 3};
    fl.push_front(0);
    for (int x : fl) std::cout << x << ' '; // 0 1 2 3
}
```
```
- **Исключения:** конструкторы могут выбрасывать исключения.
- **Безопасность в C++11:** нет `operator[]`; безопасный доступ через итераторы.

## Похожие типы

- [[Языки программирования/C++/Библиотеки/<list>|<list>]]

## Источники

- https://en.cppreference.com/w/cpp/header/<forward_list>
- https://en.cppreference.com/w/cpp/header/<forward_list>
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<forward_list>|Содержание]] | [[Языки программирования/C++/Библиотеки/<forward_list>/insert_after|Вперёд]]
