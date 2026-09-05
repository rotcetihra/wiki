# timer_settime

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<time.h>|<time.h>]] / timer_settime

[[Языки программирования/C++/Библиотеки/<time.h>/timer_delete|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <time.h>\nint timer_settime(timer_t timerid, int flags, const struct itimerval *new_value, struct itimerval *old_value);
```

## Параметры

| Параметр | Описание |
|---|---|
| `timerid` | ID |\n| `flags` | 0 или TIMER_ABSTIME |\n| `new_value` | новое значение |\n| `old_value` | предыдущее |
## Возвращаемое значение

0 или -1.

## Что делает

Устанавливает время таймера.

## Примеры

### Базовое использование

```cpp
timer_settime(tid, 0, &its, NULL);
```

## Источники

- https://man7.org/linux/man-pages/man2/timer_settime2.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<time.h>/timer_delete|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
