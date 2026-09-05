# getrusage

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<sys/resource.h>|<sys/resource.h>]] / getrusage

[[Языки программирования/C++/Библиотеки/<sys/resource.h>/setrlimit|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <sys/resource.h>\nint getrusage(int who, struct rusage *usage);
```

## Параметры

| Параметр | Описание |
|---|---|
| `who` | RUSAGE_SELF, RUSAGE_CHILDREN |\n| `usage` | использование |
## Возвращаемое значение

0 или -1.

## Что делает

Получает использование ресурсов.

## Примеры

### Базовое использование

```cpp
struct rusage ru;\ngetrusage(RUSAGE_SELF, &ru);
```

## Источники

- https://man7.org/linux/man-pages/man2/getrusage2.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<sys/resource.h>/setrlimit|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
