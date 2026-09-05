# pthread_once

[[Языки программирования/C++/Библиотеки|Библиотеки]] / [[Языки программирования/C++/Библиотеки/<pthread.h>|<pthread.h>]] / pthread_once

[[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_getspecific|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]

**Дата написания:** 05.09.2026

## Прототип

```cpp
#include <pthread.h>
int pthread_once(pthread_once_t *once_control,
                 void (*init_routine)(void));
```

## Параметры

| Параметр | Описание |
|---|---|
| `once_control` | указатель на переменную `pthread_once_t`, инициализированную `PTHREAD_ONCE_INIT` |
| `init_routine` | функция инициализации |
## Возвращаемое значение

0 при успехе, код ошибки при неудаче.

## Что делает

Гарантирует, что функция `init_routine` будет вызвана ровно один раз, даже если несколько потоков вызывают `pthread_once()` одновременно.

## Примеры

### Базовое использование

```cpp
static pthread_once_t once = PTHREAD_ONCE_INIT;

void init() {
    // инициализация
}

void *thread_func(void *arg) {
    pthread_once(&once, init);
    // ...
}
```

## Исexceptions

- **Исключения:** Возвращает код ошибки.
- **Безопасность в C++11:** Потокобезопасна.

## Похожие функции

- [[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_key_create|pthread_key_create]]

## Источники

- https://man7.org/linux/man-pages/man3/pthread_once.3.html
- POSIX.1-2024 (IEEE Std 1003.1-2024)

[[Языки программирования/C++/Библиотеки/<pthread.h>/pthread_getspecific|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]]
