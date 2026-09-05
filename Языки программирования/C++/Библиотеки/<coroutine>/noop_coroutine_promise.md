# noop_coroutine_promise

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<coroutine>|<coroutine>]] / noop_coroutine_promise

[[Языки программирования/C++/Библиотеки/<coroutine>/noop_coroutine|Назад]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Содержание]] | [[Языки программирования/C++/Библиотеки/<coroutine>/noop_coroutine_handle|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <coroutine>

struct noop_coroutine_promise {};
```

## Параметры

Нет.

## Возвращаемое значение

Тип promise для noop-корутины.

## Что делает

Promise-тип дляnoop-корутины. Не содержит операций.

## Примеры

```cpp
#include <coroutine>
#include <iostream>

int main()
{
    std::noop_coroutine_promise p;
    std::cout << "noop_promise создан" << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<coroutine>/noop_coroutine|noop_coroutine]] — создание noop-корутины

## Источники

- https://en.cppreference.com/w/cpp/coroutine/noop_coroutine_promise
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<coroutine>/noop_coroutine|Назад]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Содержание]] | [[Языки программирования/C++/Библиотеки/<coroutine>/noop_coroutine_handle|Вперёд]]
