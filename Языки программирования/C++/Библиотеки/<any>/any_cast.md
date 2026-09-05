# any_cast

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<any>|<any>]] / any_cast

[[Языки программирования/C++/Библиотеки/<any>/any|Назад]] | [[Языки программирования/C++/Библиотеки/<any>|Содержание]] | [[Языки программирования/C++/Библиотеки/<any>/make_any|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <any>

template<class T>
T any_cast(const any& operand);

template<class T>
T any_cast(any& operand);

template<class T>
T any_cast(any&& operand);

template<class T>
const T* any_cast(const any* operand) noexcept;

template<class T>
T* any_cast(any* operand) noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `operand` | Объект `any` для извлечения значения |

## Возвращаемое значение

Значение типа `T` (по значению, ссылке или указателю).

## Что делает

Извлекает значение из контейнера `any`. Если тип не совпадает, бросает `std::bad_any_cast`.

## Примеры

```cpp
#include <any>
#include <iostream>

int main()
{
    std::any a = 42;

    // По значению
    int val = std::any_cast<int>(a);

    // По указателю (без исключений)
    if (auto* p = std::any_cast<int>(&a))
        std::cout << *p << std::endl; // 42

    // Ошибка типа
    try {
        double d = std::any_cast<double>(a);
    } catch (const std::bad_any_cast& e) {
        std::cout << "Ошибка: " << e.what() << std::endl;
    }
}
```

## Исключения

- **Исключения:** по значению/ссылке — бросает `std::bad_any_cast` при несовпадении типа. По указателю — возвращает `nullptr` при несовпадении типа.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<any>/any|any]] — контейнер
- [[Языки программирования/C++/Библиотеки/<any>/make_any|make_any]] — создание объекта

## Источники

- https://en.cppreference.com/w/cpp/any/any_cast
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<any>/any|Назад]] | [[Языки программирования/C++/Библиотеки/<any>|Содержание]] | [[Языки программирования/C++/Библиотеки/<any>/make_any|Вперёд]]
