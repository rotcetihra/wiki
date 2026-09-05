# <filesystem>

[[Языки программирования/C++/Библиотеки|Библиотеки]] / <filesystem>

[[Языки программирования/C++/Библиотеки/<locale>|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>|Вперёд]]

**Дата написания:** 05.09.2026

## Оглавление

### Типы

- [[Языки программирования/C++/Библиотеки/<filesystem>/path|path]] — путь к файлу
- [[Языки программирования/C++/Библиотеки/<filesystem>/directory_entry|directory_entry]] — запись каталога
- [[Языки программирования/C++/Библиотеки/<filesystem>/directory_iterator|directory_iterator]] — итератор каталога
- [[Языки программирования/C++/Библиотеки/<filesystem>/recursive_directory_iterator|recursive_directory_iterator]] — рекурсивный итератор
- [[Языки программирования/C++/Библиотеки/<filesystem>/file_status|file_status]] — статус файла
- [[Языки программирования/C++/Библиотеки/<filesystem>/space_info|space_info]] — информация о пространстве
- [[Языки программирования/C++/Библиотеки/<filesystem>/file_time_type|file_time_type]] — время файла

### Перечисления

- [[Языки программирования/C++/Библиотеки/<filesystem>/copy_options|copy_options]] — опции копирования
- [[Языки программирования/C++/Библиотеки/<filesystem>/directory_options|directory_options]] — опции каталога
- [[Языки программирования/C++/Библиотеки/<filesystem>/perm_options|perm_options]] — опции прав
- [[Языки программирования/C++/Библиотеки/<filesystem>/perm_bad|perm_bad]] — ошибка прав
- [[Языки программирования/C++/Библиотеки/<filesystem>/file_type|file_type]] — тип файла

### Операции с файлами

- [[Языки программирования/C++/Библиотеки/<filesystem>/copy_file|copy_file]] — копирование файла
- [[Языки программирования/C++/Библиотеки/<filesystem>/create_directory|create_directory]] — создание каталога
- [[Языки программирования/C++/Библиотеки/<filesystem>/create_directories|create_directories]] — рекурсивное создание
- [[Языки программирования/C++/Библиотеки/<filesystem>/create_hard_link|create_hard_link]] — жёсткая ссылка
- [[Языки программирования/C++/Библиотеки/<filesystem>/create_symlink|create_symlink]] — символическая ссылка
- [[Языки программирования/C++/Библиотеки/<filesystem>/current_path|current_path]] — текущий каталог
- [[Языки программирования/C++/Библиотеки/<filesystem>/exists|exists]] — проверка существования
- [[Языки программирования/C++/Библиотеки/<filesystem>/equivalent|equivalent]] — эквивалентность путей
- [[Языки программирования/C++/Библиотеки/<filesystem>/file_size|file_size]] — размер файла
- [[Языки программирования/C++/Библиотеки/<filesystem>/initial_path|initial_path]] — начальный каталог
- [[Языки программирования/C++/Библиотеки/<filesystem>/is_block_file|is_block_file]] — блочное устройство
- [[Языки программирования/C++/Библиотеки/<filesystem>/is_character_file|is_character_file]] — символьное устройство
- [[Языки программирования/C++/Библиотеки/<filesystem>/is_directory|is_directory]] — каталог
- [[Языки программирования/C++/Библиотеки/<filesystem>/is_empty|is_empty]] — пустой файл/каталог
- [[Языки программирования/C++/Библиотеки/<filesystem>/is_fifo|is_fifo]] — именованный канал
- [[Языки программирования/C++/Библиотеки/<filesystem>/is_other|is_other]] — другой тип
- [[Языки программирования/C++/Библиотеки/<filesystem>/is_regular_file|is_regular_file]] — обычный файл
- [[Языки программирования/C++/Библиотеки/<filesystem>/is_socket|is_socket]] — сокет
- [[Языки программирования/C++/Библиотеки/<filesystem>/is_symlink|is_symlink]] — символическая ссылка
- [[Языки программирования/C++/Библиотеки/<filesystem>/last_write_time|last_write_time]] — время модификации
- [[Языки программирования/C++/Библиотеки/<filesystem>/permissions|permissions]] — установка прав
- [[Языки программирования/C++/Библиотеки/<filesystem>/read_symlink|read_symlink]] — чтение ссылки
- [[Языки программирования/C++/Библиотеки/<filesystem>/remove|remove]] — удаление файла
- [[Языки программирования/C++/Библиотеки/<filesystem>/remove_all|remove_all]] — рекурсивное удаление
- [[Языки программирования/C++/Библиотеки/<filesystem>/rename|rename]] — переименование
- [[Языки программирования/C++/Библиотеки/<filesystem>/resize_file|resize_file]] — изменение размера
- [[Языки программирования/C++/Библиотеки/<filesystem>/status|status]] — получение статуса
- [[Языки программирования/C++/Библиотеки/<filesystem>/status_known|status_known]] — проверка статуса
- [[Языки программирования/C++/Библиотеки/<filesystem>/swap|swap]] — обмен
- [[Языки программирования/C++/Библиотеки/<filesystem>/symlink_status|symlink_status]] — статус ссылки
- [[Языки программирования/C++/Библиотеки/<filesystem>/temp_directory_path|temp_directory_path]] — каталог временных файлов
- [[Языки программирования/C++/Библиотеки/<filesystem>/weakly_canonical|weakly_canonical]] — слабая канонизация

### Операции с путями

- [[Языки программирования/C++/Библиотеки/<filesystem>/absolute|absolute]] — абсолютный путь
- [[Языки программирования/C++/Библиотеки/<filesystem>/canonical|canonical]] — канонический путь
- [[Языки программирования/C++/Библиотеки/<filesystem>/relative|relative]] — относительный путь
- [[Языки программирования/C++/Библиотеки/<filesystem>/proximate|proximate]] — приблизительный путь

## Описание библиотеки

Заголовочный файл `<filesystem>` (C++17) предоставляет класс для манипуляций с путями файловой системы, итераторы по каталогам и операции для работы с файлами и каталогами: создание, удаление, копирование, перемещение, получение информации о правах и размерах.

## Исключения

- **Исключения:** большинство функций возвращают `std::error_code`. Некоторые бросают `filesystem_error` с сообщением об ошибке и путями.
- **Безопасность в C++11:** одновременный доступ к одной файловой системе из нескольких потоков безопасен.

## Стандарты

C++17, C++20, C++23.

## Источники

- https://en.cppreference.com/w/cpp/header/filesystem
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<locale>|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<system_error>|Вперёд]]
