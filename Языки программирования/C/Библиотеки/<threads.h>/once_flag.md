# once_flag

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<threads.h>|<threads.h>]] / once_flag

[[Языки программирования/C/Библиотеки/<threads.h>/tss_t|Назад]] | [[Языки программирования/C/Библиотеки/<threads.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<threads.h>/tss_dtor_t|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <threads.h>

typedef /* неопределённый тип */ once_flag;
```

## Описание

Тип `once_flag` используется совместно с `call_once` для гарантии однократного выполнения функции, даже если несколько потоков вызывают `call_once` одновременно. Инициализируется макросом `ONCE_FLAG_INIT`.

## Пример

```c
#include <stdio.h>
#include <threads.h>

once_flag flag;

void init(void)
{
    printf("Инициализация выполнена\n");
}

int func(void *arg)
{
    call_once(&flag, init);
    return 0;
}

int main(void)
{
    flag = ONCE_FLAG_INIT;
    thrd_t t1, t2;
    thrd_create(&t1, func, NULL);
    thrd_create(&t2, func, NULL);
    thrd_join(t1, NULL);
    thrd_join(t2, NULL);
    return 0;
}
```

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Гарантия однократного выполнения | Нельзя сбросить флаг после использования |
| Потокобезопасный | — |

## Похожие типы

- [[Языки программирования/C/Библиотеки/<threads.h>/ONCE_FLAG_INIT|ONCE_FLAG_INIT]] — инициализатор
- [[Языки программирования/C/Библиотеки/<threads.h>/call_once|call_once]] — однократное выполнение функции

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.26.2
