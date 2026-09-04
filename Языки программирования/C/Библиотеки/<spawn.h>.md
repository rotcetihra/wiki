# <spawn.h>

[[Языки программирования/C/Библиотеки|Библиотеки]] / <spawn.h>

**Дата написания:** 04.09.2026

## Оглавление

### Типы

- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_t|posix_spawnattr_t]] — атрибуты порождения процесса
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawn_file_actions_t|posix_spawn_file_actions_t]] — действия с файлами при порождении

### Константы флагов

- [[Языки программирования/C/Библиотеки/<spawn.h>/POSIX_SPAWN_RESETIDS|POSIX_SPAWN_RESETIDS]] — сброс ID
- [[Языки программирования/C/Библиотеки/<spawn.h>/POSIX_SPAWN_SETPGROUP|POSIX_SPAWN_SETPGROUP]] — установка группы процессов
- [[Языки программирования/C/Библиотеки/<spawn.h>/POSIX_SPAWN_SETSCHEDPARAM|POSIX_SPAWN_SETSCHEDPARAM]] — установка параметров планирования
- [[Языки программирования/C/Библиотеки/<spawn.h>/POSIX_SPAWN_SETSCHEDULER|POSIX_SPAWN_SETSCHEDULER]] — установка политики планирования
- [[Языки программирования/C/Библиотеки/<spawn.h>/POSIX_SPAWN_SETSIGDEF|POSIX_SPAWN_SETSIGDEF]] — обработка сигналов по умолчанию
- [[Языки программирования/C/Библиотеки/<spawn.h>/POSIX_SPAWN_SETSIGMASK|POSIX_SPAWN_SETSIGMASK]] — установка маски сигналов

### Функции порождения

- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawn|posix_spawn]] — порождение нового процесса
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnp|posix_spawnp]] — порождение с поиском в PATH

### Функции управления файловыми действиями

- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawn_file_actions_init|posix_spawn_file_actions_init]] — инициализация действий с файлами
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawn_file_actions_destroy|posix_spawn_file_actions_destroy]] — уничтожение действий с файлами
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawn_file_actions_addclose|posix_spawn_file_actions_addclose]] — добавление закрытия дескриптора
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawn_file_actions_adddup2|posix_spawn_file_actions_adddup2]] — добавление дублирования дескриптора
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawn_file_actions_addopen|posix_spawn_file_actions_addopen]] — добавление открытия файла

### Функции управления атрибутами

- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_init|posix_spawnattr_init]] — инициализация атрибутов
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_destroy|posix_spawnattr_destroy]] — уничтожение атрибутов
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_setflags|posix_spawnattr_setflags]] — установка флагов
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_getflags|posix_spawnattr_getflags]] — получение флагов
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_setpgroup|posix_spawnattr_setpgroup]] — установка группы процессов
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_getpgroup|posix_spawnattr_getpgroup]] — получение группы процессов
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_setschedparam|posix_spawnattr_setschedparam]] — установка параметров планирования
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_getschedparam|posix_spawnattr_getschedparam]] — получение параметров планирования
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_setschedpolicy|posix_spawnattr_setschedpolicy]] — установка политики планирования
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_getschedpolicy|posix_spawnattr_getschedpolicy]] — получение политики планирования
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_setsigdefault|posix_spawnattr_setsigdefault]] — установка сигналов по умолчанию
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_getsigdefault|posix_spawnattr_getsigdefault]] — получение сигналов по умолчанию
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_setsigmask|posix_spawnattr_setsigmask]] — установка маски сигналов
- [[Языки программирования/C/Библиотеки/<spawn.h>/posix_spawnattr_getsigmask|posix_spawnattr_getsigmask]] — получение маски сигналов

## Описание библиотеки

Заголовочный файл `<spawn.h>` — порождение процессов (POSIX Advanced Realtime). Определяет типы и функции для создания нового процесса с возможностью настройки атрибутов и действий с файлами.

### Константы флагов

| Константа | Описание |
|---|---|
| `POSIX_SPAWN_RESETIDS` | Сброс effective UID/GID до реальных |
| `POSIX_SPAWN_SETPGROUP` | Установка новой группы процессов |
| `POSIX_SPAWN_SETSCHEDPARAM` | Установка параметров планирования |
| `POSIX_SPAWN_SETSCHEDULER` | Установка политики планирования |
| `POSIX_SPAWN_SETSIGDEF` | Обработка сигналов по умолчанию |
| `POSIX_SPAWN_SETSIGMASK` | Установка маски сигналов |

### Функции

| Функция | Описание |
|---|---|
| `posix_spawn(pid_t *, const char *, const posix_spawn_file_actions_t *, const posix_spawnattr_t *, char *const [], char *const [])` | Порождение нового процесса |
| `posix_spawnp(...)` | То же, с поиском исполняемого файла в `PATH` |
| `posix_spawn_file_actions_init(...)` | Инициализация действий с файлами |
| `posix_spawn_file_actions_destroy(...)` | Уничтожение действий с файлами |
| `posix_spawn_file_actions_addclose(...)` | Закрытие дескриптора в дочернем процессе |
| `posix_spawn_file_actions_adddup2(...)` | Дублирование дескриптора |
| `posix_spawn_file_actions_addopen(...)` | Открытие файла по имени |

### Возвращаемое значение

Все функции возвращают `0` при успехе или номер ошибки при ошибке.

### Использование

```c
#include <spawn.h>

pid_t pid;
posix_spawn_file_actions_t actions;
posix_spawn_file_actions_init(&actions);
posix_spawn_file_actions_addclose(&actions, STDIN_FILENO);

char *argv[] = {"ls", "-l", NULL};
posix_spawn(&pid, "/bin/ls", &actions, NULL, argv, NULL);

posix_spawn_file_actions_destroy(&actions);
```

## Исключения

- **NULL:** `posix_spawn()` и `posix_spawnp()` не принимают `NULL` в качестве имени файла.
- **errno:** при ошибке устанавливается `errno` (например, `EACCES`, `EINVAL`, `ENOMEM`, `ENOENT`).
- **EACCES:** нет прав доступа к файлу.
- **ENOENT:** файл не найден.
- **EINVAL:** неверный аргумент (например, неинициализированный атрибут).
- **ENOMEM:** недостаточно памяти.
- **fork + exec:** `posix_spawn()` заменяет `fork()` + `exec()` на системах с ограниченной виртуальной памятью.
- **Многопоточность:** функции потокобезопасны.

## Стандарты

POSIX.1-2017, Advanced Realtime.

## Источники

- https://man7.org/linux/man-pages/man0/spawn.h.0p.html
- `/usr/include/spawn.h`

[[Языки программирования/C/Библиотеки|Содержание]]
