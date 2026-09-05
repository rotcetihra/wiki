# posix_spawn_file_actions_init

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<spawn.h>|<spawn.h>]] / posix_spawn_file_actions_init

[[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <spawn.h>\nint posix_spawn_file_actions_init(posix_spawn_file_actions_t *file_actions);
```

## Параметры

| Параметр | Описание |
|---|---|
| `file_actions` | действия |
## Возвращаемое значение

0 или -1.

## Что делает

Инициализирует действия.

## Примеры

### Базовое использование

```cpp
posix_spawn_file_actions_t fa;\nposix_spawn_file_actions_init(&fa);
```

## Источники

- https://man7.org/linux/man-pages/man3/posix_spawn_file_actions_init3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки|Содержание]]
