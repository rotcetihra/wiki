# posix_spawn_file_actions_addclose

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<spawn.h>|<spawn.h>]] / posix_spawn_file_actions_addclose

[[Языки программирования/C++/Библиотеки/<spawn.h>/posix_spawn_file_actions_addopen|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <spawn.h>\nint posix_spawn_file_actions_addclose(posix_spawn_file_actions_t *file_actions, int fildes);
```

## Параметры

| Параметр | Описание |
|---|---|
| `fildes` | дескриптор |
## Возвращаемое значение

0 или -1.

## Что делает

Закрывает файл при запуске.

## Примеры

### Базовое использование

```cpp
posix_spawn_file_actions_addclose(&fa, fd);
```

## Источники

- https://man7.org/linux/man-pages/man3/posix_spawn_file_actions_addclose3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<spawn.h>/posix_spawn_file_actions_addopen|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
