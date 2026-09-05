# MATH_ERREXCEPT

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<cmath>|<cmath>]] / MATH_ERREXCEPT

[[Языки программирования/C++/Библиотеки/<cmath>/MATH_ERRNO|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/math_errhandling|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <cmath>

#define MATH_ERREXCEPT 2
```

## Параметры

Нет.

## Возвращаемое значение

Константа `2`.

## Что делает

Битовая маска для `math_errhandling`. Указывает, что математические функции должны генерировать исключения плавающей точки (FE_INVALID, FE_OVERFLOW и т. д.) при ошибках.

## Примеры

```cpp
#include <cmath>
#include <iostream>

int main()
{
    if (math_errhandling & MATH_ERREXCEPT)
        std::cout << "FP-исключения включены для math" << std::endl;
}
```

## Исключения

- **Исключения:** макрос определения, не функция.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<cmath>/MATH_ERRNO|MATH_ERRNO]] — установка errno
- [[Языки программирования/C++/Библиотеки/<cmath>/math_errhandling|math_errhandling]] — текущая политика

## Источники

- https://en.cppreference.com/w/cpp/numeric/math/math_errhandling
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<cmath>/MATH_ERRNO|Назад]] | [[Языки программирования/C++/Библиотеки/<cmath>|Содержание]] | [[Языки программирования/C++/Библиотеки/<cmath>/math_errhandling|Вперёд]]
