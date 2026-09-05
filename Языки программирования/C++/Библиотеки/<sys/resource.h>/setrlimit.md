# setrlimit

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<sys/resource.h>|<sys/resource.h>]] / setrlimit

[[Языки программирования/C++/Библиотеки/<sys/resource.h>/getrlimit|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <sys/resource.h>\nint setrlimit(int resource, const struct rlimit *rlim);
```

## Параметры

| Параметр | Описание |
|---|---|
| `resource` | тип ресурса |\n| `rlim` | новый лимит |
## Возвращаемое значение

0 или -1.

## Что делает

Устанавливает ограничение ресурса.

## Примеры

### Базовое использование

```cpp
struct rlimit rl;\nrl.rlim_cur = 1024;\nsetrlimit(RLIMIT_NOFILE, &rl);
```

## Источники

- https://man7.org/linux/man-pages/man2/setrlimit2.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<sys/resource.h>/getrlimit|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
