# clock_getres

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<time.h>|<time.h>]] / clock_getres

[[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <time.h>\nint clock_getres(clockid_t clk_id, struct timespec *res);
```

## Параметры

| Параметр | Описание |
|---|---|
| `clk_id` | CLOCK_REALTIME, CLOCK_MONOTONIC |\n| `res` | разрешение |
## Возвращаемое значение

0 или -1.

## Что делает

Получает разрешение часов.

## Примеры

### Базовое использование

```cpp
struct timespec res;\nclock_getres(CLOCK_REALTIME, &res);
```

## Источники

- https://man7.org/linux/man-pages/man2/clock_getres2.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки|Содержание]]
