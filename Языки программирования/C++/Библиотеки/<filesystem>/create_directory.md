# create_directory

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<filesystem>|<filesystem>]] / create_directory

[[Языки программирования/C++/Библиотеки/<filesystem>/exists|Назад]] | [[Языки программирования/C++/Библиотеки/<filesystem>|Содержание]] | [[Языки программирования/C++/Библиотеки/<filesystem>/create_directories|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <filesystem>

bool create_directory(const std::filesystem::path& p);
bool create_directory(const std::filesystem::path& p, std::error_code& ec) noexcept;
bool create_directory(const std::filesystem::path& p, const std::filesystem::path& existing_p);
```

## Параметры

| Параметр | Описание |
|---|---|
| `p` | Путь нового каталога |
| `existing_p` | Каталог для копирования атрибутов |

## Возвращаемое значение

`true` если каталог создан, `false` если уже существует.

## Что делает

Создаёт новый каталог по указанному пути.

## Примеры

```cpp
#include <filesystem>
#include <iostream>

int main()
{
    namespace fs = std::filesystem;
    bool created = fs::create_directory("/tmp/test_dir");
    std::cout << std::boolalpha << created << std::endl; // true (или false если уже есть)
}
```

## Исключения

- **Исключения:** может бросать `filesystem_error`.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<filesystem>/create_directories|create_directories]] — рекурсивное создание

## Источники

- https://en.cppreference.com/w/cpp/filesystem/create_directory
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<filesystem>/exists|Назад]] | [[Языки программирования/C++/Библиотеки/<filesystem>|Содержание]] | [[Языки программирования/C++/Библиотеки/<filesystem>/create_directories|Вперёд]]
