# <strings.h>

[[Языки программирования/C/Глава 10. Стандартная библиотека C|Глава 10. Стандартная библиотека C]] / <strings.h>

[[Языки программирования/C/Глава 10. Стандартная библиотека C/<string.h>|Назад]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C|Содержание]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<time.h>|Вперёд]]

**Дата написания:** 05.08.2026
**Дата обновления:** 18.08.2026

## Оглавление

### BSD и расширения

- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<strings.h>/bcmp|bcmp]] — сравнение N байт (устаревшая)
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<strings.h>/bcopy|bcopy]] — копирование N байт (устаревшая)
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<strings.h>/bzero|bzero]] — обнуление N байт (устаревшая)
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<strings.h>/ffs|ffs]] — позиция первого установленного бита
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<strings.h>/ffsl|ffsl]] — то же для `long`
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<strings.h>/ffsll|ffsll]] — то же для `long long`
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<strings.h>/index|index]] — первое вхождение символа (устаревшая)
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<strings.h>/rindex|rindex]] — последнее вхождение символа (устаревшая)
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<strings.h>/strcasecmp|strcasecmp]] — сравнение строк без учёта регистра
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<strings.h>/strcasecmp_l|strcasecmp_l]] — то же с явной локалью
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<strings.h>/strncasecmp|strncasecmp]] — сравнение не более N символов без учёта регистра
- [[Языки программирования/C/Глава 10. Стандартная библиотека C/<strings.h>/strncasecmp_l|strncasecmp_l]] — то же с явной локалью

## Описание библиотеки

Заголовочный файл `<strings.h>` — унаследованный интерфейс BSD, включённый в POSIX; в стандарт ISO C он не входит. Определяет функции, которых нет в стандартном `<string.h>`: регистронезависимое сравнение строк (`strcasecmp`, `strncasecmp` и их `_l`-варианты) и поиск первого установленного бита (`ffs`, `ffsl`, `ffsll`), а также устаревшие (LEGACY) функции `bcmp`, `bcopy`, `bzero`, `index`, `rindex`, заменяемые функциями `<string.h>`.

Файл доступен на Unix-подобных системах (Linux, macOS, BSD); в Windows его нет — аналогом `strcasecmp()` служит `_stricmp()` из `<string.h>`.

>[!WARNING]
>Названия `strings.h` (POSIX) и `string.h` (стандарт C) легко перепутать — при подключении обратите внимание на букву «s».

### Сравнение без учёта регистра

| Функция | Описание |
|---|---|
| `strcasecmp()` | Сравнение строк без учёта регистра в текущей локали |
| `strncasecmp()` | Сравнение не более `n` символов без учёта регистра |
| `strcasecmp_l()` | Сравнение без учёта регистра по правилам явной локали |
| `strncasecmp_l()` | Сравнение не более `n` символов по правилам явной локали |

### Устаревшие функции BSD

| Функция | Описание | Замена |
|---|---|---|
| `bcmp()` | Сравнение `n` байт | `memcmp()` |
| `bcopy()` | Копирование `n` байт (аргументы наоборот!) | `memmove()` / `memcpy()` |
| `bzero()` | Обнуление `n` байт | `memset()` |
| `index()` | Первое вхождение символа | `strchr()` |
| `rindex()` | Последнее вхождение символа | `strrchr()` |

### Битовые операции

| Функция | Описание |
|---|---|
| `ffs()` | Позиция первого установленного бита в `int` |
| `ffsl()` | То же для `long` |
| `ffsll()` | То же для `long long` |

## Исходный текст заголовочного файла

Приведён полный текст заголовочного файла `<strings.h>` из glibc (версия 2.40, 2024 год) — комментарии в нём описывают назначение каждой функции и условия её объявления.

```c
/* Copyright (C) 1991-2024 Free Software Foundation, Inc.
This file is part of the GNU C Library.
The GNU C Library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
The GNU C Library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public
License along with the GNU C Library; if not, see
<https://www.gnu.org/licenses/>. */

#ifndef _STRINGS_H
#define _STRINGS_H 1
#include <features.h>
#define __need_size_t
#include <stddef.h>
/* Tell the caller that we provide correct C++ prototypes. */

#if defined __cplusplus && __GNUC_PREREQ (4, 4)
# define __CORRECT_ISO_CPP_STRINGS_H_PROTO
#endif

__BEGIN_DECLS
#if defined __USE_MISC || !defined __USE_XOPEN2K8
/* Compare N bytes of S1 and S2 (same as memcmp). */

extern int bcmp (const void *__s1, const void *__s2, size_t __n)
__THROW __attribute_pure__ __nonnull ((1, 2));
/* Copy N bytes of SRC to DEST (like memmove, but args reversed). */

extern void bcopy (const void *__src, void *__dest, size_t __n)
__THROW __nonnull ((1, 2));
/* Set N bytes of S to 0. */

extern void bzero (void *__s, size_t __n) __THROW __nonnull ((1));
/* Find the first occurrence of C in S (same as strchr). */

# ifdef __CORRECT_ISO_CPP_STRINGS_H_PROTO
extern "C++"

{
extern char *index (char *__s, int __c)
__THROW __asm ("index") __attribute_pure__ __nonnull ((1));
extern const char *index (const char *__s, int __c)
__THROW __asm ("index") __attribute_pure__ __nonnull ((1));
# if defined __OPTIMIZE__
__extern_always_inline char *
index (char *__s, int __c) __THROW
{
return __builtin_index (__s, __c);
}

__extern_always_inline const char *
index (const char *__s, int __c) __THROW
{
return __builtin_index (__s, __c);
}

# endif
}

# else
extern char *index (const char *__s, int __c)
__THROW __attribute_pure__ __nonnull ((1));
# endif
/* Find the last occurrence of C in S (same as strrchr). */

# ifdef __CORRECT_ISO_CPP_STRINGS_H_PROTO
extern "C++"

{
extern char *rindex (char *__s, int __c)
__THROW __asm ("rindex") __attribute_pure__ __nonnull ((1));
extern const char *rindex (const char *__s, int __c)
__THROW __asm ("rindex") __attribute_pure__ __nonnull ((1));
# if defined __OPTIMIZE__
__extern_always_inline char *
rindex (char *__s, int __c) __THROW
{
return __builtin_rindex (__s, __c);
}

__extern_always_inline const char *
rindex (const char *__s, int __c) __THROW
{
return __builtin_rindex (__s, __c);
}

# endif
}

# else
extern char *rindex (const char *__s, int __c)
__THROW __attribute_pure__ __nonnull ((1));
# endif
#endif

#if defined __USE_MISC || !defined __USE_XOPEN2K8 || defined __USE_XOPEN2K8XSI
/* Return the position of the first bit set in I, or 0 if none are set.
The least-significant bit is position 1, the most-significant 32. */

extern int ffs (int __i) __THROW __attribute_const__;
#endif

/* The following two functions are non-standard but necessary for non-32 bit
platforms. */

# ifdef __USE_MISC
extern int ffsl (long int __l) __THROW __attribute_const__;
__extension__ extern int ffsll (long long int __ll)
__THROW __attribute_const__;
# endif
/* Compare S1 and S2, ignoring case. */

extern int strcasecmp (const char *__s1, const char *__s2)
__THROW __attribute_pure__ __nonnull ((1, 2));
/* Compare no more than N chars of S1 and S2, ignoring case. */

extern int strncasecmp (const char *__s1, const char *__s2, size_t __n)
__THROW __attribute_pure__ __nonnull ((1, 2));
#ifdef __USE_XOPEN2K8
/* POSIX.1-2008 extended locale interface (see locale.h). */

# include <bits/types/locale_t.h>
/* Compare S1 and S2, ignoring case, using collation rules from LOC. */

extern int strcasecmp_l (const char *__s1, const char *__s2, locale_t __loc)
__THROW __attribute_pure__ __nonnull ((1, 2, 3));
/* Compare no more than N chars of S1 and S2, ignoring case, using
collation rules from LOC. */

extern int strncasecmp_l (const char *__s1, const char *__s2,
size_t __n, locale_t __loc)
__THROW __attribute_pure__ __nonnull ((1, 2, 4));
#endif

__END_DECLS
#if __GNUC_PREREQ (3,4) && __USE_FORTIFY_LEVEL > 0 \
&& defined __fortify_function
/* Functions with security checks. */

# if defined __USE_MISC || !defined __USE_XOPEN2K8
# include <bits/strings_fortified.h>
# endif
#endif

#endif /* strings.h */
```

[[Языки программирования/C/Глава 10. Стандартная библиотека C/<string.h>|Назад]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C|Содержание]] | [[Языки программирования/C/Глава 10. Стандартная библиотека C/<time.h>|Вперёд]]
