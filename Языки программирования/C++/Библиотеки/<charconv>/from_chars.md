# from_chars

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<charconv>|<charconv>]] / from_chars

[[Языки программирования/C++/Библиотеки/<charconv>/to_chars|Назад]] | [[Языки программирования/C++/Библиотеки/<charconv>|Содержание]] | [[Языки программирования/C++/Библиотеки/<charconv>/chars_format|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <charconv>

std::from_chars_result from_chars(const char* first, const char* last,
                                   int& value, int base = 10);

std::from_chars_result from_chars(const char* first, const char* last,
                                   long long& value, int base = 10);

std::from_chars_result from_chars(const char* first, const char* last,
                                   float& value,
                                   std::chars_format fmt = std::chars_format::general);
std::from_chars_result from_chars(const char* first, const char* last,
                                   double& value,
                                   std::chars_format fmt = std::chars_format::general);
std::from_chars_result from_chars(const char* first, const char* last,
                                   long double& value,
                                   std::chars_format fmt = std::chars_format::general);
```

## Параметры

| Параметр | Описание |
|---|---|
| `first`, `last` | Входной символьный диапазон |
| `value` | Выходное значение |
| `base` | Основание системы счисления (2-36) |
| `fmt` | Формат разбираемого числа |

## Возвращаемое значение

`std::from_chars_result` с полями `ptr` (итератор на непереданный символ) и `ec` (код ошибки).

## Что делает

Разбирает числовое значение из символьного диапазона. Самая быстрая функция разбора чисел из строк.

## Примеры

```cpp
#include <charconv>
#include <string_view>
#include <iostream>

int main()
{
    std::string_view sv = "42abc";
    int value;

    auto [ptr, ec] = std::from_chars(sv.data(), sv.data() + sv.size(), value);

    if (ec == std::errc{})
        std::cout << value << std::endl; // 42
}
```

## Исключения

- **Исключения:** не бросает исключений.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<charconv>/to_chars|to_chars]] — преобразование числа в строку

## Источники

- https://en.cppreference.com/w/cpp/utility/from_chars
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<charconv>/to_chars|Назад]] | [[Языки программирования/C++/Библиотеки/<charconv>|Содержание]] | [[Языки программирования/C++/Библиотеки/<charconv>/chars_format|Вперёд]]
