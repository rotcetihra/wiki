# exists

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<filesystem>|<filesystem>]] / exists

[[Языки программирования/C++/Библиотеки/<filesystem>/directory_iterator|Назад]] | [[Языки программирования/C++/Библиотеки/<filesystem>|Содержание]] | [[Языки программирования/C++/Библиотеки/<filesystem>/is_block_file|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <filesystem>

bool exists(std::filesystem::file_status s) noexcept;
bool exists(const std::filesystem::path& p);
bool exists(const std::filesystem::path& p, std::error_code& ec) noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `p` | Путь для проверки |
| `s` | Статус файла |
| `ec` | Код ошибки |

## Возвращаемое значение

`true`, если файл или каталог существует.

## Что делает

Проверяет существование файла или каталога по указанному пути.

## Примеры

```cpp
#include <filesystem>
#include <iostream>

int main()
{
    namespace fs = std::filesystem;
    std::cout << std::boolalpha << fs::exists("/tmp") << std::endl; // true
    std::cout << std::boolalpha << fs::exists("/nonexistent") << std::endl; // false
}
```

## Исключения

- **Исключения:** без `error_code` — может бросать `filesystem_error`.

## Похожие функции

- `std::filesystem::status` — получение статуса

## Источники

- https://en.cppreference.com/w/cpp/filesystem/exists
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<filesystem>/directory_iterator|Назад]] | [[Языки программирования/C++/Библиотеки/<filesystem>|Содержание]] | [[Языки программирования/C++/Библиотеки/<filesystem>/is_block_file|Вперёд]]
