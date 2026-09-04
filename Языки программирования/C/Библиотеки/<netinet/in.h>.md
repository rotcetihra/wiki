# <netinet/in.h>

[[Языки программирования/C/Библиотеки|Библиотеки]] / <netinet/in.h>

**Дата написания:** 04.09.2026

## Оглавление

### Типы

- [[Языки программирования/C/Библиотеки/<netinet/in.h>/in_port_t|in_port_t]] — номер порта (uint16_t)
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/in_addr_t|in_addr_t]] — адрес IPv4 (uint32_t)

### Структуры IPv4

- [[Языки программирования/C/Библиотеки/<netinet/in.h>/struct in_addr|struct in_addr]] — адрес IPv4
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/struct sockaddr_in|struct sockaddr_in]] — адрес сокета IPv4

### Структуры IPv6

- [[Языки программирования/C/Библиотеки/<netinet/in.h>/struct in6_addr|struct in6_addr]] — адрес IPv6 (128 бит)
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/struct sockaddr_in6|struct sockaddr_in6]] — адрес сокета IPv6
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/struct ipv6_mreq|struct ipv6_mreq]] — запрос мультикаста IPv6

### Константы протоколов

- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IPPROTO_IP|IPPROTO_IP]] — Internet-протокол
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IPPROTO_IPV6|IPPROTO_IPV6]] — IPv6
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IPPROTO_ICMP|IPPROTO_ICMP]] — протокол управления
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IPPROTO_RAW|IPPROTO_RAW]] — сырые IP-пакеты
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IPPROTO_TCP|IPPROTO_TCP]] — TCP
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IPPROTO_UDP|IPPROTO_UDP]] — UDP

### Константы адресов

- [[Языки программирования/C/Библиотеки/<netinet/in.h>/INADDR_ANY|INADDR_ANY]] —wildcard IPv4-адрес
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/INADDR_BROADCAST|INADDR_BROADCAST]] — broadcast IPv4-адрес
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/INET_ADDRSTRLEN|INET_ADDRSTRLEN]] — длина строки IPv4 (16)
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/INET6_ADDRSTRLEN|INET6_ADDRSTRLEN]] — длина строки IPv6 (46)

### Константы опций IPv6

- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IPV6_JOIN_GROUP|IPV6_JOIN_GROUP]] — вступление в мультикаст-группу
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IPV6_LEAVE_GROUP|IPV6_LEAVE_GROUP]] — выход из мультикаст-группы
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IPV6_MULTICAST_HOPS|IPV6_MULTICAST_HOPS]] — hop limit мультикаста
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IPV6_MULTICAST_IF|IPV6_MULTICAST_IF]] — интерфейс мультикаста
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IPV6_MULTICAST_LOOP|IPV6_MULTICAST_LOOP]] — возврат мультикаста
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IPV6_UNICAST_HOPS|IPV6_UNICAST_HOPS]] — hop limit unicast
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IPV6_V6ONLY|IPV6_V6ONLY]] — только IPv6

### Макросы проверки IPv6

- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IN6_IS_ADDR_UNSPECIFIED|IN6_IS_ADDR_UNSPECIFIED]] — неопределённый адрес
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IN6_IS_ADDR_LOOPBACK|IN6_IS_ADDR_LOOPBACK]] — loopback
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IN6_IS_ADDR_MULTICAST|IN6_IS_ADDR_MULTICAST]] — мультикаст
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IN6_IS_ADDR_LINKLOCAL|IN6_IS_ADDR_LINKLOCAL]] — link-local
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IN6_IS_ADDR_SITELOCAL|IN6_IS_ADDR_SITELOCAL]] — site-local
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IN6_IS_ADDR_V4MAPPED|IN6_IS_ADDR_V4MAPPED]] — IPv4-mapped
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IN6_IS_ADDR_V4COMPAT|IN6_IS_ADDR_V4COMPAT]] — IPv4-compatible
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IN6_IS_ADDR_MC_NODELOCAL|IN6_IS_ADDR_MC_NODELOCAL]] — unicast link-local multicast
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IN6_IS_ADDR_MC_LINKLOCAL|IN6_IS_ADDR_MC_LINKLOCAL]] — link-local multicast
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IN6_IS_ADDR_MC_SITELOCAL|IN6_IS_ADDR_MC_SITELOCAL]] — site-local multicast
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IN6_IS_ADDR_MC_ORGLOCAL|IN6_IS_ADDR_MC_ORGLOCAL]] — organization-local multicast
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IN6_IS_ADDR_MC_GLOBAL|IN6_IS_ADDR_MC_GLOBAL]] — global multicast

### Внешние переменные

- `const struct in6_addr in6addr_any` — wildcard IPv6-адрес
- `const struct in6_addr in6addr_loopback` — loopback IPv6-адрес

### Макросы инициализации

- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IN6ADDR_ANY_INIT|IN6ADDR_ANY_INIT]] — инициализация wildcard
- [[Языки программирования/C/Библиотеки/<netinet/in.h>/IN6ADDR_LOOPBACK_INIT|IN6ADDR_LOOPBACK_INIT]] — инициализация loopback

## Описание библиотеки

Заголовочный файл `<netinet/in.h>` — семейство адресов Internet. Определяет типы, структуры и константы для работы с протоколами IPv4 и IPv6.

### Структуры IPv4

#### `struct in_addr`

```c
struct in_addr {
    in_addr_t s_addr;  /* Адрес IPv4 (в сетевом порядке байтов) */
};
```

#### `struct sockaddr_in`

```c
struct sockaddr_in {
    sa_family_t     sin_family;  /* AF_INET */
    in_port_t       sin_port;    /* Номер порта (сетевой порядок) */
    struct in_addr  sin_addr;    /* IP-адрес */
};
```

### Структуры IPv6

#### `struct in6_addr`

```c
struct in6_addr {
    uint8_t s6_addr[16];  /* Адрес IPv6 (сетевой порядок) */
};
```

#### `struct sockaddr_in6`

```c
struct sockaddr_in6 {
    sa_family_t      sin6_family;    /* AF_INET6 */
    in_port_t        sin6_port;      /* Номер порта (сетевой порядок) */
    uint32_t         sin6_flowinfo;  /* Traffic class и flow info */
    struct in6_addr  sin6_addr;      /* Адрес IPv6 */
    uint32_t         sin6_scope_id;  /* Interface index для scope */
};
```

### Инициализация

```c
/* IPv4 — привязка ко всем интерфейсам */
struct sockaddr_in addr4 = {0};
addr4.sin_family = AF_INET;
addr4.sin_port = htons(8080);
addr4.sin_addr.s_addr = htonl(INADDR_ANY);

/* IPv6 — привязка ко всем интерфейсам */
struct sockaddr_in6 addr6 = {0};
addr6.sin6_family = AF_INET6;
addr6.sin6_port = htons(8080);
addr6.sin6_addr = in6addr_any;
```

## Исключения

- **NULL:** заголовок не содержит функций.
- **Порядок байтов:** `sin_port` и `sin_addr`/`sin6_addr` хранятся в сетевом порядке байтов; используйте `htons()`/`htonl()`.
- **Инициализация `sockaddr_in6`:** рекомендуется инициализация `{0}` (стандартная), а не `memset(..., 0, ...)` из-за возможных нестандартных полей.
- **`sin6_scope_id`:** для link-local адресов должен содержать индекс интерфейса.
- **Мультикаст:** `IPV6_JOIN_GROUP` требует `IPPROTO_IPV6` в `setsockopt()`.
- **`in6addr_any`:** объявлен как `const`; не изменяйте его значение.

## Стандарты

POSIX.1-2017.

## Источники

- https://man7.org/linux/man-pages/man0/netinet_in.h.0p.html
- `/usr/include/netinet/in.h`

[[Языки программирования/C/Библиотеки|Содержание]]
