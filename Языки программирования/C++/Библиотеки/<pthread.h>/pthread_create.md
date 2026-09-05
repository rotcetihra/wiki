# pthread_create

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<pthread.h>|<pthread.h>]] / pthread_create

[[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_join|Вперёд]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <pthread.h>
int pthread_create(pthread_t *thread, const pthread_attr_t *attr,
                   void *(*start_routine)(void *), void *arg);
```

## Параметры

| Параметр | Описание |
|---|---|
| `thread` | указатель на идентификатор нового потока |
| `attr` | атрибуты потока (NULL — по умолчанию) |
| `start_routine` | функция, которую выполняет поток |
| `arg` | аргумент функции потока |
## Возвращаемое значение

0 при успехе, код ошибки при неудаче.

## Что делает

Создаёт новый поток, который начинает выполнение с функции `start_routine`, передавая ей аргумент `arg`.

## Примеры

### Базовое использование

```cpp
void *thread_func(void *arg) {
    printf("Поток работает");
    return NULL;
}

pthread_t tid;
pthread_create(&tid, NULL, thread_func, NULL);
pthread_join(tid, NULL);
```

## Исexceptions

- **Исключения:** Возвращает код ошибки (EAGAIN, EINVAL, EPERM).
- **Безопасность в C++11:** Потокобезопасна.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_join|pthread_join]]

## Источники

- https://man7.org/linux/man-pages/man3/pthread_create.3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_join|Вперёд]]
