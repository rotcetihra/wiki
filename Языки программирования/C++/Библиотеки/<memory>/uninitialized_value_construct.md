# uninitialized_value_construct

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<memory>|<memory>]] / uninitialized_value_construct

[[Языки программирования/C++/Библиотеки/<memory>/uninitialized_default_construct|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<memory>/uninitialized_copy|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <memory>
template<class ForwardIt>
void uninitialized_value_construct(ForwardIt first, ForwardIt last);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first` | начало диапазона |
| `last` | конец диапазона |

## Возвращаемое значение

Ничего не возвращает.

## Что делает

Конструирование значением

## Примеры

### Базовое использование

```cpp
alignas(int) char buf[10*sizeof(int)];
auto f = reinterpret_cast<int*>(buf);
std::uninitialized_value_construct(f, f+10);
```

## Исключения

- **Исключения:** Выбрасывает при ошибке.
- **Безопасность в C++11:** Не является потокобезопасным.

## Источники

- https://en.cppreference.com/w/cpp/header/memory
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<memory>/uninitialized_default_construct|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<memory>/uninitialized_copy|Вперёд]]
