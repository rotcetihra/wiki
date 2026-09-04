# <sys/un.h>

[[Языки программирования/C/Библиотеки|Библиотеки]] / <sys/un.h>

**Дата написания:** 04.09.2026

## Оглавление

### Структуры

- [[Языки программирования/C/Библиотеки/<sys/un.h>/struct sockaddr_un|struct sockaddr_un]] — адрес UNIX-доменного сокета

## Описание библиотеки

Заголовочный файл `<sys/un.h>` — определения для UNIX-доменных сокетов. Определяет структуру `sockaddr_un` для хранения адресов локальных сокетов.

### Структура `struct sockaddr_un`

```c
struct sockaddr_un {
    sa_family_t  sun_family;  /* AF_UNIX */
    char         sun_path[];  /* Путь к файлу сокета (неизвестного размера) */
};
```

### Использование

```c
#include <sys/un.h>
#include <sys/socket.h>

int sock = socket(AF_UNIX, SOCK_STREAM, 0);

struct sockaddr_un addr = {0};
addr.sun_family = AF_UNIX;
strncpy(addr.sun_path, "/tmp/my.sock", sizeof(addr.sun_path) - 1);

bind(sock, (struct sockaddr *)&addr, sizeof(addr));
```

## Исключения

- **NULL:** заголовок не содержит функций.
- **Размер `sun_path`:** размер не определён стандартом; обычно от 92 до 108 байтов (зависит от реализации).
- **Не предполагайте фиксированный размер:** не используйте `sizeof(addr.sun_path)` без проверки на целевой платформе.
- **Инициализация:** рекомендуется инициализация `{0}` (как для `sockaddr_in6`).
- **Удаление:** при завершении удалите файл сокета через `unlink()`.
- **Многопоточность:** функции потокобезопасны.

## Стандарты

POSIX.1-2017.

## Источники

- https://man7.org/linux/man-pages/man0/sys_un.h.0p.html
- `/usr/include/sys/un.h`

[[Языки программирования/C/Библиотеки|Содержание]]
