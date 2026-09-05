# mmap

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<sys/mman.h>|<sys/mman.h>]] / mmap

[[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <sys/mman.h>\nvoid *mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset);
```

## Параметры

| Параметр | Описание |
|---|---|
| `addr` | адрес (NULL — автоматически) |\n| `length` | размер |\n| `prot` | защита (PROT_READ, PROT_WRITE) |\n| `flags` | флаги (MAP_SHARED, MAP_PRIVATE) |\n| `fd` | файл |\n| `offset` | смещение |
## Возвращаемое значение

Указатель на область или MAP_FAILED.

## Что делает

Отображает файл в память.

## Примеры

### Базовое использование

```cpp
void *p = mmap(NULL, 4096, PROT_READ, MAP_PRIVATE, fd, 0);
```

## Источники

- https://man7.org/linux/man-pages/man2/mmap2.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки|Содержание]]
