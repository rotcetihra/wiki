# sched_setparam

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<sched.h>|<sched.h>]] / sched_setparam

[[Языки программирования/C++/Библиотеки/<sched.h>/sched_getparam|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <sched.h>\nint sched_setparam(pid_t pid, const struct sched_param *param);
```

## Параметры

| Параметр | Описание |
|---|---|
| `pid` | PID |\n| `param` | новые параметры |
## Возвращаемое значение

0 или -1.

## Что делает

Устанавливает параметры планирования.

## Примеры

### Базовое использование

```cpp
struct sched_param p;\np.sched_priority = 10;\nsched_setparam(0, &p);
```

## Источники

- https://man7.org/linux/man-pages/man2/sched_setparam2.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<sched.h>/sched_getparam|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
