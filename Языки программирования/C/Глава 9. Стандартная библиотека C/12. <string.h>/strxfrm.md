# strxfrm

[[Языки программирования/C/Глава 9. Стандартная библиотека C|Глава 9. Стандартная библиотека C]] / [[Языки программирования/C/Глава 9. Стандартная библиотека C/12. <string.h>|12. <string.h>]] / strxfrm

[[Языки программирования/C/Глава 9. Стандартная библиотека C/12. <string.h>/strtok|Назад]] | [[Языки программирования/C/Глава 9. Стандартная библиотека C/12. <string.h>|Содержание]] | [[Языки программирования/C/Глава 9. Стандартная библиотека C/13. <errno.h>|Вперёд]]

**Дата написания:** 18.08.2026

## Прототип

```c
#include <string.h>

size_t strxfrm(char *dest, const char *src, size_t n);
```

## Параметры

| Параметр | Описание |
|---|---|
| `dest` | Буфер для преобразованной строки |
| `src` | Исходная строка |
| `n` | Максимальный размер буфера `dest` (в байтах, включая нуль) |

## Возвращаемое значение

Возвращает длину, которая потребовалась бы без ограничения `n` (в байтах, без учёта завершающего нуля). Если возвращённое значение ≥ `n`, строка в буфер не поместилась. При `n` равном 0 функция лишь возвращает требуемую длину.

## Что делает

Преобразует строку `src` в «форму сравнения»: для любых двух строк результат `strcmp(strxfrm(a), strxfrm(b))` эквивалентен вызову `strcoll(a, b)`. Преобразование учитывает правила сортировки текущей локали (категория `LC_COLLATE`). Преобразованный ключ можно использовать в `strcmp()` для сортировки множества строк — это быстрее, чем вызывать `strcoll()` при каждом сравнении.

> [!WARNING]
>Области `dest` и `src` не должны перекрываться — иначе неопределённое поведение.

## Примеры

### Базовое преобразование

```c
#include <stdio.h>
#include <string.h>
#include <locale.h>

int main(void)
{
    setlocale(LC_ALL, "");

    char buf[64];
    size_t len = strxfrm(buf, "привет", sizeof(buf));
    printf("Длина ключа: %zu\n", len);
    printf("Ключ: %s\n", buf);

    return 0;
}
```

### Определение требуемого размера буфера

```c
#include <stdio.h>
#include <string.h>
#include <locale.h>
#include <stdlib.h>

int main(void)
{
    setlocale(LC_ALL, "");

    const char *word = "Архитектура";
    size_t len = strxfrm(NULL, word, 0); // Определяем длину

    char *key = malloc(len + 1);
    if (key != NULL) {
        strxfrm(key, word, len + 1);
        printf("Ключ: %s (длина %zu)\n", key, len);
        free(key);
    }

    return 0;
}
```

### Сортировка с предварительным преобразованием ключей

```c
#include <stdio.h>
#include <string.h>
#include <locale.h>
#include <stdlib.h>

struct entry {
    const char *word;
    char key[64];
};

int compare(const void *a, const void *b)
{
    return strcmp(((const struct entry *)a)->key,
                 ((const struct entry *)b)->key);
}

int main(void)
{
    setlocale(LC_ALL, "");

    struct entry entries[] = {
        {"Äpfel", ""},
        {"zebra", ""},
        {"ananas", ""},
        {"árbol", ""}
    };
    size_t count = sizeof(entries) / sizeof(entries[0]);

    for (size_t i = 0; i < count; i++) {
        strxfrm(entries[i].key, entries[i].word, sizeof(entries[i].key));
    }

    qsort(entries, count, sizeof(struct entry), compare);

    for (size_t i = 0; i < count; i++) {
        printf("%s\n", entries[i].word);
    }

    return 0;
}
```

## Ошибки и errno

- Если `dest` не достаточно большой (возвращённое значение ≥ `n`), содержимое `dest` не определено
- Если `src` не является валидной строкой — неопределённое поведение

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Позволяет сортировать через `strcmp()` | Двойное преобразование: сначала `strxfrm`, потом `strcmp` |
| Учитывает локаль | Сложнее в использовании, чем `strcoll()` |
| Один ключ строится один раз | Нужно выделять буфер под ключ |

## Альтернативы

- **`strcoll()`** — сравнение без предварительного преобразования (медленнее при сортировке)
- **`strcmp()`** — побайтовое сравнение без локали
- **`strcoll_l()`** (POSIX) — сравнение с указанной локалью

## Похожие функции

- [[Языки программирования/C/Глава 9. Стандартная библиотека C/12. <string.h>/strcoll|strcoll]] — сравнение строк с учётом локали
- [[Языки программирования/C/Глава 9. Стандартная библиотека C/12. <string.h>/strcmp|strcmp]] — побайтовое сравнение строк
- [[Языки программирования/C/Глава 9. Стандартная библиотека C/12. <string.h>/strlen|strlen]] — определение длины строки

## Источники

- Стандарт ISO C89 (§4.11.4.5)
- [cppreference: strxfrm](https://en.cppreference.com/w/c/string/byte/strxfrm)
- Linux man-pages: `strxfrm(3)`
