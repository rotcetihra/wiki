# suspend_always

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<coroutine>|<coroutine>]] / suspend_always

[[Языки программирования/C++/Библиотеки/<coroutine>/coroutine_handle|Назад]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Содержание]] | [[Языки программирования/C++/Библиотеки/<coroutine>/suspend_never|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <coroutine>

struct suspend_always {
    constexpr bool await_ready() noexcept { return false; }
    constexpr void await_suspend(std::coroutine_handle<>) noexcept {}
    constexpr void await_resume() noexcept {}
};
```

## Параметры

Нет.

## Возвращаемое значение

Аwaitable, который всегда приостанавливает корутину.

## Что делает

Представляет точку приостановки, которая всегда приостанавливает выполнение корутины (`await_ready()` возвращает `false`).

## Примеры

```cpp
#include <coroutine>
#include <iostream>

struct Task {
    struct promise_type {
        Task get_return_object() { return {}; }
        std::suspend_always initial_suspend() { return {}; } // приостановка при старте
        std::suspend_always final_suspend() noexcept { return {}; }
        void return_void() {}
    };
};
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<coroutine>/suspend_never|suspend_never]] — не приостанавливает

## Источники

- https://en.cppreference.com/w/cpp/coroutine/suspend_always
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<coroutine>/coroutine_handle|Назад]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Содержание]] | [[Языки программирования/C++/Библиотеки/<coroutine>/suspend_never|Вперёд]]
