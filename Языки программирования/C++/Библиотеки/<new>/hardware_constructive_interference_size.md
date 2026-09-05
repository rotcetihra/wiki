# hardware_constructive_interference_size

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<new>|<new>]] / hardware_constructive_interference_size

[[Языки программирования/C++/Библиотеки/<new>/set_new_handler|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<new>/hardware_destructive_interference_size|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <new>
inline constexpr std::size_t hardware_constructive_interference_size = /* unspecified */;
```

## Возвращаемое значение

`constexpr std::size_t` — размер в байтах.

## Что делает

Минимальный размер кэш-линии для конструктивной интерференции.

## Примеры

### Базовое использование

```cpp
alignas(std::hardware_constructive_interference_size) int x;
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/new
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<new>/set_new_handler|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<new>/hardware_destructive_interference_size|Вперёд]]
