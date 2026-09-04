# <pthread.h>

[[Языки программирования/C/Библиотеки|Библиотеки]] / <pthread.h>

**Дата написания:** 04.09.2026

## Оглавление

### Константы отмены

- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_CANCEL_DISABLE|PTHREAD_CANCEL_DISABLE]] — отмена отключена
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_CANCEL_ENABLE|PTHREAD_CANCEL_ENABLE]] — отмена включена
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_CANCEL_DEFERRED|PTHREAD_CANCEL_DEFERRED]] — отложенная отмена
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_CANCEL_ASYNCHRONOUS|PTHREAD_CANCEL_ASYNCHRONOUS]] — немедленная отмена
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_CANCELED|PTHREAD_CANCELED]] — значение возврата отменённого потока

### Константы мьютексов

- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_MUTEX_DEFAULT|PTHREAD_MUTEX_DEFAULT]] — мьютекс по умолчанию
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_MUTEX_NORMAL|PTHREAD_MUTEX_NORMAL]] — обычный мьютекс
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_MUTEX_ERRORCHECK|PTHREAD_MUTEX_ERRORCHECK]] — мьютекс с проверкой ошибок
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_MUTEX_RECURSIVE|PTHREAD_MUTEX_RECURSIVE]] — рекурсивный мьютекс
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_MUTEX_ROBUST|PTHREAD_MUTEX_ROBUST]] — устойчивый мьютекс
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_MUTEX_STALLED|PTHREAD_MUTEX_STALLED]] — застрявший мьютекс

### Константыcheduling

- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_INHERIT_SCHED|PTHREAD_INHERIT_SCHED]] — наследование планирования
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_EXPLICIT_SCHED|PTHREAD_EXPLICIT_SCHED]] — явное планирование
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_SCOPE_PROCESS|PTHREAD_SCOPE_PROCESS]] — область видимости процесс
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_SCOPE_SYSTEM|PTHREAD_SCOPE_SYSTEM]] — область видимости система
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_PROCESS_PRIVATE|PTHREAD_PROCESS_PRIVATE]] — приватный процесс
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_PROCESS_SHARED|PTHREAD_PROCESS_SHARED]] — общий процесс
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_PRIO_NONE|PTHREAD_PRIO_NONE]] — нет приоритета
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_PRIO_INHERIT|PTHREAD_PRIO_INHERIT]] — наследование приоритета
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_PRIO_PROTECT|PTHREAD_PRIO_PROTECT]] — защита приоритета

### Константы создания потоков

- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_CREATE_DETACHED|PTHREAD_CREATE_DETACHED]] — отсоединённый поток
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_CREATE_JOINABLE|PTHREAD_CREATE_JOINABLE]] — присоединяемый поток

### Константы инициализации

- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_ONCE_INIT|PTHREAD_ONCE_INIT]] — однократная инициализация
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_BARRIER_SERIAL_THREAD|PTHREAD_BARRIER_SERIAL_THREAD]] — серийный поток барьера
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_MUTEX_INITIALIZER|PTHREAD_MUTEX_INITIALIZER]] — инициализатор мьютекса
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_COND_INITIALIZER|PTHREAD_COND_INITIALIZER]] — инициализатор переменной условия
- [[Языки программирования/C/Библиотеки/<pthread.h>/PTHREAD_RWLOCK_INITIALIZER|PTHREAD_RWLOCK_INITIALIZER]] — инициализатор блокировки чтения-записи

### Управление потоками

- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_create|pthread_create]] — создание потока
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_join|pthread_join]] — ожидание завершения потока
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_detach|pthread_detach]] — отсоединение потока
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_exit|pthread_exit]] — завершение потока
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_self|pthread_self]] — получение ID текущего потока
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_equal|pthread_equal]] — сравнение ID потоков
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_cancel|pthread_cancel]] — отмена потока
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_setcancelstate|pthread_setcancelstate]] — установка состояния отмены
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_setcanceltype|pthread_setcanceltype]] — установка типа отмены
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_testcancel|pthread_testcancel]] — проверка отмены
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_cleanup_push|pthread_cleanup_push]] — установка обработчика очистки
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_cleanup_pop|pthread_cleanup_pop]] — удаление обработчика очистки

### Атрибуты потока

- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_init|pthread_attr_init]] — инициализация атрибутов
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_destroy|pthread_attr_destroy]] — уничтожение атрибутов
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_setdetachstate|pthread_attr_setdetachstate]] — установка состояния отсоединения
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_getdetachstate|pthread_attr_getdetachstate]] — получение состояния отсоединения
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_setstacksize|pthread_attr_setstacksize]] — установка размера стека
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_getstacksize|pthread_attr_getstacksize]] — получение размера стека
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_setstack|pthread_attr_setstack]] — установка стека
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_getstack|pthread_attr_getstack]] — получение стека
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_setguardsize|pthread_attr_setguardsize]] — установка размера保护区
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_getguardsize|pthread_attr_getguardsize]] — получение размера保护区
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_setschedparam|pthread_attr_setschedparam]] — установка параметров планирования
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_getschedparam|pthread_attr_getschedparam]] — получение параметров планирования
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_setschedpolicy|pthread_attr_setschedpolicy]] — установка политики планирования
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_getschedpolicy|pthread_attr_getschedpolicy]] — получение политики планирования
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_setinheritsched|pthread_attr_setinheritsched]] — установка наследования планирования
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_getinheritsched|pthread_attr_getinheritsched]] — получение наследования планирования
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_setscope|pthread_attr_setscope]] — установка области видимости
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_attr_getscope|pthread_attr_getscope]] — получение области видимости

### Мьютексы

- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutex_init|pthread_mutex_init]] — инициализация мьютекса
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutex_destroy|pthread_mutex_destroy]] — уничтожение мьютекса
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutex_lock|pthread_mutex_lock]] — блокировка мьютекса
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutex_trylock|pthread_mutex_trylock]] — попытка блокировки
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutex_timedlock|pthread_mutex_timedlock]] — блокировка с таймаутом
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutex_unlock|pthread_mutex_unlock]] — разблокировка мьютекса
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutex_consistent|pthread_mutex_consistent]] — восстановление устойчивого мьютекса
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutex_getprioceiling|pthread_mutex_getprioceiling]] — получение приоритета потолка
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutex_setprioceiling|pthread_mutex_setprioceiling]] — установка приоритета потолка

### Атрибуты мьютексов

- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutexattr_init|pthread_mutexattr_init]] — инициализация атрибутов
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutexattr_destroy|pthread_mutexattr_destroy]] — уничтожение атрибутов
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutexattr_settype|pthread_mutexattr_settype]] — установка типа
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutexattr_gettype|pthread_mutexattr_gettype]] — получение типа
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutexattr_setpshared|pthread_mutexattr_setpshared]] — установка общности
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutexattr_getpshared|pthread_mutexattr_getpshared]] — получение общности
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutexattr_setprotocol|pthread_mutexattr_setprotocol]] — установка протокола
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutexattr_getprotocol|pthread_mutexattr_getprotocol]] — получение протокола
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutexattr_setprioceiling|pthread_mutexattr_setprioceiling]] — установка приоритета потолка
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutexattr_getprioceiling|pthread_mutexattr_getprioceiling]] — получение приоритета потолка
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutexattr_setrobust|pthread_mutexattr_setrobust]] — установка устойчивости
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_mutexattr_getrobust|pthread_mutexattr_getrobust]] — получение устойчивости

### Условия

- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_cond_init|pthread_cond_init]] — инициализация переменной условия
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_cond_destroy|pthread_cond_destroy]] — уничтожение переменной условия
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_cond_wait|pthread_cond_wait]] — ожидание условия
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_cond_timedwait|pthread_cond_timedwait]] — ожидание с таймаутом
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_cond_signal|pthread_cond_signal]] — сигнализирование условия
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_cond_broadcast|pthread_cond_broadcast]] — широковещательный сигнал

### Атрибуты условий

- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_condattr_init|pthread_condattr_init]] — инициализация атрибутов
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_condattr_destroy|pthread_condattr_destroy]] — уничтожение атрибутов
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_condattr_setpshared|pthread_condattr_setpshared]] — установка общности
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_condattr_getpshared|pthread_condattr_getpshared]] — получение общности
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_condattr_setclock|pthread_condattr_setclock]] — установка часов
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_condattr_getclock|pthread_condattr_getclock]] — получение часов

### Блокировки чтения-записи

- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_rwlock_init|pthread_rwlock_init]] — инициализация блокировки
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_rwlock_destroy|pthread_rwlock_destroy]] — уничтожение блокировки
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_rwlock_rdlock|pthread_rwlock_rdlock]] — блокировка на чтение
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_rwlock_tryrdlock|pthread_rwlock_tryrdlock]] — попытка блокировки на чтение
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_rwlock_timedrdlock|pthread_rwlock_timedrdlock]] — блокировка на чтение с таймаутом
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_rwlock_wrlock|pthread_rwlock_wrlock]] — блокировка на запись
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_rwlock_trywrlock|pthread_rwlock_trywrlock]] — попытка блокировки на запись
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_rwlock_timedwrlock|pthread_rwlock_timedwrlock]] — блокировка на запись с таймаутом
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_rwlock_unlock|pthread_rwlock_unlock]] — разблокировка

### Атрибуты блокировок чтения-записи

- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_rwlockattr_init|pthread_rwlockattr_init]] — инициализация атрибутов
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_rwlockattr_destroy|pthread_rwlockattr_destroy]] — уничтожение атрибутов
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_rwlockattr_setpshared|pthread_rwlockattr_setpshared]] — установка общности
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_rwlockattr_getpshared|pthread_rwlockattr_getpshared]] — получение общности

### Спин-блокировки

- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_spin_init|pthread_spin_init]] — инициализация спин-блокировки
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_spin_destroy|pthread_spin_destroy]] — уничтожение спин-блокировки
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_spin_lock|pthread_spin_lock]] — блокировка
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_spin_trylock|pthread_spin_trylock]] — попытка блокировки
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_spin_unlock|pthread_spin_unlock]] — разблокировка

### Барьеры

- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_barrier_init|pthread_barrier_init]] — инициализация барьера
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_barrier_destroy|pthread_barrier_destroy]] — уничтожение барьера
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_barrier_wait|pthread_barrier_wait]] — ожидание барьера

### Атрибуты барьеров

- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_barrierattr_init|pthread_barrierattr_init]] — инициализация атрибутов
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_barrierattr_destroy|pthread_barrierattr_destroy]] — уничтожение атрибутов
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_barrierattr_setpshared|pthread_barrierattr_setpshared]] — установка общности
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_barrierattr_getpshared|pthread_barrierattr_getpshared]] — получение общности

### Потоковые данные

- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_key_create|pthread_key_create]] — создание ключа потоковых данных
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_key_delete|pthread_key_delete]] — удаление ключа
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_setspecific|pthread_setspecific]] — установка значения потоковых данных
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_getspecific|pthread_getspecific]] — получение значения потоковых данных

### Прочие функции

- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_once|pthread_once]] — однократная инициализация
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_atfork|pthread_atfork]] — обработчик fork
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_getconcurrency|pthread_getconcurrency]] — получение уровня параллелизма
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_setconcurrency|pthread_setconcurrency]] — установка уровня параллелизма
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_getcpuclockid|pthread_getcpuclockid]] — получение clockid потока
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_getschedparam|pthread_getschedparam]] — получение параметров планирования
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_setschedparam|pthread_setschedparam]] — установка параметров планирования
- [[Языки программирования/C/Библиотеки/<pthread.h>/pthread_setschedprio|pthread_setschedprio]] — установка приоритета планирования

## Описание библиотеки

Заголовочный файл `<pthread.h>` — потоки. Определяет константы, типы и функции для работы с потоками POSIX (pthreads).

### Константы отмены

| Константа | Описание |
|---|---|
| `PTHREAD_CANCEL_ENABLE` | Отмена включена (по умолчанию) |
| `PTHREAD_CANCEL_DISABLE` | Отмена отключена |
| `PTHREAD_CANCEL_DEFERRED` | Отмена откладывается до точки отмены |
| `PTHREAD_CANCEL_ASYNCHRONOUS` | Отмена выполняется немедленно |

### Константы мьютексов

| Константа | Описание |
|---|---|
| `PTHREAD_MUTEX_NORMAL` | Поведение по умолчанию; Deadlock detection не определена |
| `PTHREAD_MUTEX_ERRORCHECK` | Проверка ошибок; повторная блокировка возвращает `EDEADLK` |
| `PTHREAD_MUTEX_RECURSIVE` | Рекурсивная блокировка; подсчёт блокировок |
| `PTHREAD_MUTEX_DEFAULT` | Зависит от реализации |

### Инициализаторы

```c
pthread_mutex_t  mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t   cond  = PTHREAD_COND_INITIALIZER;
pthread_rwlock_t rwlock = PTHREAD_RWLOCK_INITIALIZER;
```

### Функции управления потоками

| Функция | Описание |
|---|---|
| `pthread_create(...)` | Создание нового потока |
| `pthread_join(pthread_t, void **)` | Ожидание завершения потока |
| `pthread_detach(pthread_t)` | Отсоединение потока |
| `pthread_exit(void *)` | Завершение текущего потока |
| `pthread_self(void)` | Возврат ID текущего потока |
| `pthread_equal(pthread_t, pthread_t)` | Сравнение двух ID потоков |
| `pthread_cancel(pthread_t)` | Отмена потока |

### Функции мьютексов

| Функция | Описание |
|---|---|
| `pthread_mutex_init(...)` | Инициализация мьютекса |
| `pthread_mutex_destroy(...)` | Уничтожение мьютекса |
| `pthread_mutex_lock(...)` | Блокировка мьютекса |
| `pthread_mutex_trylock(...)` | Неблокирующая попытка блокировки |
| `pthread_mutex_timedlock(...)` | Блокировка с таймаутом |
| `pthread_mutex_unlock(...)` | Разблокировка мьютекса |

### Функции условий

| Функция | Описание |
|---|---|
| `pthread_cond_init(...)` | Инициализация переменной условия |
| `pthread_cond_destroy(...)` | Уничтожение переменной условия |
| `pthread_cond_wait(...)` | Ожидание условия (атомарно с мьютексом) |
| `pthread_cond_timedwait(...)` | Ожидание с таймаутом |
| `pthread_cond_signal(...)` | Пробуждение одного ожидающего потока |
| `pthread_cond_broadcast(...)` | Пробуждение всех ожидающих потоков |

## Исключения

- **NULL:** функции не принимают `NULL` в качестве аргументов (кроме `pthread_getspecific()`).
- **Возвращаемое значение:** все функции возвращают `0` при успехе или номер ошибки (положительное число).
- **EINVAL:** неверный атрибут или неинициализированный объект.
- **EBUSY:** объект уже используется (при уничтожении).
- **EDEADLK:** обнаружен deadlock (для `PTHREAD_MUTEX_ERRORCHECK`).
- **EPERM:** нет прав (для `PTHREAD_MUTEX_ROBUST`).
- **ENOMEM:** недостаточно памяти.
- **ETIMEDOUT:** таймаут (для `_timedwait` и `_timedlock` функций).
- **Многопоточность:** функции потокобезопасны по определению.

## Стандарты

POSIX.1-2017.

## Источники

- https://man7.org/linux/man-pages/man0/pthread.h.0p.html
- `/usr/include/pthread.h`

[[Языки программирования/C/Библиотеки|Содержание]]
