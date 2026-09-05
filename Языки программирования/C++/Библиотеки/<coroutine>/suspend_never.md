# suspend_never

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<coroutine>|<coroutine>]] / suspend_never

[[Языки программирования/C++/Библиотеки/<coroutine>/suspend_always|Назад]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Содержание]] | [[Языки программирования/C++/Библиотеки/<coroutine>/noop_coroutine|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <coroutine>

struct suspend_never {
    constexpr bool await_ready() noexcept { return true; }
    constexpr void await_suspend(std::coroutine_handle<>) noexcept {}
    constexpr void await_resume() noexcept {}
};
```

## Параметры

Нет.

## Возвращаемое значение

Awaitable, который никогда не приостанавливает корутину.

## Что делает

Представляет точку, которая не приостанавливает выполнение (`await_ready()` возвращает `true`).

## Примеры

```cpp
#include <coroutine>

struct Task {
    struct promise_type {
        Task get_return_object() { return {}; }
        std::suspend_never initial_suspend() { return {}; } // запуск сразу
        std::suspend_never final_suspend() noexcept { return {}; }
        void return_void() {}
    };
};
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<coroutine>/suspend_always|suspend_always]] — всегда приостанавливает

## Источники

- https://en.cppreference.com/w/cpp/coroutine/suspend_never
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<coroutine>/suspend_always|Назад]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Содержание]] | [[Языки программирования/C++/Библиотеки/<coroutine>/noop_coroutine|Вперёд]]
