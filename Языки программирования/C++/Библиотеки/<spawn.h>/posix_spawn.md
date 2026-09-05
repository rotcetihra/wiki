# posix_spawn

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<spawn.h>|<spawn.h>]] / posix_spawn

[[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <spawn.h>\nint posix_spawn(pid_t *pid, const char *path, const posix_spawn_file_actions_t *file_actions, const posix_spawnattr_t *attrp, char *const argv[], char *const envp[]);
```

## Параметры

| Параметр | Описание |
|---|---|
| `pid` | PID нового процесса |\n| `path` | путь к программе |\n| `file_actions` | действия над файлами |\n| `attrp` | атрибуты |\n| `argv` | аргументы |\n| `envp` | окружение |
## Возвращаемое значение

0 или код ошибки.

## Что делает

Запускает новый процесс.

## Примеры

### Базовое использование

```cpp
pid_t pid;\nposix_spawn(&pid, "/bin/ls", NULL, NULL, argv, environ);
```

## Источники

- https://man7.org/linux/man-pages/man3/posix_spawn3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки|Содержание]]
