# regex_error

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Библиотеки]] / [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/<regex>|<regex>]] / regex_error

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_constants|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/basic_regex|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <regex>
class regex_error : public runtime_error;
```

## Параметры

| Параметр | Описание |
|---|---|


## Возвращаемое значение

Исключение с описанием ошибки и кодом.

## Что делает

Бросается при ошибках компиляции или выполнения regex. Содержит код ошибки через `code()`.

## Примеры

### Базовое использование

```cpp
try {
    std::regex re("[");
} catch (const std::regex_error& e) {
    std::cout << "Regex error: " << e.what() << std::endl;
    std::cout << "Code: " << e.code() << std::endl;
}
```

## Исключения

- **Исключения:** Это само исключение.

## Источники

- https://en.cppreference.com/w/cpp/header/regex
- ISO/IEC 14882:2024

[[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/regex_constants|Назад]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки|Содержание]] | [[/home/rotcetihra/Рабочий стол/Проекты/wiki/Языки программирования/C++/Библиотеки/basic_regex|Вперёд]]
