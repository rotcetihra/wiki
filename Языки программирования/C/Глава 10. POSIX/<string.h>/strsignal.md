# strsignal

[[Языки программирования/C/Глава 10. POSIX|Глава 10. POSIX]] / [[Языки программирования/C/Глава 10. POSIX/<string.h>|<string.h>]] / strsignal

[[Языки программирования/C/Глава 10. POSIX/<string.h>/strsep|Назад]] | [[Языки программирования/C/Глава 10. POSIX/<string.h>|Содержание]] | [[Языки программирования/C/Глава 10. POSIX/<string.h>/strtok_r|Вперёд]]

**Дата написания:** 18.08.2026

## Прототип

```c
#include <string.h> // POSIX (XSI, POSIX.1-2008)

char *strsignal(int sig);
```

## Параметры

| Параметр | Описание |
|---|---|
| `sig` | Номер сигнала (например, `SIGSEGV`, `SIGTERM` из `<signal.h>`) |

## Возвращаемое значение

Возвращает указатель на строку с названием сигнала. Если номер невалиден — реализация-зависимая строка (например, «Unknown signal»).

## Что делает

Аналог [[Языки программирования/C/Глава 9. Стандартная библиотека C/12. <string.h>/strerror|strerror()]] для сигналов: по номеру возвращает описание (например, `strsignal(SIGSEGV)` → «Segmentation fault»). Удобно для вывода причин завершения процесса в логах и обработчиках сигналов.

## Примеры

### Вывод описания сигнала

```c
#include <stdio.h>
#include <string.h>
#include <signal.h>

int main(void)
{
    printf("%s\n", strsignal(SIGSEGV)); // Segmentation fault
    printf("%s\n", strsignal(SIGTERM)); // Terminated
    printf("%s\n", strsignal(SIGKILL)); // Killed

    return 0;
}
```

### Вывод статуса завершения дочернего процесса

```c
#include <stdio.h>
#include <string.h>
#include <signal.h>
#include <sys/wait.h>

void report_status(int status)
{
    if (WIFSIGNALED(status)) {
        printf("Процесс завершён сигналом: %s\n", strsignal(WTERMSIG(status)));
    }
}
```

## Ошибки и errno

Функция не устанавливает `errno`. Для невалидного номера возвращает строку «Unknown signal N» (glibc).

>[!WARNING]
>Как и `strerror()`, использует статический буфер: в многопоточных программах не вызывайте без синхронизации.

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Простое описание сигнала | Статический буфер |
| Удобна для логов | Только POSIX (нет в C) |
| | Зависит от локали |

## Альтернативы

- **[[Языки программирования/C/Глава 9. Стандартная библиотека C/12. <string.h>/strerror|strerror()]]** — для кодов ошибок
- Собственная таблица сигналов — переносимая замена

## Похожие функции

- [[Языки программирования/C/Глава 9. Стандартная библиотека C/12. <string.h>/strerror|strerror]] — описание кода ошибки
- [[Языки программирования/C/Глава 10. POSIX/<string.h>/strerrordesc_np|strerrordesc_np]] — описание ошибки без перевода

## Источники

- POSIX.1-2008 (XSI)
- Linux man-pages: `strsignal(3)`