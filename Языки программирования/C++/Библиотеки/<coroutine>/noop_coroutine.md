# noop_coroutine

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<coroutine>|<coroutine>]] / noop_coroutine

[[Языки программирования/C++/Библиотеки/<coroutine>/suspend_never|Назад]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Содержание]] | [[Языки программирования/C++/Библиотеки/<coroutine>/noop_coroutine_promise|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <coroutine>

constexpr std::noop_coroutine_handle noop_coroutine() noexcept;
```

## Параметры

Нет.

## Возвращаемое значение

`noop_coroutine_handle` — хэндл noop-корутины, которая ничего не делает при возобновлении.

## Что делает

Возвращает хэндл «пустой» корутины. `resume()` такой корутины — нет операции. Полезна как значение по умолчанию.

## Примеры

```cpp
#include <coroutine>
#include <iostream>

int main()
{
    auto h = std::noop_coroutine();
    std::cout << h.done() << std::endl; // 0 (не завершена)
    h.resume(); // ничего не делает
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<coroutine>/noop_coroutine_handle|noop_coroutine_handle]] — тип хэндла

## Источники

- https://en.cppreference.com/w/cpp/coroutine/noop_coroutine
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<coroutine>/suspend_never|Назад]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Содержание]] | [[Языки программирования/C++/Библиотеки/<coroutine>/noop_coroutine_promise|Вперёд]]
