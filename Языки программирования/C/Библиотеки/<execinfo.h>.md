# <execinfo.h>

[[Языки программирования/C/Библиотеки|Библиотеки]] / <execinfo.h>

**Дата написания:** 04.09.2026

## Оглавление

### Функции

- [[Языки программирования/C/Библиотеки/<execinfo.h>/backtrace|backtrace]] — получение адресов возврата
- [[Языки программирования/C/Библиотеки/<execinfo.h>/backtrace_symbols|backtrace_symbols]] — преобразование адресов в имена функций
- [[Языки программирования/C/Библиотеки/<execinfo.h>/backtrace_symbols_fd|backtrace_symbols_fd]] — вывод имён функций в файловый дескриптор

## Описание библиотеки

Заголовочный файл `<execinfo.h>` — трассировка стека. Определяет функции для получения и вывода трассировки стека (backtrace), полезные для отладки и диагностики.

### Функции

| Функция | Описание |
|---|---|
| `backtrace(void **array, int size)` | Сохраняет до `size` адресов возврата в `array`; возвращает количество сохранённых |
| `backtrace_symbols(void *const *array, int size)` | Преобразует массив адресов в массив строк с именами функций; выделяет память через `malloc()` |
| `backtrace_symbols_fd(void *const *array, int size, int fd)` | Выводит имена функций в файловый дескриптор `fd` |

### Возвращаемое значение

- `backtrace()`: количество сохранённых адресов (меньше `size` если стек короче).
- `backtrace_symbols()`: указатель на массив строк или `NULL` при ошибке.
- `backtrace_symbols_fd()`: ничего не возвращает.

### Использование

```c
#include <execinfo.h>
#include <stdio.h>
#include <stdlib.h>

void print_backtrace(void) {
    void *buffer[128];
    int n = backtrace(buffer, 128);
    char **symbols = backtrace_symbols(buffer, n);
    if (symbols == NULL) {
        perror("backtrace_symbols");
        return;
    }
    for (int i = 0; i < n; i++) {
        printf("%s\n", symbols[i]);
    }
    free(symbols);
}
```

## Исключения

- **NULL:** `backtrace_symbols()` возвращает `NULL` при ошибке выделения памяти.
- **Память:** `backtrace_symbols()` выделяет память через `malloc()`; освобождайте через `free()`.
- **Точность:** имена функций могут быть неточными (особенно без `-rdynamic` при компиляции).
- **Компиляция:** используйте `-rdynamic` для получения имён функций.
- **Не POSIX:** функции не являются частью POSIX; доступны в glibc и BSD.
- **Многопоточность:** функции потокобезопасны.

## Стандарты

glibc, BSD (не POSIX).

## Источники

- `/usr/include/execinfo.h`

[[Языки программирования/C/Библиотеки|Содержание]]
