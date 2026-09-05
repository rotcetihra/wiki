# chars_format

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<charconv>|<charconv>]] / chars_format

[[Языки программирования/C++/Библиотеки/<charconv>/from_chars|Назад]] | [[Языки программирования/C++/Библиотеки/<charconv>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <charconv>

enum class chars_format {
    scientific = /*implementation-defined*/,
    fixed      = /*implementation-defined*/,
    hex        = /*implementation-defined*/,
    general    = fixed | scientific
};
```

## Описание

Перечисление, определяющее формат представления чисел с плавающей точкой для `to_chars` и `from_chars`.

| Значение | Описание |
|---|---|
| `scientific` | Научная нотация: `1.23e+04` |
| `fixed` | Фиксированный: `12300.0` |
| `hex` | Шестнадцатеричный: `0x1.83p+13` |
| `general` | комбинация `fixed | scientific` |

## Примеры

```cpp
#include <charconv>
#include <array>
#include <iostream>

int main()
{
    char buf[50];
    double val = 12345.6789;

    auto [ptr1, ec1] = std::to_chars(buf, buf + sizeof(buf), val, std::chars_format::scientific, 2);
    std::cout << std::string_view(buf, ptr1 - buf) << std::endl; // 1.23e+04

    auto [ptr2, ec2] = std::to_chars(buf, buf + sizeof(buf), val, std::chars_format::fixed, 2);
    std::cout << std::string_view(buf, ptr2 - buf) << std::endl; // 12345.68
}
```

## Исключения

- **Исключения:** не применимо (перечисление).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<charconv>/to_chars|to_chars]] — преобразование числа в строку
- [[Языки программирования/C++/Библиотеки/<charconv>/from_chars|from_chars]] — разбор строки в число

## Источники

- https://en.cppreference.com/w/cpp/utility/chars_format
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<charconv>/from_chars|Назад]] | [[Языки программирования/C++/Библиотеки/<charconv>|Содержание]] | [[Языки программирования/C++/Библиотеки/<chrono>|Вперёд]]
