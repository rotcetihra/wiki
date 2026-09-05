# posix_spawn_file_actions_addopen

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<spawn.h>|<spawn.h>]] / posix_spawn_file_actions_addopen

[[Языки программирования/C++/Библиотеки/<spawn.h>/posix_spawn_file_actions_init|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <spawn.h>\nint posix_spawn_file_actions_addopen(posix_spawn_file_actions_t *file_actions, int fildes, const char *path, int oflag, mode_t mode);
```

## Параметры

| Параметр | Описание |
|---|---|
| `fildes` | дескриптор |\n| `path` | путь |\n| `oflag` | флаги |\n| `mode` | права |
## Возвращаемое значение

0 или -1.

## Что делает

Открывает файл при запуске.

## Примеры

### Базовое использование

```cpp
posix_spawn_file_actions_addopen(&fa, fd, "file.txt", O_RDONLY, 0);
```

## Источники

- https://man7.org/linux/man-pages/man3/posix_spawn_file_actions_addopen3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<spawn.h>/posix_spawn_file_actions_init|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
