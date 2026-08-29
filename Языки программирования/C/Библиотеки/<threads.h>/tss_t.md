# tss_t

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<threads.h>|<threads.h>]] / tss_t

[[Языки программирования/C/Библиотеки/<threads.h>/mtx_t|Назад]] | [[Языки программирования/C/Библиотеки/<threads.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<threads.h>/once_flag|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <threads.h>

typedef /* неопределённый тип */ tss_t;
```

## Описание

Тип `tss_t` представляет ключ потокового хранилища данных (Thread-Specific Storage). Каждый поток хранит собственное значение для данного ключа. Создаётся через `tss_create`, значения устанавливаются через `tss_set` и получаются через `tss_get`.

## Пример

```c
#include <stdio.h>
#include <threads.h>

tss_t key;

void destructor(void *val)
{
    printf("Освобождение: %d\n", *(int *)val);
}

int func(void *arg)
{
    int *val = malloc(sizeof(int));
    *val = 42;
    tss_set(key, val);
    printf("Значение: %d\n", *(int *)tss_get(key));
    return 0;
}

int main(void)
{
    tss_create(&key, destructor);
    thrd_t t;
    thrd_create(&t, func, NULL);
    thrd_join(t, NULL);
    tss_delete(key);
    return 0;
}
```

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Каждый поток хранит своё значение | Деструктор вызывается не более `TSS_DTOR_ITERATIONS` раз |
| Потокобезопасный доступ | Нельзя передать значение из одного потока в другой |

## Похожие типы

- [[Языки программирования/C/Библиотеки/<threads.h>/tss_dtor_t|tss_dtor_t]] — тип деструктора
- [[Языки программирования/C/Библиотеки/<threads.h>/tss_create|tss_create]] — создание ключа
- [[Языки программирования/C/Библиотеки/<threads.h>/tss_get|tss_get]] — получение значения
- [[Языки программирования/C/Библиотеки/<threads.h>/tss_set|tss_set]] — установка значения

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.26.6
