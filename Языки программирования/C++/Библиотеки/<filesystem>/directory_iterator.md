# directory_iterator

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<filesystem>|<filesystem>]] / directory_iterator

[[Языки программирования/C++/Библиотеки/<filesystem>/directory_entry|Назад]] | [[Языки программирования/C++/Библиотеки/<filesystem>|Содержание]] | [[Языки программирования/C++/Библиотеки/<filesystem>/recursive_directory_iterator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <filesystem>

class directory_iterator;
```

## Параметры

Нет.

## Возвращаемое значение

Итератор для перебора записей каталога (не рекурсивно).

## Что делает

Позволяет перебирать файлы и подкаталоги в указанном каталоге.

## Примеры

```cpp
#include <filesystem>
#include <iostream>

int main()
{
    namespace fs = std::filesystem;
    for (const auto& entry : fs::directory_iterator("."))
        std::cout << entry.path().filename() << std::endl;
}
```

## Исключения

- **Исключения:** может бросать `filesystem_error`.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<filesystem>/recursive_directory_iterator|recursive_directory_iterator]] — рекурсивный

## Источники

- https://en.cppreference.com/w/cpp/filesystem/directory_iterator
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<filesystem>/directory_entry|Назад]] | [[Языки программирования/C++/Библиотеки/<filesystem>|Содержание]] | [[Языки программирования/C++/Библиотеки/<filesystem>/recursive_directory_iterator|Вперёд]]
