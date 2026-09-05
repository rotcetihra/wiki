# directory_entry

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<filesystem>|<filesystem>]] / directory_entry

[[Языки программирования/C++/Библиотеки/<filesystem>/path|Назад]] | [[Языки программирования/C++/Библиотеки/<filesystem>|Содержание]] | [[Языки программирования/C++/Библиотеки/<filesystem>/directory_iterator|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <filesystem>

class directory_entry;
```

## Параметры

Нет.

## Возвращаемое значение

Класс `std::filesystem::directory_entry` — запись о файле в каталоге.

## Что делает

Хранит путь и (кэшированный) статус файла, полученный при итерации по каталогу.

## Примеры

```cpp
#include <filesystem>
#include <iostream>

int main()
{
    namespace fs = std::filesystem;
    for (const auto& entry : fs::directory_iterator("/tmp"))
        std::cout << entry.path() << std::endl;
}
```

## Исключения

- **Исключения:** не бросает исключений (при正常使用).

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<filesystem>/directory_iterator|directory_iterator]] — итератор каталога

## Источники

- https://en.cppreference.com/w/cpp/filesystem/directory_entry
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<filesystem>/path|Назад]] | [[Языки программирования/C++/Библиотеки/<filesystem>|Содержание]] | [[Языки программирования/C++/Библиотеки/<filesystem>/directory_iterator|Вперёд]]
