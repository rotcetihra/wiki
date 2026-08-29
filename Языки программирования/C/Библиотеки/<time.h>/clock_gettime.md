# clock_gettime

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<time.h>|<time.h>]] / clock_gettime

[[Языки программирования/C/Библиотеки/<time.h>/clock|Назад]] | [[Языки программирования/C/Библиотеки/<time.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<time.h>/ctime|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#define _POSIX_C_SOURCE 199309L
#include <time.h>

int clock_gettime(clockid_t clk_id, struct timespec *tp);
```

## Описание

Функция `clock_gettime()` получает время с наносекундной точностью для различных часов системы. Параметр `clk_id` определяет, какое время извлекается:

| Значение | Описание |
|---|---|
| `CLOCK_REALTIME` | Текущее календарное время (аналог `time()`) |
| `CLOCK_MONOTONIC` | Монотонные часы (не перескакивают назад) |
| `CLOCK_PROCESS_CPUTIME_ID` | Время процессора процесса |
| `CLOCK_THREAD_CPUTIME_ID` | Время процессора потока |
| `CLOCK_REALTIME_COARSE` | Быстрые, но менее точные реальные часы (Linux) |

Возвращает 0 при успехе, -1 при ошибке.

> [!NOTE]
> Функция требует POSIX.1-2001 и определения `_POSIX_C_SOURCE >= 199309L`. В glibc также доступна при `_GNU_SOURCE`.

## Примеры

```c
#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <time.h>

int main(void)
{
    struct timespec ts;

    clock_gettime(CLOCK_REALTIME, &ts);
    printf("Текущее время: %ld.%09ld\n", (long)ts.tv_sec, ts.tv_nsec);

    /* Измерение интервала */
    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);

    volatile long long sum = 0;
    for (long long i = 0; i < 100000000LL; i++)
        sum += i;

    clock_gettime(CLOCK_MONOTONIC, &end);

    double elapsed = (double)(end.tv_sec - start.tv_sec) +
                     (double)(end.tv_nsec - start.tv_nsec) / 1e9;
    printf("Интервал: %.6f сек\n", elapsed);

    return 0;
}
```

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Наносекундная точность | Не входит в ISO C (POSIX-расширение) |
| Несколько типов часов (реальные, монотонные, процессорные) | Требует `_POSIX_C_SOURCE` или `_GNU_SOURCE` |
| Потокобезопасна | Не доступна на Windows (аналог — `QueryPerformanceCounter`) |

## Похожие функции

- [[Языки программирования/C/Библиотеки/<time.h>/timespec_get|timespec_get]] — стандартная C11-альтернатива
- [[Языки программирования/C/Библиотеки/<time.h>/clock|clock]] — процессорное время в тиках
- [[Языки программирования/C/Библиотеки/<time.h>/time|time]] — календарное время в секундах

## Источники

- POSIX.1-2008 (IEEE Std 1003.1-2008)
- GNU C Library, man-страница `clock_gettime(2)`
