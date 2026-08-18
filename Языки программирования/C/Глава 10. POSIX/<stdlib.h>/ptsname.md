# ptsname

[[Языки программирования/C/Глава 10. POSIX|Глава 10. POSIX]] / [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>|<stdlib.h>]] / ptsname

[[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/posix_openpt|Назад]] | [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>|Содержание]] | [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/putenv|Вперёд]]

**Дата написания:** 18.08.2026

## Прототип

```c
#include <stdlib.h> // POSIX XSI

char *ptsname(int fd);
int ptsname_r(int fd, char *buf, size_t buflen); // GNU
```

## Параметры

| Параметр | Описание |
|---|---|
| `fd` | Дескриптор master-устройства псевдо-терминала |
| `buf` | Буфер для имени (не менее `PTYNAME_MAX`, в glibc — 128) |
| `buflen` | Размер буфера |

## Возвращаемое значение

`ptsname()` — указатель на статический буфер с путём к slave-устройству (например, `/dev/pts/3`) или `NULL` при ошибке. `ptsname_r()` — 0 при успехе или код ошибки; имя записывается в `buf`.

## Что делает

Возвращает имя slave-устройства, соответствующего master-дескриптору псевдо-терминала. `ptsname()` использует статический буфер — не потокобезопасна (в POSIX отмечена как LEGACY). `ptsname_r()` (GNU) — потокобезопасная версия с явным буфером. Типовое использование: после `posix_openpt()` + `grantpt()` + `unlockpt()` — получить путь для `open()` slave.

>[!WARNING]
>Буфер `ptsname()` статический: два вызова в одном выражении дадут один и тот же указатель, и результат первого будет затёрт вторым вызовом. Для многопоточности используйте `ptsname_r()`.

## Примеры

```c
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int master = posix_openpt(O_RDWR | O_NOCTTY);
    grantpt(master);
    unlockpt(master);

    char slave[128];
    int rc = ptsname_r(master, slave, sizeof slave);
    if (rc != 0) {
        return 1;
    }

    printf("%s\n", slave); // /dev/pts/N

    close(master);
    return 0;
}
```

## Ошибки и errno

`ptsname()` при ошибке возвращает `NULL` и устанавливает `errno` (например, `ENOTTY` — `fd` не master pty). `ptsname_r()` возвращает код ошибки: `ERANGE` — буфер мал, `ENOTTY` — не pty.

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Простой доступ к имени slave | `ptsname()` — статический буфер, не потокобезопасна |
| `ptsname_r()` потокобезопасна (GNU) | Имя зависит от реализации и порядка устройств |

## Альтернативы

- **`ttyname()`** — имя терминала по дескриптору (глава sysio, не здесь)
- `/dev/pts/N` по номеру — не переносимо

## Похожие функции

- [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/posix_openpt|posix_openpt]] — открытие master
- [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/grantpt|grantpt]] — права slave
- [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/unlockpt|unlockpt]] — разблокировка

## Источники

- POSIX.1-2024, раздел `ptsname()`
- GNU C Library (man-страница `ptsname(3)`)