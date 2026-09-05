# uninitialized_copy

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<memory>|<memory>]] / uninitialized_copy

[[Языки программирования/C++/Библиотеки/<memory>/uninitialized_value_construct|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<memory>/uninitialized_fill|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <memory>
template<class ForwardIt>
void uninitialized_copy(ForwardIt first, ForwardIt last);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first` | начало диапазона |
| `last` | конец диапазона |

## Возвращаемое значение

Ничего не возвращает.

## Что делает

Копирование в неинициализированную память

## Примеры

### Базовое использование

```cpp
int src[] = {1,2,3};
alignas(int) char buf[3*sizeof(int)];
auto d = reinterpret_cast<int*>(buf);
std::uninitialized_copy(src, src+3, d);
```

## Исключения

- **Исключения:** Выбрасывает при ошибке.
- **Безопасность в C++11:** Не является потокобезопасным.

## Источники

- https://en.cppreference.com/w/cpp/header/memory
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<memory>/uninitialized_value_construct|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<memory>/uninitialized_fill|Вперёд]]
