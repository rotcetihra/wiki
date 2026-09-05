# remove

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<filesystem>|<filesystem>]] / remove

[[Языки программирования/C++/Библиотеки/<filesystem>/create_directory|Назад]] | [[Языки программирования/C++/Библиотеки/<filesystem>|Содержание]] | [[Языки программирования/C++/Библиотеки/<filesystem>/remove_all|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <filesystem>

bool remove(const std::filesystem::path& p);
bool remove(const std::filesystem::path& p, std::error_code& ec) noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `p` | Путь к файлу или каталогу |

## Возвращаемое значение

`true` если удалено, `false` если не существовало.

## Что делает

Удаляет файл или пустой каталог.

## Примеры

```cpp
#include <filesystem>
#include <iostream>

int main()
{
    namespace fs = std::filesystem;
    bool removed = fs::remove("/tmp/test_file.txt");
    std::cout << std::boolalpha << removed << std::endl;
}
```

## Исключения

- **Исключения:** может бросать `filesystem_error`.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<filesystem>/remove_all|remove_all]] — рекурсивное удаление

## Источники

- https://en.cppreference.com/w/cpp/filesystem/remove
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<filesystem>/create_directory|Назад]] | [[Языки программирования/C++/Библиотеки/<filesystem>|Содержание]] | [[Языки программирования/C++/Библиотеки/<filesystem>/remove_all|Вперёд]]
