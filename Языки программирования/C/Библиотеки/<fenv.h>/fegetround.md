# fegetround

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<fenv.h>|<fenv.h>]] / fegetround

[[Языки программирования/C/Библиотеки/<fenv.h>/fetestexcept|Назад]] | [[Языки программирования/C/Библиотеки/<fenv.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<fenv.h>/fesetround|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <fenv.h>

int fegetround(void);
```

## Описание

Функция `fegetround` возвращает текущее направление округления. Возвращаемое значение является одной из констант: `FE_DOWNWARD`, `FE_TONEAREST`, `FE_TOWARDZERO` или `FE_UPWARD`.

Функция не имеет параметров и не генерирует ошибок. Если текущее направление не соответствует ни одной из поддерживаемых констант, поведение не определено (на практике это невозможно на стандартных платформах).

Для изменения направления округления используется `fesetround`.

## Пример

```c
#include <stdio.h>
#include <fenv.h>

const char *rounding_name(int mode)
{
    switch (mode) {
        case FE_DOWNWARD:   return "FE_DOWNWARD";
        case FE_TONEAREST:  return "FE_TONEAREST";
        case FE_TOWARDZERO: return "FE_TOWARDZERO";
        case FE_UPWARD:     return "FE_UPWARD";
        default:            return "неизвестно";
    }
}

int main(void)
{
    printf("Текущее направление: %s\n", rounding_name(fegetround()));

    fesetround(FE_TOWARDZERO);
    printf("После установки: %s\n", rounding_name(fegetround()));

    fesetround(FE_TONEAREST);
    printf("Восстановлено: %s\n", rounding_name(fegetround()));

    return 0;
}
```

## Возвращаемое значение

| Значение | Описание |
|---|---|
| `FE_DOWNWARD` | Округление к минус бесконечности |
| `FE_TONEAREST` | Округление к ближайшему (по умолчанию IEEE 754) |
| `FE_TOWARDZERO` | Округление к нулю (усечение) |
| `FE_UPWARD` | Округление к плюс бесконечности |

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Простая проверка текущего направления | Не позволяет установить направление (нужен `fesetround`) |
| Не имеет побочных эффектов | Возвращает `int`, а не перечисление |
| Стандартная функция ISO C99/C23 | — |

## Похожие функции

- [[Языки программирования/C/Библиотеки/<fenv.h>/fesetround|fesetround]] — установка направления округления
- [[Языки программирования/C/Библиотеки/<fenv.h>/FE_DOWNWARD|FE_DOWNWARD]] — округление к минус бесконечности
- [[Языки программирования/C/Библиотеки/<fenv.h>/FE_TONEAREST|FE_TONEAREST]] — округление к ближайшему
- [[Языки программирования/C/Библиотеки/<fenv.h>/FE_TOWARDZERO|FE_TOWARDZERO]] — округление к нулю
- [[Языки программирования/C/Библиотеки/<fenv.h>/FE_UPWARD|FE_UPWARD]] — округление к плюс бесконечности

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.6.6.1
- GNU C Library, заголовочный файл `fenv.h`
