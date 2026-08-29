# atomic_thread_fence

[[Языки программирования/C/Глава 10. Стандартная библиотека C|Глава 10. Стандартная библиотека C]] / [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdatomic.h>|<stdatomic.h>]] / atomic_thread_fence

[[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdatomic.h>/atomic_fetch_sub|Назад]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdatomic.h>|Содержание]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdatomic.h>/atomic_signal_fence|Вперёд]]

**Дата написания:** 20.08.2026

## Определение

```c
#include <stdatomic.h>

void atomic_thread_fence(memory_order order);
```

## Описание

Функция `atomic_thread_fence` устанавливает барьер памяти между потоками. Барьер запрещает компилятору и процессору выполнять переупорядочивание операций памяти через указанную границу.

Модели памяти:
- `memory_order_relaxed` — без барьера;
- `memory_order_acquire` — запрещает переупорядочивание чтений и записей после барьера;
- `memory_order_release` — запрещает переупорядочивание чтений и записей до барьера;
- `memory_order_acq_rel` — комбинация `acquire` и `release`;
- `memory_order_seq_cst` — последовательно согласованный порядок (самый строгий).

> [!NOTE]
> `atomic_thread_fence` не является атомарной операцией — она не влияет на значения переменных, а только на порядок их видимости.

## Пример

```c
#include <stdio.h>
#include <stdatomic.h>

atomic_int data = 0;
atomic_int ready = 0;

void producer(void)
{
    atomic_store(&data, 42);
    atomic_thread_fence(memory_order_release);
    atomic_store(&ready, 1);
}

void consumer(void)
{
    while (atomic_load(&ready) == 0) {}
    atomic_thread_fence(memory_order_acquire);
    printf("Данные: %d\n", atomic_load(&data));
}

int main(void)
{
    producer();
    consumer();
    return 0;
}
```

## Параметры

| Параметр | Описание |
|---|---|
| `order` | Модель памяти для барьера |

## Возвращаемое значение

Функция ничего не возвращает.

## Плюсы и минусы

| Преимущество | Недостаток |
|---|---|
| Управление порядком операций памяти | Сложно использовать правильно |
| Не требует атомарных переменных | Может снизить производительность |
| Портативна (стандартная часть C11) | — |

## Похожие определения

- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdatomic.h>/atomic_signal_fence|atomic_signal_fence]] — барьер для обработчиков сигналов
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<stdatomic.h>/atomic_store|atomic_store]] — атомарная запись

## Источники

- ISO/IEC 9899:2024 (C23), раздел 7.17.4.1
- GNU C Library, заголовочный файл `stdatomic.h`
