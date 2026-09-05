# pthread_mutex_unlock

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<pthread.h>|<pthread.h>]] / pthread_mutex_unlock

[[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_mutex_trylock|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_mutex_destroy|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <pthread.h>
int pthread_mutex_unlock(pthread_mutex_t *mutex);
```

## Параметры

| Параметр | Описание |
|---|---|
| `mutex` | указатель на мьютекс |
## Возвращаемое значение

0 при успехе, код ошибки при неудаче.

## Что делает

Разблокирует мьютекс, ранее заблокированный через `pthread_mutex_lock()` или `pthread_mutex_trylock()`.

## Примеры

### Базовое использование

```cpp
pthread_mutex_unlock(&mutex);
```

## Исexceptions

- **Исключения:** Возвращает код ошибки (EINVAL, EPERM).
- **Безопасность в C++11:** Потокобезопасна для разных мьютексов.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_mutex_lock|pthread_mutex_lock]]

## Источники

- https://man7.org/linux/man-pages/man3/pthread_mutex_unlock.3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_mutex_trylock|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_mutex_destroy|Вперёд]]
