# getsockopt

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<sys/socket.h>|<sys/socket.h>]] / getsockopt

[[Языки программирования/C++/Библиотеки/<sys/socket.h>/shutdown|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<sys/socket.h>/setsockopt|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <sys/socket.h>\nint getsockopt(int sockfd, int level, int optname, void *optval, socklen_t *optlen);
```

## Параметры

| Параметр | Описание |
|---|---|
| `sockfd` | файловый дескриптор сокета |
| `level` | уровень (SOL_SOCKET, IPPROTO_TCP) |
| `optname` | имя опции |
| `optval` | буфер для значения |
| `optlen` | размер буфера |
## Возвращаемое значение

0 при успехе, -1 при ошибке.

## Что делает

Получает значение опции сокета.

## Примеры

### Базовое использование

```cpp
int optval;\nsocklen_t optlen = sizeof(optval);\ngetsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &optval, &optlen);
```

## Исключения

- **Исключения:** Возвращает -1 при ошибке.
- **Безопасность в C++11:** Потокобезопасна.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<sys/socket.h>/setsockopt|setsockopt]]

## Источники

- https://man7.org/linux/man-pages/man3/getsockopt.3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<sys/socket.h>/shutdown|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<sys/socket.h>/setsockopt|Вперёд]]
