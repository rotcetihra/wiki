# current

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<source_location>|<source_location>]] / current

[[Языки программирования/C++/Библиотеки/<source_location>/source_location|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <source_location>
static constexpr source_location current(int delay = 0) noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `delay` | смещение кадра стека |

## Возвращаемое значение

`source_location` — информация о текущем месте.

## Что делает

Возвращает source_location для текущей точки вызова.

## Примеры

### Базовое использование

```cpp
auto loc = std::source_location::current();
std::cout << loc.file_name() << ":" << loc.line();
```

## Исключения

- **Исключения:** Не бросает исключений (`noexcept`).
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/source_location
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<source_location>/source_location|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
