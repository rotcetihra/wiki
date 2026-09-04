# <err.h>

[[Языки программирования/C/Библиотеки|Библиотеки]] / <err.h>

**Дата написания:** 04.09.2026

## Оглавление

### Функции вывода ошибок

- [[Языки программирования/C/Библиотеки/<err.h>/err|err]] — вывод сообщения об ошибке и завершение
- [[Языки программирования/C/Библиотеки/<err.h>/errx|errx]] — вывод сообщения без errno и завершение
- [[Языки программирования/C/Библиотеки/<err.h>/warn|warn]] — вывод предупреждения
- [[Языки программирования/C/Библиотеки/<err.h>/warnx|warnx]] — вывод предупреждения без errno

### Функции с va_list

- [[Языки программирования/C/Библиотеки/<err.h>/verr|verr]] — вывод ошибки с va_list и завершение
- [[Языки программирования/C/Библиотеки/<err.h>/verrx|verrx]] — вывод ошибки без errno с va_list и завершение
- [[Языки программирования/C/Библиотеки/<err.h>/vwarn|vwarn]] — вывод предупреждения с va_list
- [[Языки программирования/C/Библиотеки/<err.h>/vwarnx|vwarnx]] — вывод предупреждения без errno с va_list

## Описание библиотеки

Заголовочный файл `<err.h>` — форматированные сообщения об ошибках. Определяет функции для вывода сообщений об ошибках в stderr и завершения программы.

### Функции

| Функция | Описание |
|---|---|
| `err(int eval, const char *fmt, ...)` | Вывод имени программы, `:`, сообщения, `:`, strerror(errno) и `exit(eval)` |
| `errx(int eval, const char *fmt, ...)` | То же без добавления strerror(errno) |
| `warn(const char *fmt, ...)` | Вывод предупреждения (без завершения) |
| `warnx(const char *fmt, ...)` | То же без добавления strerror(errno) |
| `verr(int eval, const char *fmt, va_list)` | Аналог `err()` для va_list |
| `verrx(int eval, const char *fmt, va_list)` | Аналог `errx()` для va_list |
| `vwarn(const char *fmt, va_list)` | Аналог `warn()` для va_list |
| `vwarnx(const char *fmt, va_list)` | Аналог `warnx()` для va_list |

### Возвращаемое значение

- `err()`, `errx()`, `verr()`, `verrx()`: не возвращают (`[[noreturn]]`), завершают программу через `exit(eval)`.
- `warn()`, `warnx()`, `vwarn()`, `vwarnx()`: ничего не возвращают.

### Использование

```c
#include <err.h>

p = malloc(size);
if (p == NULL)
    err(EXIT_FAILURE, NULL);

fd = open(file_name, O_RDONLY, 0);
if (fd == -1)
    err(EXIT_FAILURE, "%s", file_name);

/* Вывод без завершения */
warnx("%s: %s: пробуем блочное устройство", raw_device, strerror(errno));
```

## Исключения

- **NULL:** `err()` и `warn()` принимают `NULL` для `fmt` (выводят только strerror(errno)).
- **exit(eval):** `err()`/`errx()` завершают программу; `warn()`/`warnx()` — нет.
- **Формат:** поддерживается формат `printf()`.
- **Потокобезопасность:** функции потокобезопасны (MT-Safe locale).
- **BSD:** функции изначально из BSD, не являются частью POSIX.

## Стандарты

BSD.

## Источники

- https://man7.org/linux/man-pages/man3/err.3.html
- `/usr/include/err.h`

[[Языки программирования/C/Библиотеки|Содержание]]
