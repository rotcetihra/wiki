# fetestexcept

[[Языки программирования/C/Глава 10. Стандартная библиотека C|Глава 10. Стандартная библиотека C]] / [[Языки программирования/C/Глава 10. Стандартная библиотека C/<fenv.h>|<fenv.h>]] / fetestexcept

[[Языки программирования/C/Глава 10. Стандартная библиотека C/<fenv.h>/fesetexceptflag|Назад]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<fenv.h>|Содержание]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<fenv.h>/fegetround|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <fenv.h>

int fetestexcept(int excepts);
```

## Описание

Функция `fetestexcept` определяет, какие из указанных исключений в настоящее время активны (установлены). Параметр `excepts` — побитовая маска проверяемых исключений.

Функция возвращает побитовое И исключений `excepts` с текущими активными флагами. Например, если активны `FE_DIVBYZERO` и `FE_INVALID`, а `excepts` равен `FE_DIVBYZERO | FE_INVALID | FE_OVERFLOW`, функция вернёт `FE_DIVBYZERO | FE_INVALID`.

Для проверки конкретного исключения используется идиома:

```c
if (fetestexcept(FE_INVALID) & FE_INVALID) {
    // FE_INVALID активно
}
```

Или более компактно (поскольку `fetestexcept` возвращает только те биты, которые запрошены):

```c
if (fetestexcept(FE_INVALID)) {
    // FE_INVALID активно
}
```

## Пример

```c
#include <stdio.h>
#include <fenv.h>
#include <math.h>

int main(void)
{
    feclearexcept(FE_ALL_EXCEPT);

    volatile double a = 0.0;
    volatile double b = 0.0;
    volatile double c = a / b;

    volatile double d = -1.0;
    double e = sqrt(d);

    int active = fetestexcept(FE_ALL_EXCEPT);
    printf("Активные исключения: 0x%x\n", active);

    if (active & FE_INVALID)
        printf("  FE_INVALID\n");
    if (active & FE_DIVBYZERO)
        printf("  FE_DIVBYZERO\n");

    feclearexcept(FE_ALL_EXCEPT);
    printf("После сброса: %d\n", fetestexcept(FE_ALL_EXCEPT));

    return 0;
}
```

## Параметры

| Параметр | Описание |
|---|---|
| `excepts` | Побитовая маска проверяемых исключений |

## Возвращаемое значение

| Значение | Описание |
|---|---|
| Побитовое И `excepts` с активными флагами | Биты, соответствующие активным исключениям из `excepts` |

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Позволяет проверить несколько исключений за один вызов | Не сбрасывает флаги — только проверяет |
| Не имеет побочных эффектов | Возвращает маску, а не отдельные значения |
| Стандартная функция ISO C99/C23 | Для проверки одного исключения нужна маска |

## Похожие функции

- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<fenv.h>/feclearexcept|feclearexcept]] — сброс исключений
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<fenv.h>/feraiseexcept|feraiseexcept]] — генерация исключений
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<fenv.h>/FE_ALL_EXCEPT|FE_ALL_EXCEPT]] — маска всех исключений

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.6.5.5
- GNU C Library, заголовочный файл `fenv.h`
