# sched_setscheduler

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<sched.h>|<sched.h>]] / sched_setscheduler

[[Языки программирования/C++/Библиотеки/<sched.h>/sched_getscheduler|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <sched.h>\nint sched_setscheduler(pid_t pid, int policy, const struct sched_param *param);
```

## Параметры

| Параметр | Описание |
|---|---|
| `pid` | PID |\n| `policy` | политика |\n| `param` | параметры |
## Возвращаемое значение

0 или -1.

## Что делает

Устанавливает политику планирования.

## Примеры

### Базовое использование

```cpp
sched_setscheduler(0, SCHED_FIFO, &p);
```

## Источники

- https://man7.org/linux/man-pages/man2/sched_setscheduler2.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<sched.h>/sched_getscheduler|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
