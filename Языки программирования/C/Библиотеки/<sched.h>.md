# <sched.h>

[[Языки программирования/C/Библиотеки|Библиотеки]] / <sched.h>

**Дата написания:** 04.09.2026

## Оглавление

### Типы

- [[Языки программирования/C/Библиотеки/<sched.h>/struct sched_param|struct sched_param]] — параметры планирования

### Константы политик планирования

- [[Языки программирования/C/Библиотеки/<sched.h>/SCHED_FIFO|SCHED_FIFO]] — политика FIFO
- [[Языки программирования/C/Библиотеки/<sched.h>/SCHED_RR|SCHED_RR]] — политика Round Robin
- [[Языки программирования/C/Библиотеки/<sched.h>/SCHED_SPORADIC|SCHED_SPORADIC]] — спорадическая политика
- [[Языки программирования/C/Библиотеки/<sched.h>/SCHED_OTHER|SCHED_OTHER]] — стандартная политика

### Функции

- [[Языки программирования/C/Библиотеки/<sched.h>/sched_setscheduler|sched_setscheduler]] — установка политики планирования
- [[Языки программирования/C/Библиотеки/<sched.h>/sched_getscheduler|sched_getscheduler]] — получение политики планирования
- [[Языки программирования/C/Библиотеки/<sched.h>/sched_setparam|sched_setparam]] — установка параметров планирования
- [[Языки программирования/C/Библиотеки/<sched.h>/sched_getparam|sched_getparam]] — получение параметров планирования
- [[Языки программирования/C/Библиотеки/<sched.h>/sched_get_priority_max|sched_get_priority_max]] — максимальный приоритет
- [[Языки программирования/C/Библиотеки/<sched.h>/sched_get_priority_min|sched_get_priority_min]] — минимальный приоритет
- [[Языки программирования/C/Библиотеки/<sched.h>/sched_rr_get_interval|sched_rr_get_interval]] — интервал Round Robin
- [[Языки программирования/C/Библиотеки/<sched.h>/sched_yield|sched_yield]] — уступка процессора

## Описание библиотеки

Заголовочный файл `<sched.h>` — планирование выполнения. Определяет структуру `sched_param`, константы политик планирования и функции для управления планированием процессов и потоков.

### Структура `struct sched_param`

```c
struct sched_param {
    int sched_priority;                /* Приоритет выполнения */
    /* Дополнительно для SCHED_SPORADIC: */
    int             sched_ss_low_priority;   /* Низкий приоритет */
    struct timespec sched_ss_repl_period;    /* Период пополнения */
    struct timespec sched_ss_init_budget;    /* Начальный бюджет */
    int             sched_ss_max_repl;       /* Макс. пополнений */
};
```

### Константы политик

| Константа | Описание |
|---|---|
| `SCHED_FIFO` | Приоритетная очередь без квантования |
| `SCHED_RR` | Приоритетная очередь с квантованием |
| `SCHED_SPORADIC` | Спорадическая политика (периодические задачи) |
| `SCHED_OTHER` | Стандартная политика ОС |

### Функции

| Функция | Описание |
|---|---|
| `sched_setscheduler(pid_t, int, const struct sched_param *)` | Установка политики планирования |
| `sched_getscheduler(pid_t)` | Получение политики планирования |
| `sched_setparam(pid_t, const struct sched_param *)` | Установка параметров |
| `sched_getparam(pid_t, struct sched_param *)` | Получение параметров |
| `sched_get_priority_max(int)` | Максимальный приоритет для политики |
| `sched_get_priority_min(int)` | Минимальный приоритет для политики |
| `sched_rr_get_interval(pid_t, struct timespec *)` | Интервал квантования RR |
| `sched_yield(void)` | Уступка процессора другому потоку |

## Исключения

- **NULL:** функции не принимают `NULL`.
- **pid_t:** `0` означает текущий процесс.
- **EPERM:** нет прав на изменение планирования (не root).
- **EINVAL:** неверная политика или параметры.
- **SCHED_OTHER:** приоритет игнорируется для этой политики.
- **Многопоточность:** функции потокобезопасны.

## Стандарты

POSIX.1-2017.

## Источники

- https://man7.org/linux/man-pages/man0/sched.h.0p.html
- `/usr/include/sched.h`

[[Языки программирования/C/Библиотеки|Содержание]]
