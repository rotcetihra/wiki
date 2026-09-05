# noop_coroutine_handle

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<coroutine>|<coroutine>]] / noop_coroutine_handle

[[Языки программирования/C++/Библиотеки/<coroutine>/noop_coroutine_promise|Назад]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Содержание]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <coroutine>

using noop_coroutine_handle = coroutine_handle<noop_coroutine_promise>;
```

## Параметры

Нет.

## Возвращаемое значение

Алиас для `std::coroutine_handle<std::noop_coroutine_promise>`.

## Что делает

Тип хэндла для noop-корутины.

## Примеры

```cpp
#include <coroutine>
#include <iostream>

int main()
{
    std::noop_coroutine_handle h = std::noop_coroutine();
    std::cout << sizeof(h) << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<coroutine>/coroutine_handle|coroutine_handle]] — обобщённый хэндл

## Источники

- https://en.cppreference.com/w/cpp/coroutine/noop_coroutine_handle
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<coroutine>/noop_coroutine_promise|Назад]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Содержание]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Вперёд]]
