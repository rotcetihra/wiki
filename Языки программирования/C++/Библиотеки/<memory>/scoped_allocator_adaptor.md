# scoped_allocator_adaptor

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<memory>|<memory>]] / scoped_allocator_adaptor

[[Языки программирования/C++/Библиотеки/<memory>/uses_allocator|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<memory>/raw_storage_iterator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <memory>
template<class OuterAlloc, class... InnerAlloc>
class scoped_allocator_adaptor;
```

## Параметры

| Параметр | Описание |
|---|---|
| `OuterAlloc` | внешний аллокатор |
| `InnerAlloc` | внутренние аллокаторы |

## Возвращаемое значение

Не применимо (это тип).

## Что делает

Адаптер для автоматической передачи аллокатора.

## Примеры

### Базовое использование

```cpp
using Inner = std::allocator<int>;
using Outer = std::scoped_allocator_adaptor<Inner>;
```

## Исключения

- **Исключения:** Зависит от аллокатора.
- **Безопасность в C++11:** Потокобезопасен.

## Источники

- https://en.cppreference.com/w/cpp/header/memory
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<memory>/uses_allocator|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<memory>/raw_storage_iterator|Вперёд]]
