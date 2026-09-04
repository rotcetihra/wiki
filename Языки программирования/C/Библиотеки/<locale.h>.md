# <locale.h>

[[Языки программирования/C/Библиотеки|Библиотеки]] / <locale.h>

[[Языки программирования/C/Библиотеки/<inttypes.h>|Назад]] | [[Языки программирования/C/Библиотеки|Содержание]] | [[Языки программирования/C/Библиотеки/<setjmp.h>|Вперёд]]

**Дата написания:** 20.08.2026
**Дата обновления:** 31.08.2026

## Оглавление

### Типы

- [[Языки программирования/C/Библиотеки/<locale.h>/struct lconv|struct lconv]] — параметры форматирования локали
- [[Языки программирования/C/Библиотеки/<locale.h>/locale_t|locale_t]] — тип объекта локали

### Константы категорий локали

- [[Языки программирования/C/Библиотеки/<locale.h>/LC_ALL|LC_ALL]] — все категории локали
- [[Языки программирования/C/Библиотеки/<locale.h>/LC_COLLATE|LC_COLLATE]] — правила колляции (сортировки строк)
- [[Языки программирования/C/Библиотеки/<locale.h>/LC_CTYPE|LC_CTYPE]] — классификация и преобразование символов
- [[Языки программирования/C/Библиотеки/<locale.h>/LC_MESSAGES|LC_MESSAGES]] — категория сообщений (POSIX)
- [[Языки программирования/C/Библиотеки/<locale.h>/LC_MONETARY|LC_MONETARY]] — форматирование денежных значений
- [[Языки программирования/C/Библиотеки/<locale.h>/LC_NUMERIC|LC_NUMERIC]] — форматирование числовых значений
- [[Языки программирования/C/Библиотеки/<locale.h>/LC_TIME|LC_TIME]] — форматирование даты и времени
- [[Языки программирования/C/Библиотеки/<locale.h>/LC_GLOBAL_LOCALE|LC_GLOBAL_LOCALE]] — специальный дескриптор глобальной локали
- [[Языки программирования/C/Библиотеки/<locale.h>/NULL|NULL]] — нулевой указатель

### Маски для newlocale()

- [[Языки программирования/C/Библиотеки/<locale.h>/LC_COLLATE_MASK|LC_COLLATE_MASK]] — маска категории `LC_COLLATE`
- [[Языки программирования/C/Библиотеки/<locale.h>/LC_CTYPE_MASK|LC_CTYPE_MASK]] — маска категории `LC_CTYPE`
- [[Языки программирования/C/Библиотеки/<locale.h>/LC_MESSAGES_MASK|LC_MESSAGES_MASK]] — маска категории `LC_MESSAGES`
- [[Языки программирования/C/Библиотеки/<locale.h>/LC_MONETARY_MASK|LC_MONETARY_MASK]] — маска категории `LC_MONETARY`
- [[Языки программирования/C/Библиотеки/<locale.h>/LC_NUMERIC_MASK|LC_NUMERIC_MASK]] — маска категории `LC_NUMERIC`
- [[Языки программирования/C/Библиотеки/<locale.h>/LC_TIME_MASK|LC_TIME_MASK]] — маска категории `LC_TIME`
- [[Языки программирования/C/Библиотеки/<locale.h>/LC_ALL_MASK|LC_ALL_MASK]] — маска всех категорий

### Функции

- [[Языки программирования/C/Библиотеки/<locale.h>/localeconv|localeconv]] — получение параметров форматирования текущей локали
- [[Языки программирования/C/Библиотеки/<locale.h>/setlocale|setlocale]] — установка или запрос текущей локали
- [[Языки программирования/C/Библиотеки/<locale.h>/duplocale|duplocale]] — дублирование объекта локали
- [[Языки программирования/C/Библиотеки/<locale.h>/freelocale|freelocale]] — освобождение объекта локали
- [[Языки программирования/C/Библиотеки/<locale.h>/newlocale|newlocale]] — создание нового объекта локали
- [[Языки программирования/C/Библиотеки/<locale.h>/uselocale|uselocale]] — установка локали для текущего потока

## Описание

Заголовочный файл `<locale.h>` определяет структуру `lconv`, которая должна включать как минимум следующие члены (см. определения `LC_MONETARY` в разделе 7.3.3 и `LC_NUMERIC` в разделе 7.3.4 стандарта POSIX.1-2017):

```c
char    *currency_symbol
char    *decimal_point
char     frac_digits
char    *grouping
char    *int_curr_symbol
char     int_frac_digits
char     int_n_cs_precedes
char     int_n_sep_by_space
char     int_n_sign_posn
char     int_p_cs_precedes
char     int_p_sep_by_space
char     int_p_sign_posn
char    *mon_decimal_point
char    *mon_grouping
char    *mon_thousands_sep
char    *negative_sign
char     n_cs_precedes
char     n_sep_by_space
char     n_sign_posn
char    *positive_sign
char     p_cs_precedes
char     p_sep_by_space
char     p_sign_posn
char    *thousands_sep
```

Заголовочный файл `<locale.h>` определяет `NULL` (как описано в `<stddef.h>`) и как минимум следующие макросы:

- `LC_ALL`
- `LC_COLLATE`
- `LC_CTYPE`
- `LC_MESSAGES`
- `LC_MONETARY`
- `LC_NUMERIC`
- `LC_TIME`

которые раскрываются в целочисленные константные выражения с различными значениями для использования в качестве первого аргумента функции `setlocale()`.

Дополнительные определения макросов, начинающиеся с символов `LC_` и прописной буквы, также могут быть определены реализацией.

Заголовочный файл `<locale.h>` должен содержать как минимум следующие макросы, представляющие битовые маски для использования с функцией `newlocale()` для каждой поддерживаемой категории локали: `LC_COLLATE_MASK`, `LC_CTYPE_MASK`, `LC_MESSAGES_MASK`, `LC_MONETARY_MASK`, `LC_NUMERIC_MASK`, `LC_TIME_MASK`.

Кроме того, должен быть определён макрос для установки битов всех категорий: `LC_ALL_MASK`.

Заголовочный файл `<locale.h>` определяет `LC_GLOBAL_LOCALE` — специальный дескриптор объекта локали, используемый функциями `duplocale()` и `uselocale()`.

Заголовочный файл `<locale.h>` определяет тип `locale_t`, представляющий объект локали.

### Типы

| Тип | Описание |
|---|---|
| `struct lconv` | Структура с параметрами форматирования числовых и денежных значений |
| `locale_t` | Тип объекта локали |

### Константы категорий локали

| Константа | Описание |
|---|---|
| `LC_ALL` | Все категории локали |
| `LC_COLLATE` | Правила колляции (сортировки строк) |
| `LC_CTYPE` | Классификация и преобразование символов |
| `LC_MESSAGES` | Категория сообщений (POSIX) |
| `LC_MONETARY` | Форматирование денежных значений |
| `LC_NUMERIC` | Форматирование числовых значений (десятичный разделитель, группировка) |
| `LC_TIME` | Форматирование даты и времени |
| `LC_GLOBAL_LOCALE` | Специальный дескриптор глобальной локали |
| `NULL` | Нулевой указатель |

### Маски для newlocale()

| Маска | Описание |
|---|---|
| `LC_COLLATE_MASK` | Маска категории `LC_COLLATE` |
| `LC_CTYPE_MASK` | Маска категории `LC_CTYPE` |
| `LC_MESSAGES_MASK` | Маска категории `LC_MESSAGES` |
| `LC_MONETARY_MASK` | Маска категории `LC_MONETARY` |
| `LC_NUMERIC_MASK` | Маска категории `LC_NUMERIC` |
| `LC_TIME_MASK` | Маска категории `LC_TIME` |
| `LC_ALL_MASK` | Маска всех категорий |

### Функции

```c
locale_t      duplocale(locale_t);
void          freelocale(locale_t);
struct lconv *localeconv(void);
locale_t      newlocale(int, const char *, locale_t);
char         *setlocale(int, const char *);
locale_t      uselocale(locale_t);
```

> [!NOTE]
> Константы `LC_*` не обязательно являются побитовыми масками — для установки нескольких категорий используйте `LC_ALL`.

> [!WARNING]
> Указатели, возвращённые `localeconv()`, могут стать невалидными после вызова `setlocale()`. Следует копировать нужные данные до следующего вызова `setlocale()`.

## Исключения

- **Установление `errno`:** функции `setlocale()`, `newlocale()`, `duplocale()` не устанавливают `errno` при успешном вызове. При ошибке они возвращают `NULL` (для `setlocale()` и `newlocale()`) или `0` (для `duplocale()`).
- **Поведение при передаче `NULL`:** `setlocale(LC_ALL, NULL)` возвращает текущую локаль без её изменения. `newlocale()` с нулевым вторым аргументом возвращает новый объект локали на основе текущего. `uselocale(NULL)` возвращает текущую локаль потока.
- **Поведение при переполнении/нехватке памяти:** `newlocale()` и `duplocale()` могут завершиться ошибкой при нехватке памяти — в этом случае они возвращают `NULL` и устанавливают `errno` в `ENOMEM`.
- **Граничные случаи:** `freelocale()` с нулевым аргументом — определено как безопасный вызов (ничего не делает). `setlocale()` с пустой строкой `""` определяет локаль по переменным окружения.
- **Многопоточность:** `setlocale()` является небезопасным для потоков (не MT-Safe) — его вызов в одном потоке влияет на все потоки. `uselocale()` устанавливает локаль только для текущего потока и является MT-Safe.
- **Потокобезопасность:** для многопоточных приложений используйте `uselocale()` вместо `setlocale()`.

## Стандарты

C89, POSIX.1-2008.

## История

C89. POSIX.1-2008 добавил `duplocale()`, `freelocale()`, `newlocale()`, `uselocale()`, `locale_t`, `LC_MESSAGES`, `LC_*_MASK`, `LC_GLOBAL_LOCALE`.

## Источники

- https://man7.org/linux/man-pages/man0/locale.h.0p.html
- `/usr/include/locale.h`
- ISO/IEC 9899:2024 (C23), раздел 7.11

## См. также

- `duplocale(3p)`, `freelocale(3p)`, `localeconv(3p)`, `newlocale(3p)`, `setlocale(3p)`, `uselocale(3p)`, `nl_langinfo(3p)`
