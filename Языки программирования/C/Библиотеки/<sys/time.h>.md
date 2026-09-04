# <sys/time.h>

[[Языки программирования/C/Библиотеки|Библиотеки]] / <sys/time.h>

**Дата написания:** 04.09.2026

## Оглавление

### Типы

- [[Языки программирования/C/Библиотеки/<sys/time.h>/fd_set|fd_set]] — набор файловых дескрипторов

### Структуры

- [[Языки программирования/C/Библиотеки/<sys/time.h>/struct timeval|struct timeval]] — время в секундах и микросекундах
- [[Языки программирования/C/Библиотеки/<sys/time.h>/struct itimerval|struct itimerval]] — интервал и текущее значение таймера

### Константы таймеров

- [[Языки программирования/C/Библиотеки/<sys/time.h>/ITIMER_REAL|ITIMER_REAL]] — реальное время
- [[Языки программирования/C/Библиотеки/<sys/time.h>/ITIMER_VIRTUAL|ITIMER_VIRTUAL]] — виртуальное время процесса
- [[Языки программирования/C/Библиотеки/<sys/time.h>/ITIMER_PROF|ITIMER_PROF]] — виртуальное время + системные вызовы

### Макросы fd_set

- [[Языки программирования/C/Библиотеки/<sys/time.h>/FD_CLR|FD_CLR]] — удаление дескриптора из набора
- [[Языки программирования/C/Библиотеки/<sys/time.h>/FD_ISSET|FD_ISSET]] — проверка вхождения дескриптора
- [[Языки программирования/C/Библиотеки/<sys/time.h>/FD_SET|FD_SET]] — добавление дескриптора в набор
- [[Языки программирования/C/Библиотеки/<sys/time.h>/FD_ZERO|FD_ZERO]] — очистка набора
- [[Языки программирования/C/Библиотеки/<sys/time.h>/FD_SETSIZE|FD_SETSIZE]] — максимальное количество дескрипторов

### Функции

- [[Языки программирования/C/Библиотеки/<sys/time.h>/gettimeofday|gettimeofday]] — получение текущего времени
- [[Языки программирования/C/Библиотеки/<sys/time.h>/settimeofday|settimeofday]] — установка текущего времени
- [[Языки программирования/C/Библиотеки/<sys/time.h>/getitimer|getitimer]] — получение интервального таймера
- [[Языки программирования/C/Библиотеки/<sys/time.h>/setitimer|setitimer]] — установка интервального таймера
- [[Языки программирования/C/Библиотеки/<sys/time.h>/utimes|utimes]] — установка времён доступа и модификации
- [[Языки программирования/C/Библиотеки/<sys/time.h>/select|select]] — мультиплексирование ввода-вывода

## Описание библиотеки

Заголовочный файл `<sys/time.h>` — типы времени. Определяет структуры и функции для работы с временем и интервальными таймерами.

### Структуры

#### `struct timeval`

```c
struct timeval {
    time_t      tv_sec;   /* Секунды */
    suseconds_t tv_usec;  /* Микросекунды (0–999999) */
};
```

#### `struct itimerval`

```c
struct itimerval {
    struct timeval it_interval;  /* Интервал повторения */
    struct timeval it_value;     /* Текущее значение (таймер) */
};
```

### Константы таймеров

| Константа | Описание |
|---|---|
| `ITIMER_REAL` | Убывает в реальном времени; по истечении отправляет `SIGALRM` |
| `ITIMER_VIRTUAL` | Убывает только в пользовательском времени процесса; `SIGPROF` |
| `ITIMER_PROF` | Убывает в пользовательском + системном времени; `SIGPROF` |

### Функции

| Функция | Описание |
|---|---|
| `gettimeofday(struct timeval *, void *)` | Получение текущего времени (микросекундная точность) |
| `settimeofday(const struct timeval *, const void *)` | Установка текущего времени |
| `getitimer(int, struct itimerval *)` | Получение текущего значения интервального таймера |
| `setitimer(int, const struct itimerval *, struct itimerval *)` | Установка интервального таймера |
| `utimes(const char *, const struct timeval [2])` | Установка времён доступа и модификации файла |
| `select(int, fd_set *, fd_set *, fd_set *, struct timeval *)` | Мультиплексирование ввода-вывода |

### Возвращаемое значение

- `gettimeofday()` возвращает `0` при успехе или -1 при ошибке.
- `getitimer()`/`setitimer()` возвращают `0` при успехе или -1 при ошибке.
- `select()` возвращает количество готовых дескрипторов, 0 при таймауте или -1 при ошибке.

### Использование

```c
#include <sys/time.h>

/* Получение текущего времени */
struct timeval tv;
gettimeofday(&tv, NULL);
printf("Секунды: %ld, микросекунды: %ld\n", tv.tv_sec, tv.tv_usec);

/* Установка таймера на 5 секунд (SIGALRM) */
struct itimerval timer;
timer.it_value.tv_sec = 5;
timer.it_value.tv_usec = 0;
timer.it_interval.tv_sec = 0;  /* Без повторения */
timer.it_interval.tv_usec = 0;
setitimer(ITIMER_REAL, &timer, NULL);
```

## Исключения

- **NULL:** `gettimeofday()` принимает `NULL` для второго аргумента.
- **errno:** при ошибке устанавливается `errno` (например, `EINVAL`, `EPERM`).
- **settimeofday:** требует `CAP_SYS_TIME`; обычные процессы не могут установить время.
- **itimerval:** `it_value.tv_sec = 0` и `it_value.tv_usec = 0` отключают таймер.
- **Многопоточность:** функции потокобезопасны.
- **Точность:** `gettimeofday()` может быть заменена `clock_gettime()` (POSIX.1-2008).

## Стандарты

POSIX.1-2017, XSI.

## Источники

- https://man7.org/linux/man-pages/man0/sys_time.h.0p.html
- `/usr/include/sys/time.h`

[[Языки программирования/C/Библиотеки|Содержание]]
