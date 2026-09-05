# endian

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<bit>|<bit>]] / endian

[[Языки программирования/C++/Библиотеки/<bit>/rotr|Назад]] | [[Языки программирования/C++/Библиотеки/<bit>|Содержание]] | [[Языки программирования/C++/Библиотеки/<charconv>|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <bit>

enum class endian : std::uint8_t {
    little = /*implementation-defined*/,
    big    = /*implementation-defined*/,
    native = /*implementation-defined*/
};
```

## Описание

Перечисление, определяющее порядок байтов платформы. Константы `little`, `big` и `native` позволяют определить endian-ность во время компиляции.

## Константы

| Константа | Описание |
|---|---|
| `endian::little` | Младший байт первым (x86, ARM) |
| `endian::big` | Старший байт первым (Network byte order) |
| `endian::native` | Порядок байтов текущей платформы |

## Примеры

```cpp
#include <bit>
#include <iostream>

int main()
{
    if constexpr (std::endian::native == std::endian::little)
        std::cout << "Little-endian" << std::endl;
    else
        std::cout << "Big-endian" << std::endl;
}
```

## Исключения

- **Исключения:** не применимо (перечисление).

## Источники

- https://en.cppreference.com/w/cpp/types/endian
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<bit>/rotr|Назад]] | [[Языки программирования/C++/Библиотеки/<bit>|Содержание]] | [[Языки программирования/C++/Библиотеки/<charconv>|Вперёд]]
