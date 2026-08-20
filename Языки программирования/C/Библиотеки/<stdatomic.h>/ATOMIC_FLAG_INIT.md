# ATOMIC_FLAG_INIT

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<stdatomic.h>|<stdatomic.h>]] / ATOMIC_FLAG_INIT

[[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_flag|Назад]] | [[Языки программирования/C/Библиотеки/<stdatomic.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<stdatomic.h>/ATOMIC_VAR_INIT|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <stdatomic.h>

#define ATOMIC_FLAG_INIT /* implementation-defined */
```

## Описание

Макрос `ATOMIC_FLAG_INIT` используется для инициализации переменных типа `atomic_flag` в начальное состояние (очищенное). Это единственный способ инициализации `atomic_flag` в C11/C17.

В C23 макрос был объявлен устаревшим — вместо него рекомендуется использовать `atomic_flag_clear` или инициализатор `{0}`.

> [!NOTE]
> Инициализация через `ATOMIC_FLAG_INIT` выполняется во время выполнения программы (не в этапе инициализации статических объектов). Для статических объектов используйте `{0}`.

## Пример

```c
#include <stdio.h>
#include <stdatomic.h>

atomic_flag flag1 = ATOMIC_FLAG_INIT;
atomic_flag flag2 = ATOMIC_FLAG_INIT;

int main(void)
{
    printf("flag1 установлена: %d\n", atomic_flag_test_and_set(&flag1));
    atomic_flag_clear(&flag1);
    printf("flag2 установлена: %d\n", atomic_flag_test_and_set(&flag2));
    return 0;
}
```

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Единственный способ инициализации `atomic_flag` в C11/C17 | Устарел в C23 |
| Гарантирует начальное очищенное состояние | Не подходит для статических объектов |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_flag|atomic_flag]] — тип атомарного флага
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/ATOMIC_VAR_INIT|ATOMIC_VAR_INIT]] — инициализация атомарных переменных (устарела)

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.17.2.1
- GNU C Library, заголовочный файл `stdatomic.h`
