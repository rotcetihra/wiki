# getrlimit

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<sys/resource.h>|<sys/resource.h>]] / getrlimit

[[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <sys/resource.h>\nint getrlimit(int resource, struct rlimit *rlim);
```

## Параметры

| Параметр | Описание |
|---|---|
| `resource` | тип ресурса (RLIMIT_AS, RLIMIT_CORE) |\n| `rlim` | лимит |
## Возвращаемое значение

0 или -1.

## Что делает

Получает ограничение ресурса.

## Примеры

### Базовое использование

```cpp
struct rlimit rl;\ngetrlimit(RLIMIT_NOFILE, &rl);
```

## Источники

- https://man7.org/linux/man-pages/man2/getrlimit2.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки|Содержание]]
