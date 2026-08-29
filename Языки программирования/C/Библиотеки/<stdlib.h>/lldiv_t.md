# lldiv_t

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<stdlib.h>|<stdlib.h>]] / lldiv_t

[[Языки программирования/C/Библиотеки/<stdlib.h>/lldiv|Назад]] | [[Языки программирования/C/Библиотеки/<stdlib.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<stdlib.h>/malloc|Вперёд]]

**Дата написания:** 18.08.2026

## Определение

```c
#include <stdlib.h>

typedef struct {
    long long quot; // частное
    long long rem;  // остаток
} lldiv_t;
```

## Описание

Тип структуры, возвращаемой функцией `lldiv()`. Поля `quot` и `rem` — частное и остаток от целочисленного деления: `quot * denom + rem == numer`. Аналог `div_t`, но для `long long`. Доступен с C99.

## Примеры

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    lldiv_t r = lldiv(170LL, 5LL);

    printf("%lld %lld\n", r.quot, r.rem); // 34 0

    return 0;
}
```

## Похожие определения

- [[Языки программирования/C/Библиотеки/<stdlib.h>/lldiv|lldiv]] — функция, возвращающая `lldiv_t`
- [[Языки программирования/C/Библиотеки/<stdlib.h>/div_t|div_t]] — тип для `int`
- [[Языки программирования/C/Библиотеки/<stdlib.h>/ldiv_t|ldiv_t]] — тип для `long`

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.22.6.2
- GNU C Library, заголовочный файл `stdlib.h`