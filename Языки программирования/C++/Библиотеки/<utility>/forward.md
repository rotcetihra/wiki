# forward

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / forward

[[Языки программирования/C++/Библиотеки/<utility>/swap|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/move|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<class T>
T&& forward(std::remove_reference_t<T>& arg) noexcept;

template<class T>
T&& forward(std::remove_reference_t<T>&& arg) noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `arg` | Значение для пересылки |

## Возвращаемое значение

`T&&` — forwarding reference.

## Что делает

Пересылает аргумент с сохранением его ссылочности (lvalue/rvalue). Используется в универсальных ссылках (forwarding references).

## Примеры

```cpp
#include <utility>
#include <iostream>

template<class T>
void wrapper(T&& arg) {
    target(std::forward<T>(arg));
}

void target(int&& x) { std::cout << "rvalue: " << x << std::endl; }
void target(const int& x) { std::cout << "lvalue: " << x << std::endl; }

int main() {
    int v = 42;
    wrapper(v);       // lvalue: 42
    wrapper(42);      // rvalue: 42
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<utility>/move|move]] — безусловное rvalue

## Источники

- https://en.cppreference.com/w/cpp/utility/forward
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/swap|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/move|Вперёд]]
