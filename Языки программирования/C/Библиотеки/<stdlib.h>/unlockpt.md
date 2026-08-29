# unlockpt

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<stdlib.h>|<stdlib.h>]] / unlockpt

[[Языки программирования/C/Библиотеки/<stdlib.h>/system|Назад]] | [[Языки программирования/C/Библиотеки/<stdlib.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<stdlib.h>/wcstombs|Вперёд]]

**Дата написания:** 18.08.2026

## Прототип

```c
#include <stdlib.h> // POSIX XSI

int unlockpt(int fd);
```

## Параметры

| Параметр | Описание |
|---|---|
| `fd` | Дескриптор master-устройства псевдо-терминала (от `posix_openpt()`) |

## Возвращаемое значение

0 при успехе, -1 при ошибке.

## Что делает

Разрешает открытие slave-устройства псевдо-терминала: снимает блокировку на slave, установленную при создании пары (на Linux — `ioctl(TIOCSPTLCK, 0)`). Обязательный шаг перед `open()` slave-устройства после `posix_openpt()` и `grantpt()`. Типовая последовательность для псевдо-терминала: `posix_openpt()` → `grantpt()` → `unlockpt()` → `ptsname()` → `open(slave)`.

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

    grantpt(master);

    if (unlockpt(master) != 0) {
        return 1;
    }

    const char *slave = ptsname(master);
    int s = open(slave, O_RDWR | O_NOCTTY); // теперь slave можно открыть

    if (s >= 0) {
        close(s);
    }
    close(master);
    return 0;
}
```

## Ошибки и errno

При неудаче возвращает -1 и устанавливает `errno`: `EINVAL` — дескриптор не master псевдо-терминала, `ENOTTY` — не псевдо-терминал вовсе.

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Переносимый способ открыть slave | На некоторых реализациях — формальная операция (Linux ядро снимает блокировку само при открытии) |
| Простая (один аргумент) | Ошибки видны только по -1 без деталей |

## Альтернативы

- **`ioctl(fd, TIOCSPTLCK, 0)`** — низкоуровневый эквивалент на Linux
- Пропуск `unlockpt()` — на Linux slave иногда можно открыть и без неё, но это поведение не переносимо

## Похожие функции

- [[Языки программирования/C/Библиотеки/<stdlib.h>/posix_openpt|posix_openpt]] — открытие master
- [[Языки программирования/C/Библиотеки/<stdlib.h>/grantpt|grantpt]] — права slave
- [[Языки программирования/C/Библиотеки/<stdlib.h>/ptsname|ptsname]] — имя slave

## Источники

- POSIX.1-2024, раздел `unlockpt()`
- GNU C Library (man-страница `unlockpt(3)`)