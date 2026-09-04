# <netdb.h>

[[Языки программирования/C/Библиотеки|Библиотеки]] / <netdb.h>

**Дата написания:** 04.09.2026

## Оглавление

### Константы

- [[Языки программирования/C/Библиотеки/<netdb.h>/IPPORT_RESERVED|IPPORT_RESERVED]] — максимальный зарезервированный порт

### Структуры

- [[Языки программирования/C/Библиотеки/<netdb.h>/struct hostent|struct hostent]] — запись о хосте
- [[Языки программирования/C/Библиотеки/<netdb.h>/struct netent|struct netent]] — запись о сети
- [[Языки программирования/C/Библиотеки/<netdb.h>/struct protoent|struct protoent]] — запись о протоколе
- [[Языки программирования/C/Библиотеки/<netdb.h>/struct servent|struct servent]] — запись о сервисе
- [[Языки программирования/C/Библиотеки/<netdb.h>/struct addrinfo|struct addrinfo]] — информация об адресе

### Флаги addrinfo

- [[Языки программирования/C/Библиотеки/<netdb.h>/AI_PASSIVE|AI_PASSIVE]] — адрес для bind()
- [[Языки программирования/C/Библиотеки/<netdb.h>/AI_CANONNAME|AI_CANONNAME]] — запрос канонического имени
- [[Языки программирования/C/Библиотеки/<netdb.h>/AI_NUMERICHOST|AI_NUMERICHOST]] — числовой адрес без DNS
- [[Языки программирования/C/Библиотеки/<netdb.h>/AI_NUMERICSERV|AI_NUMERICSERV]] — числовой порт без разрешения
- [[Языки программирования/C/Библиотеки/<netdb.h>/AI_V4MAPPED|AI_V4MAPPED]] — IPv4-mapped IPv6
- [[Языки программирования/C/Библиотеки/<netdb.h>/AI_ALL|AI_ALL]] — запрос IPv4 и IPv6
- [[Языки программирования/C/Библиотеки/<netdb.h>/AI_ADDRCONFIG|AI_ADDRCONFIG]] — только настроенные адреса

### Флаги getnameinfo

- [[Языки программирования/C/Библиотеки/<netdb.h>/NI_NOFQDN|NI_NOFQDN]] — только имя узла
- [[Языки программирования/C/Библиотеки/<netdb.h>/NI_NUMERICHOST|NI_NUMERICHOST]] — числовой адрес
- [[Языки программирования/C/Библиотеки/<netdb.h>/NI_NAMEREQD|NI_NAMEREQD]] — ошибка если имя не найдено
- [[Языки программирования/C/Библиотеки/<netdb.h>/NI_NUMERICSERV|NI_NUMERICSERV]] — числовой порт
- [[Языки программирования/C/Библиотеки/<netdb.h>/NI_NUMERICSCOPE|NI_NUMERICSCOPE]] — числовой scope ID
- [[Языки программирования/C/Библиотеки/<netdb.h>/NI_DGRAM|NI_DGRAM]] — дейтаграмный сервис

### Коды ошибок

- [[Языки программирования/C/Библиотеки/<netdb.h>/EAI_AGAIN|EAI_AGAIN]] — временная ошибка
- [[Языки программирования/C/Библиотеки/<netdb.h>/EAI_BADFLAGS|EAI_BADFLAGS]] — неверные флаги
- [[Языки программирования/C/Библиотеки/<netdb.h>/EAI_FAIL|EAI_FAIL]] — невосстанавливаемая ошибка
- [[Языки программирования/C/Библиотеки/<netdb.h>/EAI_FAMILY|EAI_FAMILY]] — неверное семейство адресов
- [[Языки программирования/C/Библиотеки/<netdb.h>/EAI_MEMORY|EAI_MEMORY]] — нехватка памяти
- [[Языки программирования/C/Библиотеки/<netdb.h>/EAI_NONAME|EAI_NONAME]] — имя не разрешается
- [[Языки программирования/C/Библиотеки/<netdb.h>/EAI_SERVICE|EAI_SERVICE]] — сервис не распознан
- [[Языки программирования/C/Библиотеки/<netdb.h>/EAI_SOCKTYPE|EAI_SOCKTYPE]] — неверный тип сокета
- [[Языки программирования/C/Библиотеки/<netdb.h>/EAI_SYSTEM|EAI_SYSTEM]] — системная ошибка (см. errno)
- [[Языки программирования/C/Библиотеки/<netdb.h>/EAI_OVERFLOW|EAI_OVERFLOW]] — переполнение буфера

### Функции поиска адресов

- [[Языки программирования/C/Библиотеки/<netdb.h>/getaddrinfo|getaddrinfo]] — получение адресов по имени хоста
- [[Языки программирования/C/Библиотеки/<netdb.h>/freeaddrinfo|freeaddrinfo]] — освобождение списка addrinfo
- [[Языки программирования/C/Библиотеки/<netdb.h>/getnameinfo|getnameinfo]] — получение имени по адресу
- [[Языки программирования/C/Библиотеки/<netdb.h>/gai_strerror|gai_strerror]] — описание ошибки getaddrinfo

### Функции базы данных хостов

- [[Языки программирования/C/Библиотеки/<netdb.h>/gethostent|gethostent]] — следующая запись хоста
- [[Языки программирования/C/Библиотеки/<netdb.h>/sethostent|sethostent]] — начало чтения базы хостов
- [[Языки программирования/C/Библиотеки/<netdb.h>/endhostent|endhostent]] — завершение чтения базы хостов

### Функции базы данных сетей

- [[Языки программирования/C/Библиотеки/<netdb.h>/getnetbyaddr|getnetbyaddr]] — сеть по номеру
- [[Языки программирования/C/Библиотеки/<netdb.h>/getnetbyname|getnetbyname]] — сеть по имени
- [[Языки программирования/C/Библиотеки/<netdb.h>/getnetent|getnetent]] — следующая запись сети
- [[Языки программирования/C/Библиотеки/<netdb.h>/setnetent|setnetent]] — начало чтения базы сетей
- [[Языки программирования/C/Библиотеки/<netdb.h>/endnetent|endnetent]] — завершение чтения базы сетей

### Функции базы данных протоколов

- [[Языки программирования/C/Библиотеки/<netdb.h>/getprotobyname|getprotobyname]] — протокол по имени
- [[Языки программирования/C/Библиотеки/<netdb.h>/getprotobynumber|getprotobynumber]] — протокол по номеру
- [[Языки программирования/C/Библиотеки/<netdb.h>/getprotoent|getprotoent]] — следующая запись протокола
- [[Языки программирования/C/Библиотеки/<netdb.h>/setprotoent|setprotoent]] — начало чтения базы протоколов
- [[Языки программирования/C/Библиотеки/<netdb.h>/endprotoent|endprotoent]] — завершение чтения базы протоколов

### Функции базы данных сервисов

- [[Языки программирования/C/Библиотеки/<netdb.h>/getservbyname|getservbyname]] — сервис по имени
- [[Языки программирования/C/Библиотеки/<netdb.h>/getservbyport|getservbyport]] — сервис по порту
- [[Языки программирования/C/Библиотеки/<netdb.h>/getservent|getservent]] — следующая запись сервиса
- [[Языки программирования/C/Библиотеки/<netdb.h>/setservent|setservent]] — начало чтения базы сервисов
- [[Языки программирования/C/Библиотеки/<netdb.h>/endservent|endservent]] — завершение чтения базы сервисов

## Описание библиотеки

Заголовочный файл `<netdb.h>` — определения для сетевых операций с базой данных. Определяет структуры и функции для разрешения имён и поиска сетевых сервисов.

### Структуры

#### `struct hostent`

```c
struct hostent {
    char  *h_name;       /* Официальное имя хоста */
    char **h_aliases;    /* Массив псевдонимов (завершается NULL) */
    int    h_addrtype;   /* Тип адреса (AF_INET, AF_INET6) */
    int    h_length;     /* Длина адреса в байтах */
    char **h_addr_list;  /* Массив адресов (в сетевом порядке байтов) */
};
```

#### `struct addrinfo`

```c
struct addrinfo {
    int               ai_flags;      /* Флаги (AI_PASSIVE, AI_CANONNAME и т.д.) */
    int               ai_family;     /* Семейство сокета (AF_INET, AF_INET6) */
    int               ai_socktype;   /* Тип сокета (SOCK_STREAM, SOCK_DGRAM) */
    int               ai_protocol;   /* Протокол сокета */
    socklen_t         ai_addrlen;    /* Длина адреса */
    struct sockaddr  *ai_addr;       /* Адрес сокета */
    char             *ai_canonname;  /* Каноническое имя */
    struct addrinfo  *ai_next;       /* Следующий элемент списка */
};
```

### Функции

| Функция | Описание |
|---|---|
| `getaddrinfo(...)` | Разрешение имени хоста в адреса |
| `freeaddrinfo(struct addrinfo *)` | Освобождение списка `addrinfo` |
| `getnameinfo(...)` | Разрешение адреса в имя хоста и сервиса |
| `gai_strerror(int)` | Строковое описание ошибки `getaddrinfo()` |

### Возвращаемое значение

- `getaddrinfo()` возвращает `0` при успехе или код ошибки (`EAI_*`).
- `getnameinfo()` возвращает `0` при успехе или `EAI_*` при ошибке.
- `gai_strerror()` возвращает строку с описанием ошибки.

## Исключения

- **NULL:** `getaddrinfo()` может принимать `NULL` для `nodename` или `servname` (но не оба).
- **EAI_*:** коды ошибок, специфичные для `getaddrinfo()` и `getnameinfo()`.
- **EAI_NONAME:** имя не может быть разрешено.
- **EAI_SYSTEM:** системная ошибка; проверяйте `errno`.
- **Память:** `getaddrinfo()` выделяет память; `freeaddrinfo()` обязателен.
- **Многопоточность:** функции вроде `gethostent()` не потокобезопасны; используйте `getaddrinfo()`.
- **NI_NAMEREQD:** если указан, ошибка при невозможности разрешения имени.

## Стандарты

POSIX.1-2017, XSI.

## Источники

- https://man7.org/linux/man-pages/man0/netdb.h.0p.html
- `/usr/include/netdb.h`

[[Языки программирования/C/Библиотеки|Содержание]]
