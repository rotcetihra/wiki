# copy_file

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<filesystem>|<filesystem>]] / copy_file

[[Языки программирования/C++/Библиотеки/<filesystem>/remove|Назад]] | [[Языки программирования/C++/Библиотеки/<filesystem>|Содержание]] | [[Языки программирования/C++/Библиотеки/<filesystem>/rename|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <filesystem>

bool copy_file(const std::filesystem::path& from, const std::filesystem::path& to);
bool copy_file(const std::filesystem::path& from, const std::filesystem::path& to, std::filesystem::copy_options options);
bool copy_file(const std::filesystem::path& from, const std::filesystem::path& to, std::error_code& ec) noexcept;
```

## Параметры

| Параметр | Описание |
|---|---|
| `from` | Исходный путь |
| `to` | Целевой путь |
| `options` | Опции копирования |

## Возвращаемое значение

`true` если файл успешно скопирован.

## Что делает

Копирует содержимое одного файла в другой.

## Примеры

```cpp
#include <filesystem>
#include <iostream>

int main()
{
    namespace fs = std::filesystem;
    bool ok = fs::copy_file("/tmp/a.txt", "/tmp/b.txt");
    std::cout << std::boolalpha << ok << std::endl;
}
```

## Исключения

- **Исключения:** может бросать `filesystem_error`.

## Похожие функции

- `std::filesystem::copy` — копирование (с каталогами)

## Источники

- https://en.cppreference.com/w/cpp/filesystem/copy_file
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<filesystem>/remove|Назад]] | [[Языки программирования/C++/Библиотеки/<filesystem>|Содержание]] | [[Языки программирования/C++/Библиотеки/<filesystem>/rename|Вперёд]]
