# getpt

[[Языки программирования/C/Глава 10. POSIX|Глава 10. POSIX]] / [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>|<stdlib.h>]] / getpt

[[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/getloadavg|Назад]] | [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>|Содержание]] | [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/getsubopt|Вперёд]]

**Дата написания:** 18.08.2026

## Прототип

```c
#include <stdlib.h> // GNU (при _GNU_SOURCE)

int getpt(void);
```

## Возвращаемое значение

Файловый дескриптор master-устройства псевдо-терминала или -1 при ошибке.

## Что делает

Открывает первый доступный псевдо-терминал и возвращает дескриптор его master-устройства. GNU-расширение glibc — по сути, `posix_openpt(O_RDWR | O_NOCTTY)`. На Linux открывает `/dev/ptmx`. Используется вместе с `grantpt()`, `unlockpt()` и `ptsname()` для получения пары master/slave при создании псевдо-терминала (например, для эмуляторов терминала и утилит `script`, `expect`).

## Примеры

```c
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int master = getpt();
    if (master < 0) {
        return 1;
    }

    printf("master fd = %d\n", master);
    close(master);

    return 0;
}
```

## Ошибки и errno

При неудаче возвращает -1 и устанавливает `errno` (например, `ENOMEM` при исчерпании псевдо-терминалов).

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Простейший способ открыть псевдо-терминал | Только в glibc |
| Не требует флагов | Нет контроля над флагами открытия |

## Альтернативы

- **[[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/posix_openpt|posix_openpt()]]** — переносимая стандартная версия (POSIX XSI)

## Похожие функции

- [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/posix_openpt|posix_openpt]] — переносимый аналог
- [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/grantpt|grantpt]] — права slave-устройства
- [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/unlockpt|unlockpt]] — разблокировка slave
- [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/ptsname|ptsname]] — имя slave-устройства

## Источники

- GNU C Library (man-страница `getpt(3)`)