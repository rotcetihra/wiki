# coroutine_handle

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<coroutine>|<coroutine>]] / coroutine_handle

[[Языки программирования/C++/Библиотеки/<coroutine>/coroutine_traits|Назад]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Содержание]] | [[Языки программирования/C++/Библиотеки/<coroutine>/suspend_always|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <coroutine>

template<class Promise = void>
class coroutine_handle;
```

## Параметры

| Параметр | Описание |
|---|---|
| `Promise` | Тип promise-объекта (по умолчанию `void`) |

## Возвращаемое значение

Легковесный хэндл (указатель) на корутину.

## Что делает

Предоставляет интерфейс для управления корутиной: возобновление (`resume`), уничтожение (`destroy`), проверка завершённости (`done`), доступ к promise (`promise`).

## Примеры

```cpp
#include <coroutine>
#include <iostream>

struct Task {
    struct promise_type {
        Task get_return_object() {
            return {std::coroutine_handle<promise_type>::from_promise(*this)};
        }
        std::suspend_always initial_suspend() { return {}; }
        std::suspend_always final_suspend() noexcept { return {}; }
        void return_void() {}
        std::suspend_never yield_value(int) { return {}; }
    };
    std::coroutine_handle<promise_type> handle;
};

int main()
{
    std::cout << "coroutine_handle размер: " << sizeof(std::coroutine_handle<>) << std::endl;
}
```

## Исключения

- **Исключения:** `resume()` может бросать исключения.

## Похожие функции

- `std::coroutine_traits` — извлечение типов

## Источники

- https://en.cppreference.com/w/cpp/coroutine/coroutine_handle
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<coroutine>/coroutine_traits|Назад]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Содержание]] | [[Языки программирования/C++/Библиотеки/<coroutine>/suspend_always|Вперёд]]
