# fesetexceptflag

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<fenv.h>|<fenv.h>]] / fesetexceptflag

[[Языки программирования/C/Библиотеки/<fenv.h>/feraiseexcept|Назад]] | [[Языки программирования/C/Библиотеки/<fenv.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<fenv.h>/fetestexcept|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <fenv.h>

int fesetexceptflag(const fexcept_t *flagp, int excepts);
```

## Описание

Функция `fesetexceptflag` устанавливает текущие флаги исключений на основе сохранённого ранее значения `flagp` (полученного через `fegetexceptflag`). Параметр `excepts` — побитовая маска флагов, которые следует восстановить.

Функция не генерирует новые исключения — она лишь восстанавливает ранее сохранённое состояние флагов. Если в `flagp` были установлены флаги `FE_DIVBYZERO` и `FE_INVALID`, и `excepts` содержит `FE_DIVBYZERO`, то будет установлен только `FE_DIVBYZERO`.

Функция возвращает `0` при успешном выполнении и ненулевое значение при ошибке.

> [!NOTE]
> Эта функция восстанавливает только флаги исключений, а не направление округления. Для полного восстановления среды используйте `fesetenv`.

## Пример

```c
#include <stdio.h>
#include <fenv.h>

int main(void)
{
    fexcept_t saved;

    feraiseexcept(FE_INVALID | FE_DIVBYZERO);
    fegetexceptflag(&saved, FE_ALL_EXCEPT);
    printf("Сохранено: 0x%x\n", fetestexcept(FE_ALL_EXCEPT));

    feclearexcept(FE_ALL_EXCEPT);
    printf("После сброса: 0x%x\n", fetestexcept(FE_ALL_EXCEPT));

    fesetexceptflag(&saved, FE_INVALID);
    printf("Восстановлен только FE_INVALID: 0x%x\n", fetestexcept(FE_ALL_EXCEPT));

    fesetexceptflag(&saved, FE_DIVBYZERO);
    printf("Восстановлен FE_DIVBYZERO: 0x%x\n", fetestexcept(FE_ALL_EXCEPT));

    return 0;
}
```

## Параметры

| Параметр | Описание |
|---|---|
| `flagp` | Указатель на ранее сохранённые флаги (`fexcept_t`) |
| `excepts` | Побитовая маска флагов для восстановления |

## Возвращаемое значение

| Значение | Описание |
|---|---|
| `0` | Флаги успешно восстановлены |
| Ненулевое | Ошибка восстановления |

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Позволяет избирательно восстановить флаги | Не восстанавливает направление округления |
| Совместима с `fegetexceptflag` | Не генерирует реальных исключений — только устанавливает флаги |
| Не затрагивает флаги, не указанные в `excepts` | — |

## Похожие функции

- [[Языки программирования/C/Библиотеки/<fenv.h>/fegetexceptflag|fegetexceptflag]] — сохранение флагов в `fexcept_t`
- [[Языки программирования/C/Библиотеки/<fenv.h>/fesetenv|fesetenv]] — восстановление полной среды (включая округление)
- [[Языки программирования/C/Библиотеки/<fenv.h>/fexcept_t|fexcept_t]] — тип для хранения флагов

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.6.5.4
- GNU C Library, заголовочный файл `fenv.h`
