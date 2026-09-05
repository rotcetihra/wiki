# bad_optional_access

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<optional>|<optional>]] / bad_optional_access

[[Языки программирования/C++/Библиотеки/<optional>/nullopt_t|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<optional>/make_optional|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <optional>
class bad_optional_access : public std::exception;
```

## Возвращаемое значение

Не применимо (это тип).

## Что делает

Исключение при доступе к пустому optional.

## Примеры

### Базовое использование

```cpp
std::optional<int> opt;
try { int v = opt.value(); }
catch (const std::bad_optional_access& e) { std::cout << e.what(); }
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/optional
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<optional>/nullopt_t|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<optional>/make_optional|Вперёд]]
