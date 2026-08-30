# atomic_compare_exchange

[[Языки программирования/C/Библиотеки|Библиотеки]] / [[Языки программирования/C/Библиотеки/<stdatomic.h>|<stdatomic.h>]] / atomic_compare_exchange

[[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_exchange|Назад]] | [[Языки программирования/C/Библиотеки/<stdatomic.h>|Содержание]] | [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_fetch_add|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <stdatomic.h>

bool atomic_compare_exchange_strong(volatile A *object, C *expected, C desired);
bool atomic_compare_exchange_weak(volatile A *object, C *expected, C desired);
bool atomic_compare_exchange_strong_explicit(volatile A *object, C *expected, C desired,
    memory_order success, memory_order failure);
bool atomic_compare_exchange_weak_explicit(volatile A *object, C *expected, C desired,
    memory_order success, memory_order failure);
```

## Описание

Функция `atomic_compare_exchange_strong` атомарно сравнивает значение `object` с `expected`. Если они равны, `object` заменяется на `desired` и функция возвращает `true`. Если не равны, `expected` обновляется текущим значением `object` и функция возвращает `false`.

Версия `weak` может вызвать ложные срабатывания (возврат `false` при равенстве значений) на некоторых архитектурах. Она эффективнее `strong` в циклах ожидания.

> [!NOTE]
> `atomic_compare_exchange_strong` — основной примитив для построения lock-free алгоритмов. `weak` версия допускает ложные срабатывания и должна использоваться только в циклах.

## Пример

```c
#include <stdio.h>
#include <stdatomic.h>

atomic_int counter = 0;

void increment(void)
{
    int expected = atomic_load(&counter);
    while (!atomic_compare_exchange_weak(&counter, &expected, expected + 1)) {
        expected = atomic_load(&counter);
    }
}

int main(void)
{
    increment();
    printf("Счётчик: %d\n", atomic_load(&counter));
    return 0;
}
```

## Параметры

| Параметр | Описание |
|---|---|
| `object` | Указатель на атомарную переменную |
| `expected` | Ожидаемое значение (обновляется при несовпадении) |
| `desired` | Новое значение при совпадении |
| `success` | Модель памяти при успехе (только `_explicit` версия) |
| `failure` | Модель памяти при неудаче (только `_explicit` версия) |

## Возвращаемое значение

| Значение | Описание |
|---|---|
| `true` | Значение совпало, выполнена замена |
| `false` | Значение не совпало, `expected` обновлён |

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Основной примитив lock-free алгоритмов | Сложный интерфейс |
| Поддерживает модели памяти | `weak` версия вызывает ложные срабатывания |
| Гарантия атомарности | — |

## Похожие определения

- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_exchange|atomic_exchange]] — атомарный обмен без условия
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_fetch_add|atomic_fetch_add]] — атомарное сложение

## Обработка ошибок

- **Поведение при передаче NULL:** поведение не определено. Указатели `object` и `expected` должны указывать на валидные атомарные и неатомарную переменные соответственно.
- **Установление errno:** функция не устанавливает `errno`.
- **Возвращаемое значение при ошибке:** не применимо — функция возвращает `true` при успехе и `false` при несовпадении значений.
- **Многопоточность:** операция является атомарной и потокобезопасной. Это основной примитив для построения lock-free алгоритмов. `weak` версия допускает ложные срабатывания и должна использоваться только в циклах.
- **Связанные функции:** `atomic_exchange` — атомарный обмен без условия; `atomic_fetch_add` — атомарное сложение.

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.17.7.4
- GNU C Library, заголовочный файл `stdatomic.h`
