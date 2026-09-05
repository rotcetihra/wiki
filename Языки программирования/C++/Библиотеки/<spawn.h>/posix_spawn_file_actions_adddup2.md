# posix_spawn_file_actions_adddup2

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<spawn.h>|<spawn.h>]] / posix_spawn_file_actions_adddup2

[[Языки программирования/C++/Библиотеки/<spawn.h>/posix_spawn_file_actions_addclose|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <spawn.h>\nint posix_spawn_file_actions_adddup2(posix_spawn_file_actions_t *file_actions, int fildes, int newfildes);
```

## Параметры

| Параметр | Описание |
|---|---|
| `fildes` | исходный дескриптор |\n| `newfildes` | целевой дескриптор |
## Возвращаемое значение

0 или -1.

## Что делает

Дублирует дескриптор при запуске.

## Примеры

### Базовое использование

```cpp
posix_spawn_file_actions_adddup2(&fa, fd, STDOUT_FILENO);
```

## Источники

- https://man7.org/linux/man-pages/man3/posix_spawn_file_actions_adddup23.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<spawn.h>/posix_spawn_file_actions_addclose|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
