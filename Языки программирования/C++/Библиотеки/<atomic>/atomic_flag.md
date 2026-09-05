# atomic_flag

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<atomic>|<atomic>]] / atomic_flag

[[Языки программирования/C++/Библиотеки/<atomic>/atomic|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_bool|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <atomic>

struct atomic_flag;
```

## Описание

`std::atomic_flag` — единственный атомарный тип, который гарантированно lock-free. Может хранить `true` или `false`.

## Методы

| Метод | Описание |
|---|---|
| `test_and_set(memory_order)` | Атомарно устанавливает `true` и возвращает предыдущее значение |
| `clear(memory_order)` | Атомарно устанавливает `false` |
| `test(memory_order)` | Атомарно читает текущее значение (C++20) |

## Примеры

```cpp
#include <atomic>
#include <iostream>
#include <thread>

std::atomic_flag flag = ATOMIC_FLAG_INIT;
int shared_data = 0;

void write_data()
{
    while (flag.test_and_set(std::memory_order_acquire))
        ;
    shared_data = 42;
    flag.clear(std::memory_order_release);
}

int main()
{
    std::thread t(write_data);
    t.join();
    std::cout << shared_data << std::endl; // 42
}
```

## Исключения

- **Исключения:** атомарные операции не бросают исключений.
- **Безопасность:** потокобезопасен поdesign.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<atomic>/atomic|atomic]] — шаблон атомарного типа

## Источники

- https://en.cppreference.com/w/cpp/atomic/atomic_flag
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<atomic>/atomic|Назад]] | [[Языки программирования/C++/Библиотеки/<atomic>|Содержание]] | [[Языки программирования/C++/Библиотеки/<atomic>/atomic_bool|Вперёд]]
