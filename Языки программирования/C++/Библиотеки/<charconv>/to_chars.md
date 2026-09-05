# to_chars

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<charconv>|<charconv>]] / to_chars

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<charconv>|Содержание]] | [[Языки программирования/C++/Библиотеки/<charconv>/from_chars|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <charconv>

std::to_chars_result to_chars(char* first, char* last,
                               int value, int base = 10);

std::to_chars_result to_chars(char* first, char* last,
                               long long value, int base = 10);

std::to_chars_result to_chars(char* first, char* last,
                               float value);
std::to_chars_result to_chars(char* first, char* last,
                               double value);
std::to_chars_result to_chars(char* first, char* last,
                               long double value);

std::to_chars_result to_chars(char* first, char* last,
                               float value, std::chars_format fmt);
std::to_chars_result to_chars(char* first, char* last,
                               double value, std::chars_format fmt);
std::to_chars_result to_chars(char* first, char* last,
                               long double value, std::chars_format fmt);

std::to_chars_result to_chars(char* first, char* last,
                               float value, std::chars_format fmt, int precision);
std::to_chars_result to_chars(char* first, char* last,
                               double value, std::chars_format fmt, int precision);
std::to_chars_result to_chars(char* first, char* last,
                               long double value, std::chars_format fmt, int precision);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Выходной символьный диапазон |
| `value` | Значение для преобразования |
| `base` | Основание системы счисления (2-36) |
| `fmt` | Формат представления числа |
| `precision` | Точность для плавающей точки |

## Возвращаемое значение

`std::to_chars_result` с полями `ptr` (итератор за последний записанный символ) и `ec` (код ошибки).

## Что делает

Преобразует числовое значение в символьное представление в указанном буфере. Самая быстрая функция преобразования чисел в строки — не использует heap и не бросает исключений.

## Примеры

```cpp
#include <charconv>
#include <array>
#include <iostream>

int main()
{
    char buf[20];
    auto [ptr, ec] = std::to_chars(buf, buf + sizeof(buf), 42);

    if (ec == std::errc{})
        std::cout << std::string_view(buf, ptr - buf) << std::endl; // 42
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<charconv>/from_chars|from_chars]] — разбор строки в число

## Источники

- https://en.cppreference.com/w/cpp/utility/to_chars
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки|Назад]] | [[Языки программирования/C++/Библиотеки/<charconv>|Содержание]] | [[Языки программирования/C++/Библиотеки/<charconv>/from_chars|Вперёд]]
