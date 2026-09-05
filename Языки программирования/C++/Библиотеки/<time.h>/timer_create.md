# timer_create

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<time.h>|<time.h>]] / timer_create

[[Языки программирования/C++/Библиотеки/<time.h>/nanosleep|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <time.h>\nint timer_create(clockid_t clockid, struct sigevent *sevp, timer_t *timerid);
```

## Параметры

| Параметр | Описание |
|---|---|
| `clockid` | часы |\n| `sevp` | событие |\n| `timerid` | ID таймера |
## Возвращаемое значение

0 или -1.

## Что делает

Создаёт таймер.

## Примеры

### Базовое использование

```cpp
timer_t tid;\ntimer_create(CLOCK_REALTIME, NULL, &tid);
```

## Источники

- https://man7.org/linux/man-pages/man2/timer_create2.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<time.h>/nanosleep|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
