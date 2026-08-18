# strncat

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<string.h>|<string.h>]] / strncat

[[Языки программирования/C/Библиотеки/<string.h>/strlen|Назад]] | [[Языки программирования/C/Библиотеки/<string.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<string.h>/strncmp|Вперёд]]

**Дата написания:** 18.08.2026

## Прототип

```c
#include <string.h>

char *strncat(char *dest, const char *src, size_t n);
```

## Параметры

| Параметр | Описание |
|---|---|
| `dest` | Строка, в конец которой дописывается `src` |
| `src` | Дописываемая строка |
| `n` | Максимальное количество символов из `src` для дописывания |

## Возвращаемое значение

Возвращает `dest`.

## Что делает

Дописывает не более `n` символов из строки `src` в конец строки `dest`. В отличие от `strncpy()`, **всегда** добавляет завершающий нуль (даже если дописывается ровно `n` символов). Параметр `n` — максимум дописываемых символов, а не размер буфера `dest`.

## Примеры

### Базовое дописывание

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char line[16] = "C";
    size_t remaining = sizeof(line) - strlen(line) - 1; // Место под дописывание и нуль
    strncat(line, " language", remaining);
    printf("%s\n", line); // C language

    return 0;
}
```

### Безопасное формирование пути

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char path[32] = "/home";
    size_t remaining;

    remaining = sizeof(path) - strlen(path) - 1;
    strncat(path, "/user", remaining);

    remaining = sizeof(path) - strlen(path) - 1;
    strncat(path, "/docs", remaining);

    printf("%s\n", path); // /home/user/docs

    return 0;
}
```

### Ограничение длины результата

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char buf[8] = "Hi";
    strncat(buf, " there, how are you?", sizeof(buf) - strlen(buf) - 1);
    printf("%s\n", buf); // Hi there (усечённое)

    return 0;
}
```

## Ошибки и errno

Функция не устанавливает `errno`. Неопределённое поведение возникает при недостаточном размере буфера `dest` или перекрытии областей.

> [!WARNING]
>Параметр `n` в `strncat()` — максимум **дописываемых** символов, а не размер буфера `dest`. Передача `sizeof(dest)` вместо `n` — классическая ошибка: при длинном `dest` свободного места не останется, и строка всё равно выйдет за границы. Правильно вычислять свободное место: `sizeof(dest) - strlen(dest) - 1`.

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Гарантирует завершающий нуль | Не проверяет размер `dest` автоматически |
| Ограничивает количество дописываемых символов | Сложное вычисление `remaining` |
| Стандартная и переносимая | |

## Альтернативы

- **`strlcat()`** (BSD) — безопасное конкатенирование с проверкой размера
- **`strcat_s()`** (C11 Annex K) — проверка размера, код ошибки
- **`snprintf()`** — форматированная печать с ограничением длины

## Похожие функции

- [[Языки программирования/C/Библиотеки/<string.h>/strcat|strcat]] — дописывание без ограничения длины
- [[Языки программирования/C/Библиотеки/<string.h>/strncpy|strncpy]] — копирование с ограничением длины
- [[Языки программирования/C/Библиотеки/<string.h>/strlen|strlen]] — определение длины строки

## Источники

- Стандарт ISO C89 (§4.11.7.2)
- [cppreference: strncat](https://en.cppreference.com/w/c/string/byte/strncat)
- Linux man-pages: `strncat(3)`
