# pthread_mutex_init

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<pthread.h>|<pthread.h>]] / pthread_mutex_init

[[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_self|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_mutex_lock|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <pthread.h>
int pthread_mutex_init(pthread_mutex_t *mutex,
                       const pthread_mutexattr_t *attr);
```

## Параметры

| Параметр | Описание |
|---|---|
| `mutex` | указатель на мьютекс |
| `attr` | атрибуты мьютекса (NULL — по умолчанию) |
## Возвращаемое значение

0 при успехе, код ошибки при неудаче.

## Что делает

Инициализирует мьютекс с атрибутами по умолчанию или указанными в `attr`.

## Примеры

### Базовое использование

```cpp
pthread_mutex_t mutex;
pthread_mutex_init(&mutex, NULL);
// использование
pthread_mutex_destroy(&mutex);
```

## Исexceptions

- **Исключения:** Возвращает код ошибки (EINVAL, EBUSY, ENOMEM).
- **Безопасность в C++11:** Потокобезопасна для разных мьютексов.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_mutex_lock|pthread_mutex_lock]]

## Источники

- https://man7.org/linux/man-pages/man3/pthread_mutex_init.3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_self|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_mutex_lock|Вперёд]]
