# fpclassify

[[Языки программирования/C/Глава 10. Стандартная библиотека C|Глава 10. Стандартная библиотека C]] / [[Языки программирования/C/Глава 10. Стандартная библиотека C/<math.h>|<math.h>]] / fpclassify

[[Языки программирования/C/Глава 10. Стандартная библиотека C/<math.h>/fmin|Назад]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<math.h>|Содержание]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<math.h>/isfinite|Вперёд]]

**Дата написания:** 18.08.2026

## Определение

```c
#include <math.h>

#define fpclassify(x) /* implementation-defined */
```

## Описание

Макрос классифицирует значение с плавающей точкой. Возвращает одно из шести значений: `FP_NAN` (не число), `FP_INFINITE` (бесконечность), `FP_ZERO` (нуль), `FP_SUBNORMAL` (денормализованное число), `FP_NORMAL` (нормализованное число) или `FP_UNORDERED` (не определено).

## Примеры

```c
#include <math.h>
#include <stdio.h>

int main(void) {
    double values[] = {0.0, 1.0, INFINITY, NAN, 0.0000001};
    const char *names[] = {"0.0", "1.0", "INFINITY", "NAN", "0.0000001"};
    
    for (int i = 0; i < 5; i++) {
        int result = fpclassify(values[i]);
        printf("fpclassify(%s) = ", names[i]);
        switch (result) {
            case FP_ZERO:         printf("FP_ZERO\n"); break;
            case FP_NORMAL:       printf("FP_NORMAL\n"); break;
            case FP_INFINITE:     printf("FP_INFINITE\n"); break;
            case FP_NAN:          printf("FP_NAN\n"); break;
            case FP_SUBNORMAL:    printf("FP_SUBNORMAL\n"); break;
            case FP_UNORDERED:    printf("FP_UNORDERED\n"); break;
        }
    }
    
    return 0;
}
```

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Позволяет точно определить тип числа | Возвращает макрос, а не функцию |
| Быстрая операция |  |

## Похожие определения

- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<math.h>/isfinite|isfinite]] — проверка на конечность
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<math.h>/isinf|isinf]] — проверка на бесконечность
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<math.h>/isnan|isnan]] — проверка на NaN

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.12.11.1
- GNU C Library, заголовочный файл `math.h`