# get_id

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<thread>|<thread>]] / get_id

[[Языки программирования/C++/Библиотеки/<thread>/hardware_concurrency|Назад]] | [[Языки программирования/C++/Библиотеки/<thread>|Содержание]] | [[Языки программирования/C++/Библиотеки/<thread>/join|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <thread>

// std::thread
std::thread::id get_id() const noexcept;

// std::this_thread
std::thread::id get_id() noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| — | Параметров нет |

## Возвращаемое значение

`std::thread::id` — уникальный идентификатор потока.

## Что делает

Возвращает уникальный идентификатор потока. Для объекта `std::thread` возвращает ID запущенного потока (или знач по умолчанию, если поток не запущен). Функция `std::this_thread::get_id()` возвращает ID текущего потока.

Идентификаторы потоков можно использовать для сравнения и вывода.

## Примеры

### Базовое использование

```cpp
#include <thread>
#include <iostream>

void print_id() {
    std::cout << "Thread ID: " << std::this_thread::get_id() << "\n";
}

int main() {
    std::thread t(print_id);
    std::cout << "Main thread: " << std::this_thread::get_id() << "\n";
    std::cout << "New thread: " << t.get_id() << "\n";
    t.join();
}
```

## Исключения

- **Исключения:** Не бросает исключений.
- **Безопасность в C++11:** Потокобезопасна.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<thread>/hardware_concurrency|hardware_concurrency]] — количество аппаратных потоков

## Источники

- https://en.cppreference.com/w/cpp/thread/thread/get_id
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<thread>/hardware_concurrency|Назад]] | [[Языки программирования/C++/Библиотеки/<thread>|Содержание]] | [[Языки программирования/C++/Библиотеки/<thread>/join|Вперёд]]
