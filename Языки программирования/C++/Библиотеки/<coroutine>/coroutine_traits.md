# coroutine_traits

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<coroutine>|<coroutine>]] / coroutine_traits

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Содержание]] | [[Языки программирования/C++/Библиотеки/<coroutine>/coroutine_handle|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <coroutine>

template<class ReturnType, class... Args>
struct coroutine_traits;
```

## Параметры

| Параметр | Описание |
|---|---|
| `ReturnType` | Тип возвращаемого значения корутины |
| `Args` | Типы аргументов |

## Возвращаемое значение

Содержит `promise_type`, определённый для типа `ReturnType`.

## Что делает

Извлекает тип `promise_type` из типа возвращаемого значения корутины. Используется компилятором для создания корутины.

## Примеры

```cpp
#include <coroutine>
#include <iostream>

struct Task {
    struct promise_type {
        Task get_return_object() { return {}; }
        std::suspend_never initial_suspend() { return {}; }
        std::suspend_never final_suspend() noexcept { return {}; }
        void return_void() {}
        std::suspend_never yield_value(int) { return {}; }
    };
};

int main()
{
    using traits = std::coroutine_traits<Task>;
    std::cout << "promise_type определён" << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<coroutine>/coroutine_handle|coroutine_handle]] — хэндл корутины

## Источники

- https://en.cppreference.com/w/cpp/coroutine/coroutine_traits
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<coroutine>|Содержание]] | [[Языки программирования/C++/Библиотеки/<coroutine>/coroutine_handle|Вперёд]]
