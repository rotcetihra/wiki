# as_const

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<utility>|<utility>]] / as_const

[[Языки программирования/C++/Библиотеки/<utility>/declval|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/pair|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <utility>

template<class T>
constexpr std::add_const_t<T>& as_const(T& t) noexcept;

template<class T>
void as_const(const T&&) = delete;
```

## Параметры

| Параметр | Описание |
|---|---|
| `t` | Ссылка на значение |

## Возвращаемое значение

`const T&` — константная ссылка.

## Что делает

Возвращает константную ссылку на значение. Запрещает rvalue-аргументы.

## Примеры

```cpp
#include <utility>
#include <string>

int main()
{
    std::string s = "hello";
    const std::string& cs = std::as_const(s);
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- `const_cast<const T&>(x)` — ручное приведение

## Источники

- https://en.cppreference.com/w/cpp/utility/as_const
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<utility>/declval|Назад]] | [[Языки программирования/C++/Библиотеки/<utility>|Содержание]] | [[Языки программирования/C++/Библиотеки/<utility>/pair|Вперёд]]
