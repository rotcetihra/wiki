# getaddrinfo

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<netdb.h>|<netdb.h>]] / getaddrinfo

[[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <netdb.h>\nint getaddrinfo(const char *node, const char *service, const struct addrinfo *hints, struct addrinfo **res);
```

## Параметры

| Параметр | Описание |
|---|---|
| `node` | имя хоста |\n| `service` | сервис/порт |\n| `hints` | подсказки |\n| `res` | результат |
## Возвращаемое значение

0 или код ошибки EAI_*.

## Что делает

Разрешение имени хоста.

## Примеры

### Базовое использование

```cpp
struct addrinfo hints = {0}, *res;\nhints.ai_family = AF_INET;\ngetaddrinfo("example.com", "80", &hints, &res);
```

## Источники

- https://man7.org/linux/man-pages/man3/getaddrinfo3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки|Содержание]]
