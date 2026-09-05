# glob

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<glob.h>|<glob.h>]] / glob

[[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <glob.h>\nint glob(const char *pattern, int flags, int (*errfunc)(const char *, int), glob_t *pglob);
```

## Параметры

| Параметр | Описание |
|---|---|
| `pattern` | shell-шаблон |\n| `flags` | флаги |\n| `errfunc` | обработчик ошибок |\n| `pglob` | структура результатов |
## Возвращаемое значение

0 при успехе, GLOB_NOMATCH или другая ошибка.

## Что делает

Поиск файлов по шаблону.

## Примеры

### Базовое использование

```cpp
glob_t g;\nglob("*.txt", 0, NULL, &g);\nfor (size_t i = 0; i < g.gl_pathc; i++)\n    printf("%s", g.gl_pathv[i]);\nglobfree(&g);
```

## Источники

- https://man7.org/linux/man-pages/man3/glob3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки|Содержание]]
