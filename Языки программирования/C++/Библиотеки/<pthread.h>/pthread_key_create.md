# pthread_key_create

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<pthread.h>|<pthread.h>]] / pthread_key_create

[[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_cond_destroy|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_key_delete|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <pthread.h>
int pthread_key_create(pthread_key_t *key,
                       void (*destructor)(void *));
```

## Параметры

| Параметр | Описание |
|---|---|
| `key` | указатель на ключ |
| `destructor` | деструктор (вызывается при завершении потока) |
## Возвращаемое значение

0 при успехе, код ошибки при неудаче.

## Что делает

Создаёт ключ для доступа к локальным данным потока (thread-specific data). Каждый поток может установить своё значение через `pthread_setspecific()`.

## Примеры

### Базовое использование

```cpp
pthread_key_t key;
pthread_key_create(&key, free);
pthread_setspecific(key, strdup("data"));
```

## Исexceptions

- **Исключения:** Возвращает код ошибки (EAGAIN, ENOMEM).
- **Безопасность в C++11:** Потокобезопасна.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_key_delete|pthread_key_delete]]

## Источники

- https://man7.org/linux/man-pages/man3/pthread_key_create.3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_cond_destroy|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_key_delete|Вперёд]]
