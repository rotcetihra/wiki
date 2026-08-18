# posix_openpt

[[Языки программирования/C/Глава 10. POSIX|Глава 10. POSIX]] / [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>|<stdlib.h>]] / posix_openpt

[[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/posix_memalign|Назад]] | [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>|Содержание]] | [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/ptsname|Вперёд]]

**Дата написания:** 18.08.2026

## Прототип

```c
#include <stdlib.h> // POSIX XSI

int posix_openpt(int oflag);
```

## Параметры

| Параметр | Описание |
|---|---|
| `oflag` | Флаги открытия: обычно `O_RDWR \| O_NOCTTY` (реализация может добавлять свои, например `O_CLOEXEC`) |

## Возвращаемое значение

Дескриптор master-устройства псевдо-терминала или -1 при ошибке.

## Что делает

Открывает master-устройство псевдо-терминала (на Linux — `/dev/ptmx`). POSIX-порт для работы с псевдо-терминалами: позволяет создавать пары master/slave для эмуляции терминала (программы `script`, `expect`, эмуляторы, тесты интерактивных программ). `O_NOCTTY` обязателен, чтобы открытие не делало терминал управляющим для процесса. После открытия: `grantpt()` (права slave), `unlockpt()` (разблокировка), `ptsname()` (имя slave), затем `open()` slave-устройства `O_RDWR | O_NOCTTY`.

## Примеры

```c
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int master = posix_openpt(O_RDWR | O_NOCTTY);
    if (master < 0) {
        return 1;
    }

    printf("master fd = %d\n", master);
    close(master);

    return 0;
}
```

## Ошибки и errno

При неудаче возвращает -1 и устанавливает `errno` (например, `ENOMEM`, `ENOENT` при отсутствии псевдо-терминалов).

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Единственный переносимый способ открыть pty | XSI: требуется `_XOPEN_SOURCE` |
| Не даёт управляющий терминал автоматически | Пара slave получается дополнительными шагами |

## Альтернативы

- **[[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/getpt|getpt()]]** — GNU-сокращение без флагов
- `open("/dev/ptmx", ...)` напрямую — Linux, без переносимости

## Похожие функции

- [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/getpt|getpt]] — GNU аналог
- [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/grantpt|grantpt]] — права slave
- [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/unlockpt|unlockpt]] — разблокировка
- [[Языки программирования/C/Глава 10. POSIX/<stdlib.h>/ptsname|ptsname]] — имя slave

## Источники

- POSIX.1-2024, раздел `posix_openpt()`
- GNU C Library (man-страница `posix_openpt(3)`)