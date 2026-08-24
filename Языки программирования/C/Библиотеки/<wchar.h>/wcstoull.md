# wcstoull

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<wchar.h>|<wchar.h>]] / wcstoull

[[Языки программирования/C/Библиотеки/<wchar.h>/wcstoul|Назад]] | [[Языки программирования/C/Библиотеки/<wchar.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<wchar.h>/Многобайтовые строки|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <wchar.h>

unsigned long long wcstoull(const wchar_t *str, wchar_t **endptr, int base);
```

## Описание

Функция `wcstoull()` преобразует широкую строку `str` в беззнаковое значение типа `unsigned long long`. Является широкосимвольным аналогом `strtoull()` из `<stdlib.h>`. Поведение идентично `wcstoul()`, но результат — `unsigned long long` (максимальный беззнаковый диапазон).

При переполнении возвращает `ULLONG_MAX` и устанавливает `errno` в `ERANGE`.

## Примеры

```c
#include <stdio.h>
#include <wchar.h>
#include <locale.h>

int main(void)
{
    setlocale(LC_ALL, "");

    const wchar_t *str = L"  18446744073709551615";
    wchar_t *end;

    unsigned long long ull = wcstoull(str, &end, 10);
    printf("'%ls' → %llu\n", str, ull);

    return 0;
}
```

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Максимальный беззнаковый диапазон | Квадратичная сложность для длинных строк |
| Стандартная функция ISO C | `unsigned long long` может быть избыточен |
| Поддерживает любое основание 2–36 | Требует `<wchar.h>` |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<wchar.h>/wcstoul|wcstoul]] — беззнаковое преобразование в `unsigned long`
- [[Языки программирования/C/Библиотеки/<wchar.h>/wcstoll|wcstoll]] — знаковое преобразование в `long long`
- [[Языки программирования/C/Библиотеки/<stdlib.h>/strtoull|strtoull]] — аналог для байтовых строк

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.29.4.1
- GNU C Library, заголовочный файл `wchar.h`
