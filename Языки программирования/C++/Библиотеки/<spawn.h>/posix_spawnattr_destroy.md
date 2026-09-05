# posix_spawnattr_destroy

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<spawn.h>|<spawn.h>]] / posix_spawnattr_destroy

[[Языки программирования/C++/Библиотеки/<spawn.h>/posix_spawnattr_init|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <spawn.h>\nint posix_spawnattr_destroy(posix_spawnattr_t *attrp);
```

## Параметры

| Параметр | Описание |
|---|---|
| `attrp` | атрибуты |
## Возвращаемое значение

0 или -1.

## Что делает

Уничтожает атрибуты.

## Примеры

### Базовое использование

```cpp
posix_spawnattr_destroy(&attr);
```

## Источники

- https://man7.org/linux/man-pages/man3/posix_spawnattr_destroy3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<spawn.h>/posix_spawnattr_init|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
