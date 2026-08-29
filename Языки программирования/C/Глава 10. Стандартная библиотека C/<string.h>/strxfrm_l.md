# strxfrm_l

[[Языки программирования/C/Глава 10. Стандартная библиотека C|Глава 10. Стандартная библиотека C]] / [[Языки программирования/C/Глава 10. Стандартная библиотека C/<string.h>|<string.h>]] / strxfrm_l

[[Языки программирования/C/Глава 10. Стандартная библиотека C/<string.h>/strxfrm|Назад]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<string.h>|Содержание]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<strings.h>/bcmp|Вперёд]]

**Дата написания:** 18.08.2026

## Прототип

```c
#include <string.h> // POSIX.1-2008

size_t strxfrm_l(char *dest, const char *src, size_t n, locale_t locale);
```

## Параметры

| Параметр | Описание |
|---|---|
| `dest` | Буфер для преобразованной строки |
| `src` | Исходная строка |
| `n` | Размер буфера `dest` (с учётом завершающего нуля) |
| `locale` | Локаль, чьи правила колляции применять (тип `locale_t`) |

## Возвращаемое значение

Возвращает длину преобразованной строки без учёта завершающего нуля. Если длина ≥ `n` — результат в буфер не поместился, содержимое `dest` не определено.

## Что делает

Вариант [[Языки программирования/C/Глава 10. Стандартная библиотека C/<string.h>/strxfrm|strxfrm()]] с явной локалью: преобразует строку в «форму сравнения» для правил сортировки заданной локали, чтобы затем сравнивать результаты обычным `strcmp()`. Не зависит от глобальной локали программы и безопасна в многопоточных программах.

## Примеры

### Построение ключа сортировки

```c
#include <stdio.h>
#include <string.h>
#include <locale.h>

int main(void)
{
    locale_t ru = newlocale(LC_COLLATE_MASK, "ru_RU.UTF-8", NULL);
    if (ru == NULL) {
        return 1;
    }

    char key[128];
    size_t len = strxfrm_l(key, "Яблоко", sizeof(key), ru);

    printf("Ключ: %s (длина %zu)\n", key, len);
    freelocale(ru);

    return 0;
}
```

### Сортировка с ключами в явной локали

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
    locale_t ru = newlocale(LC_COLLATE_MASK, "ru_RU.UTF-8", NULL);
    struct entry entries[] = {{"яблоко", ""}, {"арбуз", ""}, {"банан", ""}};
    size_t count = sizeof(entries) / sizeof(entries[0]);

    for (size_t i = 0; i < count; i++) {
        strxfrm_l(entries[i].key, entries[i].word, sizeof(entries[i].key), ru);
    }

    qsort(entries, count, sizeof(struct entry), compare);

    for (size_t i = 0; i < count; i++) {
        printf("%s\n", entries[i].word); // арбуз, банан, яблоко
    }

    freelocale(ru);
    return 0;
}
```

## Ошибки и errno

Может установить `errno` в `EINVAL` при невалидной локали. Если результат не поместился (длина ≥ `n`) — содержимое `dest` не определено.

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Явная локаль | Только POSIX.1-2008 |
| Потокобезопасна | Нужно управлять локалью |
| Ключ строится один раз | Дополнительный буфер |

## Альтернативы

- **[[Языки программирования/C/Глава 10. Стандартная библиотека C/<string.h>/strxfrm|strxfrm()]]** — с глобальной локалью
- **[[Языки программирования/C/Глава 10. Стандартная библиотека C/<string.h>/strcoll_l|strcoll_l()]]** — сравнение напрямую (без ключей)
- **[[Языки программирования/C/Глава 10. Стандартная библиотека C/<string.h>/strcmp|strcmp()]]** — без локали

## Похожие функции

- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<string.h>/strxfrm|strxfrm]] — с глобальной локалью
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<string.h>/strcoll_l|strcoll_l]] — сравнение с явной локалью
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<string.h>/strcmp|strcmp]] — побайтовое сравнение

## Источники

- POSIX.1-2008 (§13)
- Linux man-pages: `strxfrm(3)` (раздел `strxfrm_l`)