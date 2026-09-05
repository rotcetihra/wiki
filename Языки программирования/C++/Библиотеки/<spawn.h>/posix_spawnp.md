# posix_spawnp

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<spawn.h>|<spawn.h>]] / posix_spawnp

[[Языки программирования/C++/Библиотеки/<spawn.h>/posix_spawn|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <spawn.h>\nint posix_spawnp(pid_t *pid, const char *file, const posix_spawn_file_actions_t *file_actions, const posix_spawnattr_t *attrp, char *const argv[], char *const envp[]);
```

## Параметры

| Параметр | Описание |
|---|---|
| `pid` | PID |\n| `file` | имя файла (ищется в PATH) |
## Возвращаемое значение

0 или код ошибки.

## Что делает

Запускает процесс по PATH.

## Примеры

### Базовое использование

```cpp
posix_spawnp(&pid, "ls", NULL, NULL, argv, environ);
```

## Источники

- https://man7.org/linux/man-pages/man3/posix_spawnp3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<spawn.h>/posix_spawn|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
