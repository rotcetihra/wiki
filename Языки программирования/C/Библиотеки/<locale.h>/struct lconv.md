# struct lconv

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<locale.h>|<locale.h>]] / struct lconv

[[Языки программирования/C/Библиотеки/<inttypes.h>/wcstoumax|Назад]] | [[Языки программирования/C/Библиотеки/<locale.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<locale.h>/LC_ALL|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <locale.h>

struct lconv {
    char *decimal_point;
    char *thousands_sep;
    char *grouping;
    char *int_curr_symbol;
    char *currency_symbol;
    char *mon_decimal_point;
    char *mon_thousands_sep;
    char *mon_grouping;
    char *positive_sign;
    char *negative_sign;
    char int_frac_digits;
    char frac_digits;
    char p_cs_precedes;
    char p_sep_by_space;
    char n_cs_precedes;
    char n_sep_by_space;
    char p_sign_posn;
    char n_sign_posn;
    char int_p_cs_precedes;
    char int_p_sep_by_space;
    char int_n_cs_precedes;
    char int_n_sep_by_space;
    char int_p_sign_posn;
    char int_n_sign_posn;
};
```

## Описание

Тип `struct lconv` -- структура, содержащая информацию о форматировании числовых и денежных значений в соответствии с текущей локалью. Заполняется функцией `localeconv`.

Поля структуры делятся на две категории:

**Числовые поля:**

| Поле | Описание |
|---|---|
| `decimal_point` | Десятичный разделитель (точка в `en_US`, запятая в `ru_RU`) |
| `thousands_sep` | Разделитель групп разрядов (пробел в `ru_RU`, запятая в `de_DE`) |
| `grouping` | Правила группирования разрядов |

**Денежные поля:**

| Поле | Описание |
|---|---|
| `int_curr_symbol` | Международный символ валюты (например, `"RUB "`) |
| `currency_symbol` | Символ валюты (например, `"руб."` или `"₽"`) |
| `mon_decimal_point` | Десятичный разделитель для денежных значений |
| `mon_thousands_sep` | Разделитель групп для денежных значений |
| `mon_grouping` | Правила группирования для денежных значений |
| `positive_sign` | Знак положительного денежного значения |
| `negative_sign` | Знак отрицательного денежного значения |
| `int_frac_digits` | Количество знаков после запятой для международного формата |
| `frac_digits` | Количество знаков после запятой для локального формата |
| `p_cs_precedes` | Символ валюты precedes положительное значение (1 = да, 0 = нет) |
| `p_sep_by_space` | Пробел между символом валюты и положительным значением |
| `n_cs_precedes` | Символ валюты precedes отрицательное значение |
| `n_sep_by_space` | Пробел между символом валюты и отрицательным значением |
| `p_sign_posn` | Позиция знака для положительного значения |
| `n_sign_posn` | Позиция знака для отрицательного значения |
| `int_p_cs_precedes` | Международный символ валюты precedes положительное значение |
| `int_p_sep_by_space` | Пробел между международным символом и положительным значением |
| `int_n_cs_precedes` | Международный символ валюты precedes отрицательное значение |
| `int_n_sep_by_space` | Пробел между международным символом и отрицательным значением |
| `int_p_sign_posn` | Позиция знака для международного положительного значения |
| `int_n_sign_posn` | Позиция знака для международного отрицательного значения |

## Пример

```c
#include <stdio.h>
#include <locale.h>

int main(void)
{
    setlocale(LC_ALL, "ru_RU.UTF-8");

    struct lconv *lc = localeconv();

    printf("Десятичный разделитель: \"%s\"\n", lc->decimal_point);
    printf("Разделитель тысяч: \"%s\"\n", lc->thousands_sep);
    printf("Символ валюты: \"%s\"\n", lc->currency_symbol);
    printf("Международный символ: \"%s\"\n", lc->int_curr_symbol);

    return 0;
}
```

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Единая структура для всех параметров локали | Указатели на строки могут стать невалидными после смены локали |
| Поддерживает международные и локальные денежные форматы | Поля `char` ограничены диапазоном значений |
| Возвращается одной функцией `localeconv` | Не все поля определены для каждой локали |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<locale.h>/localeconv|localeconv]] -- функция, заполняющая `struct lconv`
- [[Языки программирования/C/Библиотеки/<locale.h>/setlocale|setlocale]] -- установка текущей локали

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.11.1.1
- GNU C Library, заголовочный файл `locale.h`
