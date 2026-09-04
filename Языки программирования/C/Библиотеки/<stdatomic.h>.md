# <stdatomic.h>

[[Языки программирования/C/Библиотеки|Библиотеки]] / <stdatomic.h>

[[Языки программирования/C/Библиотеки/<stdarg.h>|Назад]] | [[Языки программирования/C/Библиотеки|Содержание]] | [[Языки программирования/C/Библиотеки/<stdbit.h>|Вперёд]]

**Дата написания:** 20.08.2026
**Дата обновления:** 04.09.2026

## Оглавление

### Типы

- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_flag|atomic_flag]] — атомарный флаг с test-and-set
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/memory_order|memory_order]] — порядок памяти для атомарных операций

### Макросы

- [[Языки программирования/C/Библиотеки/<stdatomic.h>/ATOMIC_FLAG_INIT|ATOMIC_FLAG_INIT]] — инициализатор для `atomic_flag`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/ATOMIC_VAR_INIT|ATOMIC_VAR_INIT]] — инициализатор для атомарных объектов (устаревший)
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/kill_dependency|kill_dependency]] — разрыв цепочки зависимостей

### Атомарные типы

- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_bool|atomic_bool]] — атомарный `_Bool`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_char|atomic_char]] — атомарный `char`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_int|atomic_int]] — атомарный `int`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_long|atomic_long]] — атомарный `long`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_llong|atomic_llong]] — атомарный `long long`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_size_t|atomic_size_t]] — атомарный `size_t`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_ptrdiff_t|atomic_ptrdiff_t]] — атомарный `ptrdiff_t`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_intptr_t|atomic_intptr_t]] — атомарный `intptr_t`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_uintptr_t|atomic_uintptr_t]] — атомарный `uintptr_t`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_intmax_t|atomic_intmax_t]] — атомарный `intmax_t`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_uintmax_t|atomic_uintmax_t]] — атомарный `uintmax_t`

### Макросы lock-free

- [[Языки программирования/C/Библиотеки/<stdatomic.h>/ATOMIC_BOOL_LOCK_FREE|ATOMIC_BOOL_LOCK_FREE]] — lock-free для `_Bool`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/ATOMIC_CHAR_LOCK_FREE|ATOMIC_CHAR_LOCK_FREE]] — lock-free для `char`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/ATOMIC_SHORT_LOCK_FREE|ATOMIC_SHORT_LOCK_FREE]] — lock-free для `short`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/ATOMIC_INT_LOCK_FREE|ATOMIC_INT_LOCK_FREE]] — lock-free для `int`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/ATOMIC_LONG_LOCK_FREE|ATOMIC_LONG_LOCK_FREE]] — lock-free для `long`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/ATOMIC_LLONG_LOCK_FREE|ATOMIC_LLONG_LOCK_FREE]] — lock-free для `long long`
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/ATOMIC_POINTER_LOCK_FREE|ATOMIC_POINTER_LOCK_FREE]] — lock-free для указателей

### Функции сравнения и обмена

- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_compare_exchange_strong|atomic_compare_exchange_strong]] — условная замена (сильная)
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_compare_exchange_strong_explicit|atomic_compare_exchange_strong_explicit]] — то же с явным порядком памяти
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_compare_exchange_weak|atomic_compare_exchange_weak]] — условная замена (слабая)
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_compare_exchange_weak_explicit|atomic_compare_exchange_weak_explicit]] — то же с явным порядком памяти
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_exchange|atomic_exchange]] — обмен значений
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_exchange_explicit|atomic_exchange_explicit]] — то же с явным порядком памяти

### Функции загрузки и сохранения

- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_load|atomic_load]] — атомарная загрузка
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_load_explicit|atomic_load_explicit]] — то же с явным порядком памяти
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_store|atomic_store]] — атомарное сохранение
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_store_explicit|atomic_store_explicit]] — то же с явным порядком памяти

### Арифметические операции

- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_fetch_add|atomic_fetch_add]] — атомарное сложение
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_fetch_add_explicit|atomic_fetch_add_explicit]] — то же с явным порядком памяти
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_fetch_sub|atomic_fetch_sub]] — атомарное вычитание
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_fetch_sub_explicit|atomic_fetch_sub_explicit]] — то же с явным порядком памяти

### Битовые операции

- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_fetch_and|atomic_fetch_and]] — атомарное И
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_fetch_and_explicit|atomic_fetch_and_explicit]] — то же с явным порядком памяти
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_fetch_or|atomic_fetch_or]] — атомарное ИЛИ
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_fetch_or_explicit|atomic_fetch_or_explicit]] — то же с явным порядком памяти
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_fetch_xor|atomic_fetch_xor]] — атомарное XOR
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_fetch_xor_explicit|atomic_fetch_xor_explicit]] — то же с явным порядком памяти

### Функции инициализации и проверки

- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_init|atomic_init]] — инициализация атомарного объекта
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_is_lock_free|atomic_is_lock_free]] — проверка, является ли тип lock-free

### Операции с `atomic_flag`

- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_flag_test_and_set|atomic_flag_test_and_set]] — установка флага и возврат старого значения
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_flag_test_and_set_explicit|atomic_flag_test_and_set_explicit]] — то же с явным порядком памяти
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_flag_clear|atomic_flag_clear]] — сброс флага
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_flag_clear_explicit|atomic_flag_clear_explicit]] — то же с явным порядком памяти

### Барьеры памяти

- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_signal_fence|atomic_signal_fence]] — барьер для обработчиков сигналов
- [[Языки программирования/C/Библиотеки/<stdatomic.h>/atomic_thread_fence|atomic_thread_fence]] — барьер для потоков

## Описание библиотеки

Заголовочный файл `<stdatomic.h>` — атомарные операции. Этот заголовок предоставляет типы и функции для выполнения атомарных операций, которые гарантируют целостность данных в многопоточной среде.

> [!NOTE]
> Реализации, определяющие макрос `__STDC_NO_ATOMICS__`, не обязаны предоставлять этот заголовок.

### Типы

| Тип | Описание |
|---|---|
| `atomic_flag` | Структурный тип для классического test-and-set; всегда lock-free |
| `memory_order` | Перечисление порядков памяти |

### Порядки памяти (`memory_order`)

| Константа | Описание |
|---|---|
| `memory_order_relaxed` | Нет ограничений на reordered операции |
| `memory_order_consume` | Зависимые от загрузки операции не перемещаются вверх |
| `memory_order_acquire` | Операции чтения не перемещаются вверх |
| `memory_order_release` | Операции записи не перемещаются вниз |
| `memory_order_acq_rel` | Комбинация acquire и release |
| `memory_order_seq_cst` | Последовательно согласованный порядок (по умолчанию) |

### Макросы lock-free

Значения макросов:
- `0` — тип никогда не является lock-free
- `1` — тип иногда является lock-free
- `2` — тип всегда является lock-free

## Исключения

- **NULL:** атомарные операции не принимают `NULL`; передача `NULL` — неопределённое поведение.
- **errno:** атомарные операции не устанавливают `errno`.
- **Переполнение:** атомарные арифметические операции не генерируют исключений переполнения; результат определяется по модулю.
- **Нехватка памяти:** не применимо.
- **Граничные случаи:** `atomic_flag` неявно инициализируется в неопределённое состояние; используйте `ATOMIC_FLAG_INIT`.
- **Многопоточность:** атомарные операции предназначены для многопоточной среды и гарантированно потокобезопасны.
- **Устаревший:** `ATOMIC_VAR_INIT` объявлен устаревшим в C23.

## Стандарты

C11, POSIX.1-2024.

## Источники

- https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/stdatomic.h.html
- `/usr/include/stdatomic.h`
- ISO/IEC 9899:2024 (C23), раздел 7.17

## См. также

- `<threads.h>` — многопоточность (POSIX pthreads)

[[Языки программирования/C/Библиотеки/<stdarg.h>|Назад]] | [[Языки программирования/C/Библиотеки|Содержание]] | [[Языки программирования/C/Библиотеки/<stdbit.h>|Вперёд]]
