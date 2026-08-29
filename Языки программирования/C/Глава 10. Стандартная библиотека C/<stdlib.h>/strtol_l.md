# strtol_l

[[Языки программирования/C/Глава 10. Стандартная библиотека C|Глава 10. Стандартная библиотека C]] / [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdlib.h>|<stdlib.h>]] / strtol_l

[[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdlib.h>/strtol|Назад]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdlib.h>|Содержание]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdlib.h>/strtold|Вперёд]]

**Дата написания:** 18.08.2026

## Прототип

```c
#include <stdlib.h> // GNU (при _GNU_SOURCE)

long strtol_l(const char *restrict nptr, char **restrict endptr, int base, locale_t loc);
long long strtoll_l(const char *restrict nptr, char **restrict endptr, int base, locale_t loc);
unsigned long strtoul_l(const char *restrict nptr, char **restrict endptr, int base, locale_t loc);
unsigned long long strtoull_l(const char *restrict nptr, char **restrict endptr, int base, locale_t loc);
```

## Параметры

| Параметр | Описание |
|---|---|
| `nptr` | Строка для преобразования |
| `endptr` | Указатель на первый нераспознанный символ (или `NULL`) |
| `base` | Основание системы счисления (2–36) или 0 для автоопределения |
| `loc` | Явная локаль (разделитель тысяч и прочие правила категории `LC_NUMERIC`) |

## Возвращаемое значение

Преобразованное число или 0, если распознавания не произошло; при переполнении — `LONG_MAX`/`LONG_MIN` (и аналоги для `long long`, `unsigned`) с `errno = ERANGE`.

## Что делает

Варианты `strtol()`/`strtoll()`/`strtoul()`/`strtoull()` с явно заданной локалью: правила разбора цифр и разделителей берутся из `loc`, а не из глобальной локали процесса. GNU-расширение. Удобны в многопоточных программах, где переключение локали нежелательно. Тип `locale_t` и `newlocale()`/`freelocale()` — в `<locale.h>`.

## Примеры

```c
#include <locale.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    locale_t loc = newlocale(LC_NUMERIC_MASK, "de_DE.UTF-8", (locale_t)0);
    if (loc == (locale_t)0) {
        return 1;
    }

    char *end;
    long v = strtol_l("  1'234", &end, 10, loc); // апостроф — разделитель тысяч
    printf("%ld\n", v); // 1234

    freelocale(loc);
    return 0;
}
```

## Ошибки и errno

При переполнении возвращает крайнее значение типа и устанавливает `errno = ERANGE`. `endptr` фиксирует позицию остановки.

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| По правилам явной локали, без глобального состояния | Только glibc — не переносима |
| Потокобезопасна | Требует управления объектом `locale_t` |

## Альтернативы

- **[[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdlib.h>/strtol|strtol()]]** — стандартная версия (текущая локаль)
- **[[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdlib.h>/strtod_l|strtod_l()]]** — вещественный аналог

## Похожие функции

- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdlib.h>/strtod_l|strtod_l]] — числа с плавающей точкой
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdlib.h>/strtol|strtol]] — стандартная версия

## Источники

- GNU C Library (man-страница `strtol_l(3)`)