# <sys/resource.h>

[[Языки программирования/C/Библиотеки|Библиотеки]] / <sys/resource.h>

**Дата написания:** 04.09.2026

## Оглавление

### Константы приоритетов

- [[Языки программирования/C/Библиотеки/<sys/resource.h>/PRIO_PROCESS|PRIO_PROCESS]] — процесс по PID
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/PRIO_PGRP|PRIO_PGRP]] — группа процессов по PGID
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/PRIO_USER|PRIO_USER]] — пользователь по UID

### Константы ресурсов

- [[Языки программирования/C/Библиотеки/<sys/resource.h>/RLIMIT_CORE|RLIMIT_CORE]] — размер core-файла
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/RLIMIT_CPU|RLIMIT_CPU]] — процессорное время
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/RLIMIT_DATA|RLIMIT_DATA]] — размер сегмента данных
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/RLIMIT_FSIZE|RLIMIT_FSIZE]] — размер файла
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/RLIMIT_NOFILE|RLIMIT_NOFILE]] — количество открытых файлов
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/RLIMIT_STACK|RLIMIT_STACK]] — размер стека
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/RLIMIT_AS|RLIMIT_AS]] — размер адресного пространства

### Константы лимитов

- [[Языки программирования/C/Библиотеки/<sys/resource.h>/RLIM_INFINITY|RLIM_INFINITY]] — отсутствие лимита
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/RLIM_SAVED_MAX|RLIM_SAVED_MAX]] — непредставимый жёсткий лимит
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/RLIM_SAVED_CUR|RLIM_SAVED_CUR]] — непредставимый мягкий лимит

### Константы getrusage

- [[Языки программирования/C/Библиотеки/<sys/resource.h>/RUSAGE_SELF|RUSAGE_SELF]] — информация о текущем процессе
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/RUSAGE_CHILDREN|RUSAGE_CHILDREN]] — информация о дочерних процессах

### Типы

- [[Языки программирования/C/Библиотеки/<sys/resource.h>/rlim_t|rlim_t]] — беззнаковый тип для значений лимитов

### Структуры

- [[Языки программирования/C/Библиотеки/<sys/resource.h>/struct rlimit|struct rlimit]] —软性和 жёсткий лимиты ресурса
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/struct rusage|struct rusage]] — статистика использования ресурсов

### Функции

- [[Языки программирования/C/Библиотеки/<sys/resource.h>/getrlimit|getrlimit]] — получение лимитов ресурса
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/setrlimit|setrlimit]] — установка лимитов ресурса
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/getrusage|getrusage]] — получение статистики использования ресурсов
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/getpriority|getpriority]] — получение приоритета процесса
- [[Языки программирования/C/Библиотеки/<sys/resource.h>/setpriority|setpriority]] — установка приоритета процесса

## Описание библиотеки

Заголовочный файл `<sys/resource.h>` — определения для XSI-операций с ресурсами. Определяет функции для управления приоритетами, лимитами ресурсов и статистикой использования.

### Структуры

#### `struct rlimit`

```c
struct rlimit {
    rlim_t rlim_cur;  /* Мягкий (текущий) лимит */
    rlim_t rlim_max;  /* Жёсткий (максимальный) лимит */
};
```

#### `struct rusage`

```c
struct rusage {
    struct timeval ru_utime;  /* Пользовательское время */
    struct timeval ru_stime;  /* Системное время */
    /* ... дополнительные поля (Linux-специфичные) ... */
};
```

### Константы ресурсов

| Константа | Описание |
|---|---|
| `RLIMIT_CORE` | Максимальный размер core-файла |
| `RLIMIT_CPU` | Максимальное процессорное время (секунды) |
| `RLIMIT_DATA` | Максимальный размер сегмента данных |
| `RLIMIT_FSIZE` | Максимальный размер создаваемого файла |
| `RLIMIT_NOFILE` | Максимальное количество файловых дескрипторов |
| `RLIMIT_STACK` | Максимальный размер стека |
| `RLIMIT_AS` | Максимальный размер адресного пространства |

### Функции

| Функция | Описание |
|---|---|
| `getrlimit(int, struct rlimit *)` | Получение.soft и жёсткого лимитов |
| `setrlimit(int, const struct rlimit *)` | Установка.soft и жёсткого лимитов |
| `getrusage(int, struct rusage *)` | Получение статистики времени процесса |
| `getpriority(int, id_t)` | Получение приоритета (nice value) |
| `setpriority(int, id_t, int)` | Установка приоритета (nice value) |

### Возвращаемое значение

- `getrlimit()`/`setrlimit()` возвращают `0` при успехе или -1 при ошибке.
- `getrusage()` возвращает `0` при успехе или -1 при ошибке.
- `getpriority()` возвращает приоритет (от -20 до 20) или -1 при ошибке.
- `setpriority()` возвращает `0` при успехе или -1 при ошибке.

### Использование

```c
#include <sys/resource.h>

/* Получение лимита на количество открытых файлов */
struct rlimit rl;
getrlimit(RLIMIT_NOFILE, &rl);
printf("Мягкий лимит: %lu\n", rl.rlim_cur);
printf("Жёсткий лимит: %lu\n", rl.rlim_max);

/* Установка лимита на размер core-файла */
struct rlimit new_rl = {RLIM_INFINITY, RLIM_INFINITY};
setrlimit(RLIMIT_CORE, &new_rl);

/* Получение приоритета текущего процесса */
int nice_val = getpriority(PRIO_PROCESS, getpid());
```

## Исключения

- **NULL:** функции не принимают `NULL`.
- **errno:** при ошибке устанавливается `errno` (например, `EPERM`, `EINVAL`, `ESRCH`).
- **EPERM:** нет прав для установки лимита выше жёсткого или для изменения приоритета чужого процесса.
- **EINVAL:** неверный ресурс или неверный диапазон значений.
- **ESRCH:** процесс/группа/пользователь не найдены.
- **RLIM_INFINITY:** обозначает отсутствие лимита ( может быть `ULONG_MAX`).
- **nice value:** диапазон от -20 (наивысший приоритет) до 20 (наинизший).
- **Многопоточность:** функции потокобезопасны.

## Стандарты

POSIX.1-2017, XSI.

## Источники

- https://man7.org/linux/man-pages/man0/sys_resource.h.0p.html
- `/usr/include/sys/resource.h`

[[Языки программирования/C/Библиотеки|Содержание]]
