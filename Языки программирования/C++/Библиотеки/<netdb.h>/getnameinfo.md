# getnameinfo

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<netdb.h>|<netdb.h>]] / getnameinfo

[[Языки программирования/C++/Библиотеки/<netdb.h>/getaddrinfo|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <netdb.h>\nint getnameinfo(const struct sockaddr *sa, socklen_t salen, char *host, socklen_t hostlen, char *serv, socklen_t servlen, int flags);
```

## Параметры

| Параметр | Описание |
|---|---|
| `sa` | адрес |\n| `host` | буфер имени |\n| `serv` | буфер сервиса |
## Возвращаемое значение

0 или код ошибки.

## Что делает

Обратное разрешение адреса.

## Примеры

### Базовое использование

```cpp
getnameinfo(&addr, len, host, sizeof(host), serv, sizeof(serv), 0);
```

## Источники

- https://man7.org/linux/man-pages/man3/getnameinfo3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<netdb.h>/getaddrinfo|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
