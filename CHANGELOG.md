# Журнал изменений

Все важные изменения базы знаний фиксируются в этом файле. Записи группируются по датам (ДД.ММ.ГГГГ), новые — сверху. Изменения и добавления уроков внутри даты группируются по главам (заголовок `#### Глава N. ...`), при этом стандартные заголовки «Добавлено», «Изменено» и т. п. остаются на верхних уровнях (`###`). Подробное правило ведения — в разделе «Журнал изменений (CHANGELOG)» файла `AGENTS.md`.

## 05.09.2026

### Добавлено

#### Категория 1. Языковая поддержка (C++)

- 9 заголовков стандартной библиотеки C++ (категория «Языковая поддержка»): `<algorithm>`, `<any>`, `<atomic>`, `<barrier>`, `<bit>`, `<charconv>`, `<chrono>`, `<compare>`, `<concepts>` — оглавления, описания библиотек и документация по типам и функциям (157 файлов).
- `<algorithm>` (71 файл): сортировка (`sort`, `stable_sort`, `partial_sort`, `nth_element`), проверка отсортированности (`is_sorted`, `is_sorted_until`), бинарный поиск (`binary_search`, `lower_bound`, `upper_bound`, `equal_range`), множество (`merge`, `inplace_merge`, `set_union`, `set_intersection`, `set_difference`, `set_symmetric_difference`, `includes`), extremum (`min_element`, `max_element`, `minmax_element`, `clamp`), предикаты (`all_of`, `any_of`, `none_of`), поиск (`find`, `find_if`, `find_end`, `find_first_of`, `adjacent_find`, `search`, `search_n`), копирование (`copy`, `copy_if`, `copy_n`, `copy_backward`, `move`, `move_backward`), заполнение (`fill`, `fill_n`, `generate`, `generate_n`), удаление (`remove`, `remove_if`, `remove_copy`, `remove_copy_if`), замена (`replace`, `replace_if`, `replace_copy`, `replace_copy_if`), модификация (`reverse`, `reverse_copy`, `rotate`, `rotate_copy`, `shuffle`, `unique`, `unique_copy`), разбиение (`partition`, `partition_copy`, `is_partitioned`, `stable_partition`), обмен (`swap_ranges`, `iter_swap`), итераторы (`reverse_iterator`, `advance`, `distance`, `next`, `prev`).
- `<any>` (6 файлов, C++17): тип `any`, функции `any_cast`, `make_any`, `swap`, `reset`.
- `<atomic>` (14 файлов, C++11): типы `atomic`, `atomic_flag`, `atomic_bool`, `atomic_int`, `atomic_long`, `atomic_llong`, `atomic_uint`, `atomic_ulong`, `atomic_ullong`, перечисление `memory_order`, функции `atomic_thread_fence`, `atomic_signal_fence`, `kill_dependency`.
- `<barrier>` (5 файлов, C++20): тип `barrier`, `arrival_token`, функции `arrive_and_wait`, `arrive_and_drop`.
- `<bit>` (12 файлов, C++20): функции `bit_cast`, `bit_ceil`, `bit_floor`, `bit_width`, `countl_zero`, `countr_zero`, `popcount`, `has_single_bit`, `rotl`, `rotr`, перечисление `endian`.
- `<charconv>` (4 файла, C++17): функции `to_chars`, `from_chars`, перечисление `chars_format`.
- `<chrono>` (15 файлов, C++11): типы `duration`, `time_point`, часы `system_clock`, `steady_clock`, `high_resolution_clock`, функции `now`, `duration_cast`, `time_point_cast`, типы длительности `hours`, `minutes`, `seconds`, `milliseconds`, `microseconds`, `nanoseconds`.
- `<compare>` (13 файлов, C++20): типы `strong_ordering`, `weak_ordering`, `partial_ordering`, константы `strong_equal`, `weak_equal`, функциональный объект `compare_three_way`, операторы `operator==`, `operator<`, `operator>`, `operator<=`, `operator>=`, оператор `<=>`.
- `<concepts>` (17 файлов, C++20): концепты `same_as`, `derived_from`, `convertible_to`, `integral`, `floating_point`, `signed_integral`, `unsigned_integral`, `assignable_from`, `swappable`, `destructible`, `constructible_from`, `default_initializable`, `copy_initializable`, `move_initializable`, `equality_comparable`, `totally_ordered`.

#### Категория 3. Контейнеры (C++)

- 14 заголовков стандартной библиотеки C++ (категория «Контейнеры»): `<array>`, `<deque>`, `<flat_map>`, `<flat_set>`, `<forward_list>`, `<list>`, `<map>`, `<set>`, `<span>`, `<spanstream>`, `<stack>`, `<unordered_map>`, `<unordered_set>`, `<vector>` — оглавления, описания библиотек и документация по типам и методам (274 файла).
- `<array>` (23 файла): тип `array`, `tuple_size`, `tuple_element`, методы `at`, `operator[]`, `front`, `back`, `data`, `begin`/`end`/`rbegin`/`rend`/`cbegin`/`cend`/`crbegin`/`crend`, `empty`, `size`, `max_size`, `fill`, `swap`, свободная функция `get`.
- `<deque>` (30 файла): тип `deque`, методы `at`, `operator[]`, `front`, `back`, `data`, итераторы, `empty`, `size`, `max_size`, `resize`, `clear`, `insert`, `emplace`, `emplace_back`/`emplace_front`, `push_back`/`push_front`, `pop_back`/`pop_front`, `assign`, `swap`.
- `<flat_map>` (21 файл, C++23): тип `flat_map`, методы `at`, `operator[]`, `insert`, `emplace`, `try_emplace`, `insert_or_assign`, `count`, `find`, `contains`, `equal_range`, `lower_bound`, `upper_bound`, `erase`, `clear`, `merge`, `swap`, `keys`, `values`, `sorted_equal`.
- `<flat_set>` (16 файлов, C++23): тип `flat_set`, методы `insert`, `emplace`, `emplace_hint`, `count`, `find`, `contains`, `equal_range`, `lower_bound`, `upper_bound`, `erase`, `clear`, `merge`, `swap`, `sorted_equal`.
- `<forward_list>` (21 файл): тип `forward_list`, методы `insert_after`, `emplace_after`, `emplace_front`, `push_front`, `pop_front`, `front`, `before_begin`, `cbefore_begin`, `max_size`, `resize`, `clear`, `reverse`, `unique`, `sort`, `merge`, `splice_after`, `remove`, `remove_if`, `assign`.
- `<list>` (25 файлов): тип `list`, методы `insert`, `emplace`, `emplace_back`/`emplace_front`, `push_back`/`push_front`, `pop_back`/`pop_front`, `front`, `back`, `size`, `empty`, `max_size`, `resize`, `clear`, `swap`, `merge`, `splice`, `remove`, `remove_if`, `reverse`, `unique`, `sort`.
- `<map>` (21 файл): тип `map`, методы `at`, `operator[]`, `insert`, `emplace`, `emplace_hint`, `try_emplace`, `insert_or_assign`, `count`, `find`, `contains`, `equal_range`, `lower_bound`, `upper_bound`, `erase`, `clear`, `merge`, `swap`, `key_comp`, `value_comp`.
- `<set>` (17 файлов): тип `set`, методы `insert`, `emplace`, `emplace_hint`, `count`, `find`, `contains`, `equal_range`, `lower_bound`, `upper_bound`, `erase`, `clear`, `merge`, `swap`, `key_comp`, `value_comp`.
- `<span>` (13 файлов, C++20): тип `span`, методы `at`, `operator[]`, `front`, `back`, `data`, `size`, `size_bytes`, `empty`, `subspan`, `first`, `last`.
- `<spanstream>` (6 файлов, C++23): типы `spanstream`, `ispanstream`, `ospanstream`, `spanbuf`, `spanstreambuf`.
- `<stack>` (9 файлов): тип `stack`, методы `push`, `emplace`, `pop`, `top`, `size`, `empty`, `swap`.
- `<unordered_map>` (24 файла): тип `unordered_map`, методы `at`, `operator[]`, `insert`, `emplace`, `emplace_hint`, `try_emplace`, `insert_or_assign`, `count`, `find`, `contains`, `equal_range`, `bucket_count`, `bucket_size`, `load_factor`, `max_load_factor`, `rehash`, `reserve`, `erase`, `clear`, `merge`, `swap`, `hash_policy`.
- `<unordered_set>` (18 файлов): тип `unordered_set`, методы `insert`, `emplace`, `emplace_hint`, `count`, `find`, `contains`, `bucket_count`, `bucket_size`, `load_factor`, `max_load_factor`, `rehash`, `reserve`, `erase`, `clear`, `merge`, `swap`.
- `<vector>` (30 файлов): тип `vector`, методы `at`, `operator[]`, `front`, `back`, `data`, итераторы, `empty`, `size`, `max_size`, `reserve`, `capacity`, `shrink_to_fit`, `clear`, `insert`, `emplace`, `emplace_back`, `push_back`, `pop_back`, `resize`, `swap`, `assign`.

#### Категория 7. Поддержка языка (C++)

- 14 заголовков стандартной библиотеки C++ (категория «Поддержка языка»): `<exception>`, `<functional>`, `<initializer_list>`, `<limits>`, `<memory>`, `<new>`, `<numbers>`, `<numeric>`, `<optional>`, `<source_location>`, `<tuple>`, `<type_traits>`, `<typeindex>`, `<typeinfo>` — оглавления, описания библиотек и документация по типам и функциям (238 файлов).
- `<exception>` (13 файлов): типы `exception`, `bad_alloc`, `bad_exception`, `bad_cast`, `bad_typeid`, `bad_weak_ptr`, `nested_exception`, `exception_ptr`, `terminate_handler`, функции `current_exception`, `rethrow_exception`, `throw_with_nested`, `terminate`.
- `<functional>` (29 файлов): типы `function`, `hash`, функции `mem_fn`, `invoke`, `bind`, `bind_front` (C++20), `ref`, `cref`, `not_fn` (C++17), `not2`, объекты-операторы `plus`, `minus`, `multiplies`, `divides`, `modulus`, `negate`, `equal_to`, `not_equal_to`, `greater`, `less`, `greater_equal`, `less_equal`, `logical_and`, `logical_or`, `logical_not`, `bit_and`, `bit_or`, `bit_xor`, `bit_not`.
- `<initializer_list>` (3 файла): тип `initializer_list`, функции `begin`, `end`.
- `<limits>` (26 файлов): типы `numeric_limits`, `float_round_style`, `float_denorm_style`, свойства `max_exponent`, `max_exponent10`, `min_exponent`, `min_exponent10`, `radix`, `epsilon`, `round_error`, `denorm_min`, `quiet_NaN`, `signaling_NaN`, `infinity`, `is_specialized`, `is_exact`, `is_integer`, `is_signed`, `is_bounded`, `is_modulo`, `digits`, `digits10`, `max_digits10`, `min`, `lowest`, `max`.
- `<memory>` (20 файлов): типы `unique_ptr`, `shared_ptr`, `weak_ptr`, `owner_less`, `enable_shared_from_this`, `pointer_traits`, `allocator_traits`, `allocator`, `uses_allocator`, `scoped_allocator_adaptor`, `raw_storage_iterator`, функции `make_unique`, `make_shared`, `allocate_shared`, `uninitialized_default_construct`, `uninitialized_value_construct`, `uninitialized_copy`, `uninitialized_fill`, `destroy`, `temporary_buffer`.
- `<new>` (9 файлов): типы `bad_alloc`, `bad_array_new_length`, `nothrow`, `new_handler`, функции `operator_new`, `operator_delete`, `set_new_handler`, константы `hardware_constructive_interference_size`, `hardware_destructive_interference_size`.
- `<numbers>` (12 файлов, C++20): константы `e`, `log2e`, `log10e`, `pi`, `inv_pi`, `ln2`, `ln10`, `sqrt2`, `sqrt3`, `inv_sqrt3`, `egamma`, `phi`.
- `<numeric>` (14 файлов): функции `iota`, `accumulate`, `inner_product`, `adjacent_difference`, `partial_sum`, `reduce` (C++17), `inclusive_scan` (C++17), `exclusive_scan` (C++17), `transform_inclusive_scan` (C++17), `transform_exclusive_scan` (C++17), `gcd` (C++17), `lcm` (C++17), `midpoint` (C++20), `lerp` (C++20).
- `<optional>` (12 файлов, C++17): типы `optional`, `nullopt`, `nullopt_t`, `bad_optional_access`, функции `make_optional`, `has_value`, `value`, `value_or`, `operator_bool`, `reset`, `emplace`, `swap`.
- `<source_location>` (2 файла, C++20): тип `source_location`, функция `current`.
- `<tuple>` (16 файлов): типы `tuple`, `tuple_size`, `tuple_element`, функции `make_tuple`, `forward_as_tuple`, `tuple_cat`, `get`, `swap`, `operator==`, `operator!=`, `operator<`, `operator>`, `operator<=`, `operator>=`, `tie`, `apply`.
- `<type_traits>` (54 файла): метатипы проверки `is_same`, `is_integral`, `is_floating_point`, `is_array`, `is_class`, `is_enum`, `is_function`, `is_pointer`, `is_reference`, `is_const`, `is_volatile`, `is_signed`, `is_unsigned`, `is_void`, `is_null_pointer`, `is_bounded_array`, `is_unbounded_array`, трансформации `remove_const`, `remove_volatile`, `remove_cv`, `remove_reference`, `remove_cvref`, `add_const`, `add_volatile`, `add_cv`, `add_lvalue_reference`, `add_rvalue_reference`, `add_pointer`, `decay`, метатипы `enable_if`, `conditional`, `common_type`, `underlying_type`, `is_convertible`, `is_nothrow_constructible`, `is_trivially_copyable`, `is_standard_layout`, `is_pod`, `is_literal_type`, `is_empty`, `is_polymorphic`, `is_abstract`, `is_final`, `is_aggregate`, `alignment_of`, `rank`, `extent`, `is_invocable`, `is_nothrow_invocable`, `invoke_result`, `conjunction`, `disjunction`, `negation`, `is_constant_evaluated`.
- `<typeindex>` (8 файлов): тип `type_index`, функции `hash`, `operator==`, `operator!=`, `operator<`, `operator<=`, `operator>`, `operator>=`.
- `<typeinfo>` (6 файлов): типы `type_info`, `bad_cast`, `bad_typeid`, функции `hash_code`, `name`, `before`.

#### Глава 1. Основы GTK

- 6 статей главы 1 раздела «Руководство по GTK» — копии статей с сайта metanit.com: «Введение в GTK» (1.1.php), «Создание окон и GtkWindow» (1.2.php), «Настройка окна приложения» (1.3.php), «GtkApplication» (1.4.php), «Создание графического интерфейса в приложении» (1.5.php), «Введение в виджеты» (2.1.php).

#### Глава 1. SQLite

- 5 статей главы 1 раздела «Базы данных» — копии статей с сайта metanit.com: «Подключение к SQLite» (1.1.php), «Выполнение кода SQL. Функция sqlite3_exec» (1.2.php), «Добавление, обновление, удаление данных в SQLite» (1.3.php), «Получение данных из базы данных SQLite» (1.4.php), «Параметризация запросов к БД SQLite» (1.5.php).

#### Глава 1. Хеш таблицы

- 12 статей главы 1 раздела «Хеш таблицы» — копии статей с сайта metanit.com: «Введение в хеш-таблицы» (1.1.php), «Хеш-функция» (1.2.php), «Определение хеш-таблицы» (1.3.php), «Размер хеш-таблицы» (1.4.php), «Операции с хеш-таблицами» (1.5.php), «Коллизии. Стратегия цепочки и связанных списков» (1.6.php), «Коллизии. Стратегия открытой адресации» (1.7.php), «Расширение хеш-таблиц для стратегии цепочки» (1.8.php), «Расширение хеш-таблицы при открытой адресации» (1.9.php), «Изменение размера таблицы, когда размеры не являются степенями двойки» (1.10.php), «Универсальные хеш-таблицы на основе макросов» (1.11.php), «Универсальные хеш-таблицы на основе функций» (1.12.php).

#### Глава 4. Модули, API и управление состоянием

- 4 статьи главы 4 раздела «Организация программ» — копии статей с сайта metanit.com: «Параметры командной строки» (4.7.php), «Директива #include. Включение файлов» (3.1.php), «Директива #define» (3.2.php), «Макросы» (3.3.php).

## 04.09.2026

### Добавлено

#### Глава 1. Управление ресурсами и обработка ошибок

- 6 статей главы 1 раздела «Организация программ» — копии статей с сайта metanit.com: «Рекурсивные функции» (4.4.php), «Область видимости переменных» (4.5.php), «Внешние объекты» (4.6.php), «Классы хранения (Storage class)» (4.8.php), «Функции как параметры других функций» (5.12.php), «Функция как результат другой функции» (5.16.php).

#### Глава 3. Возвращение результата из функции

- 5 статей главы 3 раздела «Организация программ» — копии статей с сайта metanit.com: «Результат функции» (4.3.php), «Параметры функции» (4.2.php), «Указатели на функции» (5.11.php), «Тип функции» (5.15.php), «Функции с переменным количеством параметров» (5.13.php).

### Изменено

#### Глава 7. Динамическая память

- Обновить содержание 5 статей главы 7 копиями статей с сайта metanit.com: «Выделение и освобождение памяти» (5.8.php), «Выделение памяти для двухмерного массива произвольной длины» (5.14.php), «Управление динамической памятью» (5.10.php), «Указатель как результат функции» (5.9.php), «Организация памяти программы и структура сегментов» (5.18.php).

## 30.08.2026

### Изменено

#### Глава 10. Стандартная библиотека C

- Добавить раздел «Обработка ошибок» в статьи о функциях библиотек `<wchar.h>`, `<wctype.h>`, `<strings.h>` (71 файл). Информация включает: поведение при NULL, установление errno, многопоточность, связанные функции.
- Добавить раздел «Обработка ошибок» в статьи о функциях библиотек `<time.h>` (13 файлов), `<locale.h>` (2 файла), `<signal.h>` (2 файла). Информация включает: поведение при NULL, установление errno, возвращаемые значения при ошибке, многопоточность, связанные функции.

## 29.08.2026

### Изменено

#### Глава 10. Стандартная библиотека C

- Добавить раздел «Обработка ошибок» в 46 статей о функциях `<stdio.h>`: sscanf, fgetpos, scanf, fprintf, fgets, fsetpos, ungetc, putchar, tmpfile, gets, fflush, fputs, vscanf, fclose, getchar, printf, vsnprintf, vprintf, vfscanf, fopen, setvbuf, fread, clearerr, ferror, rename, fwrite, ftell, puts, putc, snprintf, fputc, rewind, setbuf, fscanf, remove, vsprintf, fseek, tmpnam, getc, vfprintf, perror, freopen, feof, fgetc, vsscanf, sprintf. Информация включает: поведение при NULL, установление errno, многопоточность.

### Изменено

#### Глава 10. Стандартная библиотека C

- Переименовать раздел «Библиотеки» в «Глава 10. Стандартная библиотека C» для выравнивания нумерации глав (после Главы 9 идёт Глава 10).

### Добавлено

#### Глава 10. Стандартная библиотека C

- Статья «<setjmp.h>» (оглавление по категориям и описание библиотеки) и документация по типу и макросам `<setjmp.h>` (3 файла в `<setjmp.h>/`): jmp_buf, setjmp, longjmp.
- Статья «<signal.h>» (оглавление по категориям и описание библиотеки) и документация по типу, константам и функциям `<signal.h>` (12 файлов в `<signal.h>/`): sig_atomic_t, SIG_DFL, SIG_ERR, SIG_IGN, SIGABRT, SIGFPE, SIGILL, SIGINT, SIGSEGV, SIGTERM, raise, signal.
- Статья «<stdatomic.h>» (оглавление по категориям и описание библиотеки) и документация по типу, константам, функциям и барьерам памяти `<stdatomic.h>` (13 файлов в `<stdatomic.h>/`): atomic_flag, ATOMIC_FLAG_INIT, ATOMIC_VAR_INIT, atomic_init, atomic_store, atomic_load, atomic_exchange, atomic_compare_exchange, atomic_fetch_add, atomic_fetch_sub, atomic_thread_fence, atomic_signal_fence, kill_dependency.
- Статья «<stdbit.h>» (оглавление по категориям и описание библиотеки, C23) и документация по функциям битовых операций `<stdbit.h>` (15 файлов в `<stdbit.h>/`): stdc_leading_zeros, stdc_leading_ones, stdc_trailing_zeros, stdc_trailing_ones, stdc_first_leading_zero, stdc_first_leading_one, stdc_first_trailing_zero, stdc_first_trailing_one, stdc_count_zeros, stdc_count_ones, stdc_has_single_bit, stdc_bit_ceil, stdc_bit_floor, stdc_bit_width, stdc_popcount.

## 20.08.2026

### Добавлено

#### Глава 10. Стандартная библиотека C

- Статья «<fenv.h>» (оглавление по категориям и описание библиотеки) и документация по типам, константам и функциям `<fenv.h>` (24 файла в `<fenv.h>/`): fenv_t, fexcept_t, FE_DIVBYZERO, FE_INEXACT, FE_INVALID, FE_OVERFLOW, FE_UNDERFLOW, FE_ALL_EXCEPT, FE_DOWNWARD, FE_TONEAREST, FE_TOWARDZERO, FE_UPWARD, FE_DFL_ENV, feclearexcept, fegetexceptflag, feraiseexcept, fesetexceptflag, fetestexcept, fegetround, fesetround, fegetenv, feholdexcept, fesetenv, feupdateenv.
- Статья «<wchar.h>» (оглавление по категориям и описание библиотеки) и документация по типам, константам и функциям `<wchar.h>` (57 файлов в `<wchar.h>/`): wchar_t, wint_t, mbstate_t, WEOF, wcscat, wcschr, wcscmp, wcscoll, wcscpy, wcscspn, wcslen, wcsncat, wcsncmp, wcsncpy, wcspbrk, wcsrchr, wcsspn, wcsstr, wcswcs, wcsxfrm, wcstod, wcstof, wcstold, wcstol, wcstoll, wcstoul, wcstoull, btowc, wctob, mbsinit, mbrlen, mbrtowc, mbsrtowcs, wcrtomb, wcsrtombs, iswalnum, iswalpha, iswblank, iswcntrl, iswdigit, iswgraph, iswlower, iswprint, iswpunct, iswspace, iswupper, iswxdigit, towlower, towupper, towctrans, wctrans, wctype, wmemcpy, wmemmove, wmemset, wmemcmp, wmemchr.
- Статья «<wctype.h>» (оглавление по категориям и описание библиотеки) и документация по типам, функциям классификации и преобразованиям `<wctype.h>` (19 файлов в `<wctype.h>/`): wctrans_t, wctype_t, iswalnum, iswalpha, iswblank, iswcntrl, iswdigit, iswgraph, iswlower, iswprint, iswpunct, iswspace, iswupper, iswxdigit, iswctype, wctype, towctrans, towlower, towupper.
- Статья «<uchar.h>» (оглавление по категориям и описание библиотеки) и документация по типам и функциям преобразования `<uchar.h>` (6 файлов в `<uchar.h>/`): char16_t, char32_t, mbrtoc16, mbrtoc32, c16rtomb, c32rtomb.
- Статья «<complex.h>» (оглавление по категориям и описание библиотеки) и документация по макросам и функциям `<complex.h>` (23 файла в `<complex.h>/`): Complex, _Complex_I, I, cabs, cacos, cacosh, carg, casin, casinh, catan, catanh, ccos, ccosh, cexp, cimag, clog, conj, cpow, cproj, creal, csin, csinh, csqrt, ctan, ctanh.
- Статья «<inttypes.h>» (оглавление по категориям и описание библиотеки) и документация по типу, макросам и функциям `<inttypes.h>` (62 файла в `<inttypes.h>/`): imaxdiv_t, PRId8, PRId16, PRId32, PRId64, PRIdMAX, PRIi8, PRIi16, PRIi32, PRIi64, PRIiMAX, PRIo8, PRIo16, PRIo32, PRIo64, PRIoMAX, PRIu8, PRIu16, PRIu32, PRIu64, PRIuMAX, PRIx8, PRIx16, PRIx32, PRIx64, PRIxMAX, PRIX8, PRIX16, PRIX32, PRIX64, PRIXMAX, SCNd8, SCNd16, SCNd32, SCNd64, SCNdMAX, SCNi8, SCNi16, SCNi32, SCNi64, SCNiMAX, SCNo8, SCNo16, SCNo32, SCNo64, SCNoMAX, SCNu8, SCNu16, SCNu32, SCNu64, SCNuMAX, SCNx8, SCNx16, SCNx32, SCNx64, SCNxMAX, imaxabs, imaxdiv, strtoimax, strtoumax, wcstoimax, wcstoumax.
- Статья «<locale.h>» (оглавление по категориям и описание библиотеки) и документация по типу, константам и функциям `<locale.h>` (10 файлов в `<locale.h>/`): struct lconv, LC_ALL, LC_COLLATE, LC_CTYPE, LC_MONETARY, LC_NUMERIC, LC_TIME, NULL, localeconv, setlocale.
- Статья «<stdint.h>» (оглавление по категориям и описание библиотеки) и документация по типам, лимитам и макросам литералов `<stdint.h>` (89 файлов в `<stdint.h>/`): int8_t, int16_t, int32_t, int64_t, int_fast8_t, int_fast16_t, int_fast32_t, int_fast64_t, int_least8_t, int_least16_t, int_least32_t, int_least64_t, intmax_t, intptr_t, uint8_t, uint16_t, uint32_t, uint64_t, uint_fast8_t, uint_fast16_t, uint_fast32_t, uint_fast64_t, uint_least8_t, uint_least16_t, uint_least32_t, uint_least64_t, uintmax_t, uintptr_t, INT8_MIN, INT8_MAX, UINT8_MAX, INT16_MIN, INT16_MAX, UINT16_MAX, INT32_MIN, INT32_MAX, UINT32_MAX, INT64_MIN, INT64_MAX, UINT64_MAX, INTMAX_MIN, INTMAX_MAX, UINTMAX_MAX, INTPTR_MIN, INTPTR_MAX, UINTPTR_MAX, INT_FAST8_MIN, INT_FAST8_MAX, UINT_FAST8_MAX, INT_FAST16_MIN, INT_FAST16_MAX, UINT_FAST16_MAX, INT_FAST32_MIN, INT_FAST32_MAX, UINT_FAST32_MAX, INT_FAST64_MIN, INT_FAST64_MAX, UINT_FAST64_MAX, INT_LEAST8_MIN, INT_LEAST8_MAX, UINT_LEAST8_MAX, INT_LEAST16_MIN, INT_LEAST16_MAX, UINT_LEAST16_MAX, INT_LEAST32_MIN, INT_LEAST32_MAX, UINT_LEAST32_MAX, INT_LEAST64_MIN, INT_LEAST64_MAX, UINT_LEAST64_MAX, SIZE_MAX, PTRDIFF_MIN, PTRDIFF_MAX, SIG_ATOMIC_MIN, SIG_ATOMIC_MAX, WCHAR_MIN, WCHAR_MAX, WINT_MIN, WINT_MAX, INT8_C, INT16_C, INT32_C, INT64_C, INTMAX_C, UINT8_C, UINT16_C, UINT32_C, UINT64_C, UINTMAX_C.
- Статья «<stdio.h>» (оглавление по категориям и описание библиотеки) и документация по типам, константам, потокам и функциям `<stdio.h>` (64 файла в `<stdio.h>/`): FILE, fpos_t, NULL, BUFSIZ, EOF, FILENAME_MAX, FOPEN_MAX, L_tmpnam, SEEK_CUR, SEEK_END, SEEK_SET, TMP_MAX, _IOFBF, _IOLBF, _IONBF, stderr, stdin, stdout, remove, rename, tmpfile, tmpnam, fclose, fflush, fopen, freopen, setbuf, setvbuf, fprintf, fscanf, printf, scanf, snprintf, sprintf, sscanf, vfprintf, vfscanf, vprintf, vscanf, vsnprintf, vsprintf, vsscanf, fgetc, fgets, fputc, fputs, getc, getchar, gets, putc, putchar, puts, ungetc, fread, fwrite, fgetpos, fseek, fsetpos, ftell, rewind, clearerr, feof, ferror, perror.
- Статья «<tgmath.h>» (оглавление по категориям и описание библиотеки) и документация по обобщённым математическим макросам `<tgmath.h>` (43 файла в `<tgmath.h>/`): tgacos, tgasin, tgatan, tgatan2, tgcos, tgsin, tgtan, tgcosh, tgsinh, tgtanh, tgacosh, tgasinh, tgatanh, tgexp, tgexp2, tgexpm1, tglog, tglog10, tglog1p, tglog2, tgcbrt, tgsqrt, tgpow, tghypot, tgceil, tgfloor, tgnearbyint, tground, tgtrunc, tgfdim, tgfmax, tgfmin, tgfma, tgfrexp, tgldexp, tgmodf, tgscalbn, tgabs, tgcarg, tgcimag, tgconj, tgcreal, tgcproj.
- Статья «<threads.h>» (оглавление по категориям и описание библиотеки) и документация по типам, константам и функциям потоков `<threads.h>` (35 файлов в `<threads.h>/`): thrd_t, mtx_t, tss_t, once_flag, tss_dtor_t, thrd_start_t, mtx_plain, mtx_recursive, mtx_timed, thrd_success, thrd_nomem, thrd_error, thrd_busy, thrd_timedout, TSS_DTOR_ITERATIONS, ONCE_FLAG_INIT, MTX_INIT, thrd_create, thrd_current, thrd_detach, thrd_equal, thrd_exit, thrd_join, thrd_sleep, thrd_yield, mtx_init, mtx_lock, mtx_trylock, mtx_timedlock, mtx_unlock, mtx_destroy, tss_create, tss_delete, tss_get, tss_set, call_once.

## 18.08.2026

### Добавлено

#### Глава 9. Стандартная библиотека C

- Документация по кодам ошибок `<errno.h>` (135 файлов в `13. <errno.h>/`): errno, EDOM, EILSEQ, ERANGE и все коды POSIX/glibc (E2BIG, EACCES, EADDRINUSE, EADDRNOTAVAIL, EADV, EAFNOSUPPORT, EAGAIN, EALREADY, EBADE, EBADF, EBADFD, EBADMSG, EBADR, EBADRQC, EBADSLT, EBFONT, EBUSY, ECANCELED, ECHILD, ECHRNG, ECOMM, ECONNABORTED, ECONNREFUSED, ECONNRESET, EDEADLK, EDEADLOCK, EDESTADDRREQ, EDOM, EDOTDOT, EDQUOT, EEXIST, EFAULT, EFBIG, EHOSTDOWN, EHOSTUNREACH, EHWPOISON, EIDRM, EILSEQ, EINPROGRESS, EINTR, EINVAL, EIO, EISCONN, EISDIR, EISNAM, EKEYEXPIRED, EKEYREJECTED, EKEYREVOKED, EL2HLT, EL2NSYNC, EL3HLT, EL3RST, ELIBACC, ELIBBAD, ELIBEXEC, ELIBMAX, ELIBSCN, ELNRNG, ELOOP, EMEDIUMTYPE, EMFILE, EMLINK, EMSGSIZE, EMULTIHOP, ENAMETOOLONG, ENAVAIL, ENETDOWN, ENETRESET, ENETUNREACH, ENFILE, ENOANO, ENOBUFS, ENOCSI, ENODATA, ENODEV, ENOENT, ENOEXEC, ENOKEY, ENOLCK, ENOLINK, ENOMEDIUM, ENOMEM, ENOMSG, ENONET, ENOPKG, ENOPROTOOPT, ENOSPC, ENOSR, ENOSTR, ENOSYS, ENOTBLK, ENOTCONN, ENOTDIR, ENOTEMPTY, ENOTNAM, ENOTRECOVERABLE, ENOTSOCK, ENOTSUP, ENOTTY, ENOTUNIQ, ENXIO, EOPNOTSUPP, EOVERFLOW, EOWNERDEAD, EPERM, EPFNOSUPPORT, EPIPE, EPROTO, EPROTONOSUPPORT, EPROTOTYPE, ERANGE, EREMCHG, EREMOTE, EREMOTEIO, ERESTART, ERFKILL, EROFS, ESHUTDOWN, ESOCKTNOSUPPORT, ESPIPE, ESRCH, ESRMNT, ESTALE, ESTRPIPE, ETIME, ETIMEDOUT, ETOOMANYREFS, ETXTBSY, EUCLEAN, EUNATCH, EUSERS, EWOULDBLOCK, EXDEV, EXFULL, errno.
- Документация по функциям `<string.h>` (25 файлов в `12. <string.h>/`): memchr, memcmp, memcpy, memmove, memset, strcat, strchr, strcmp, strcoll, strcpy, strcspn, strdup, strerror, strlen, strncat, strncmp, strncpy, strndup, strnlen, strpbrk, strrchr, strspn, strstr, strtok, strxfrm.
- Документация по функциям `<stdlib.h>` (49 файлов в `11. <stdlib.h>/`): _Exit, EXIT_FAILURE, EXIT_SUCCESS, MB_CUR_MAX, RAND_MAX, abort, abs, aligned_alloc, at_quick_exit, atexit, atof, atoi, atol, atoll, bsearch, calloc, div, div_t, exit, free, getenv, labs, ldiv, ldiv_t, llabs, lldiv, lldiv_t, malloc, mblen, mbstowcs, mbtowc, quick_exit, qsort, rand, realloc, srand, strfromd, strfromf, strfroml, strtod, strtof, strtol, strtold, strtoll, strtoul, strtoull, system, wcstombs, wctomb.
- Статья «14. <stddef.h>» (оглавление и описание библиотеки) и документация по определениям `<stddef.h>` (8 файлов в `14. <stddef.h>/`): NULL, max_align_t, nullptr_t, offsetof, ptrdiff_t, size_t, unreachable, wchar_t.

#### Глава 10. POSIX

- Статья «<stdlib.h>» (оглавление по категориям и описание библиотеки) и документация по POSIX/GNU-функциям `<stdlib.h>` (23 файла в `<stdlib.h>/`): a64l, clearenv, drand48, ecvt, getloadavg, getpt, getsubopt, grantpt, mkdtemp, mkstemp, mktemp, posix_memalign, posix_openpt, ptsname, putenv, qsort_r, random, reallocarray, secure_getenv, setenv, strtod_l, strtol_l, unlockpt.
- Статья «<string.h>» (оглавление и описание библиотеки) и документация по POSIX/GNU-функциям `<string.h>` (27 файлов в `<string.h>/`): basename, explicit_bzero, memccpy, memfrob, memmem, mempcpy, memrchr, rawmemchr, stpcpy, stpncpy, strcasestr, strchrnul, strcoll_l, strerrordesc_np, strerror_l, strerror_r, strerror_s, strerrorname_np, strfry, strlcat, strlcpy, strsep, strsignal, strtok_r, strtok_s, strverscmp, strxfrm_l.
- Документация по функциям `<strings.h>` (12 файлов в `<strings.h>/`): bcmp, bcopy, bzero, ffs, ffsl, ffsll, index, rindex, strcasecmp, strcasecmp_l, strncasecmp, strncasecmp_l.

#### Глава 10. Стандартная библиотека C

- Статья «<ctype.h>» (оглавление по категориям и описание библиотеки) и документация по функциям и макросам `<ctype.h>` (32 файла в `<ctype.h>/`): _tolower, _toupper, isalnum, isalnum_l, isalpha, isalpha_l, isascii, isblank, isblank_l, iscntrl, iscntrl_l, isdigit, isdigit_l, isgraph, isgraph_l, islower, islower_l, isprint, isprint_l, ispunct, ispunct_l, isspace, isspace_l, isupper, isupper_l, isxdigit, isxdigit_l, toascii, tolower, tolower_l, toupper, toupper_l.
  - Документация по новым заголовочным файлам стандартной библиотеки C: `<limits.h>`, `<float.h>`, `<assert.h>`, `<stdarg.h>`, `<stdbool.h>`, `<stdalign.h>`, `<iso646.h>`, `<stdckdint.h>` (всего 105 статей функций и макросов).
- Статья «<math.h>» (оглавление и описание библиотеки) и документация по функциям и макросам `<math.h>` (76 файлов в `<math.h>/`): M_1_PI, M_2_PI, M_2_SQRTPI, M_E, M_LN10, M_LN2, M_LOG10E, M_LOG2E, M_PI, M_PI_2, M_PI_4, M_SQRT1_2, M_SQRT2, HUGE_VAL, HUGE_VALF, HUGE_VALL, INFINITY, NAN, acos, acosh, asin, asinh, atan, atan2, atanh, cbrt, ceil, cos, cosh, exp, exp2, expm1, fabs, fdim, floor, fmax, fmin, fmod, fpclassify, frexp, hypot, isfinite, isinf, isnan, isnormal, isgreater, isgreaterequal, isless, islessequal, islessgreater, isunordered, ldexp, llrint, llround, lrint, lround, log, log10, log1p, log2, logb, modf, nearbyint, pow, remainder, remquo, rint, round, scalbn, scalbln, sin, sinh, sqrt, tan, tanh, trunc.
- Статья «<time.h>» (оглавление и описание библиотеки) и документация по типам, константам и функциям `<time.h>` (19 файлов в `<time.h>/`): clock_t, struct tm, time_t, struct timespec, CLOCKS_PER_SEC, TIME_UTC, asctime, clock, clock_gettime, ctime, difftime, mktime, strftime, time, timespec_get, getdate, strptime, timelocal, tzset.

### Изменено

#### Глава 9. Стандартная библиотека C

- Урок 11 «<stdlib.h>»: статья переработана — вместо развёрнутых разделов теперь оглавление со ссылками на файлы функций и краткое описание библиотеки со сводными таблицами по категориям (преобразование строк в числа и обратно, управление памятью, сортировка и поиск, завершение программы, целочисленная математика, случайные числа, окружение, многобайтовые символы); дата обновления — 18.08.2026.
- Статья «14. <stddef.h>»: удалён раздел «Исходный текст заголовочного файла».
- Урок 12 «<string.h>»: статья переработана — вместо развёрнутых разделов теперь оглавление (два списка: ISO C и POSIX/расширения) и краткое описание библиотеки со сводными таблицами по категориям (копирование, сравнение, поиск, разбиение/длина, ошибки).
- Урок 12 «<string.h>»: примечание о POSIX-функциях обновлено — вместо заготовки ссылка на новую статью «<string.h>» главы 10.
- Урок 11 «<stdlib.h>»: добавлено примечание о POSIX/GNU-функциях со ссылкой на статью «<stdlib.h>» главы 10.
- Статья «13. <errno.h>»: переработана — вместо сырого исходного текста glibc теперь оглавление со ссылками на файлы кодов ошибок (по категориям: стандарт C, доступ и права, файлы и ФС, процессы и сигналы, память и значения, IPC, сети и сокеты, терминалы и устройства, ключи, библиотеки, исторические коды) и описание библиотеки со сводными таблицами и реализацией `errno` в glibc.
- Обновлены навигация и индексы: в «13. <errno.h>» ссылка «Вперёд» → «14. <stddef.h>», в «<strings.h>» (глава 10) ссылка «Назад» → «14. <stddef.h>», статьи добавлены в оглавления «Глава 9. Стандартная библиотека C.md» и «C.md».

#### Глава 10. POSIX

- Обновлены навигация и индексы: статья «<stdlib.h>» (ссылка «Назад» → «14. <stddef.h>»), «<string.h>» (ссылка «Назад» → «<stdlib.h>»), «<strings.h>» (ссылка «Вперёд» → «1. Создание потоков»), «Глава 10. POSIX.md» (статья «<stdlib.h>» в оглавлении перед «<string.h>»); в «1. Создание потоков» (глава 11) ссылка «Назад» → «<strings.h>», в «14. <stddef.h>» (глава 9) ссылка «Вперёд» → «<stdlib.h>».
- Статьи и папки главы переименованы — убрана нумерация: «1. <strings.h>.md» → «<strings.h>.md», «2. <string.h>.md» → «<string.h>.md», «2. <string.h>/» → «<string.h>/»; обновлены все ссылки (индексы, навигация, хлебные крошки, примечание в главе 9).
- Статья «<strings.h>» переработана под структуру «<string.h>»: вместо развёрнутого урока оглавление со ссылками на файлы функций и краткое описание библиотеки со сводными таблицами (сравнение без учёта регистра, устаревшие функции BSD с заменами, битовые операции); добавлен полный исходный текст заголовочного файла glibc в разделе «Исходный текст заголовочного файла»; дата обновления — 18.08.2026.

#### Глава 10. Стандартная библиотека C

- Глава 10. POSIX заменена новой главой «Библиотеки»: в неё перенесены статьи о заголовочных файлах из главы 9 (11. `<stdlib.h>`, 12. `<string.h>`, 13. `<errno.h>`, 14. `<stddef.h>`) и главы 10 (`<stdlib.h>`, `<string.h>`, `<strings.h>`); глава 9 оставлена с уроками 1–10.
- Статьи с одинаковыми именами объединены: «<stdlib.h>» (разделы «Стандарт C» и «Расширения POSIX и GNU»; 72 статьи функций в `<stdlib.h>/`) и «<string.h>» (те же разделы; 52 статьи функций в `<string.h>/`).
- Убрана нумерация файлов, глава отсортирована по алфавиту: `<ctype.h>`, `<errno.h>`, `<stddef.h>`, `<stdlib.h>`, `<string.h>`, `<strings.h>`.
- Обновлены навигация (главы 9 → Библиотеки → глава 11), хлебные крошки и вики-ссылки во всех статьях, индексы «Библиотеки.md», «Глава 9. Стандартная библиотека C.md», «C.md»; старые статьи-оглавления «11. <stdlib.h>» и «12. <string.h>» главы 9 удалены.
- Обновлена навигация после добавления «<ctype.h>» первой статьёй главы: в «10. Проверка символов и ctype.h» ссылка «Вперёд» ведёт на «<ctype.h>», в «<errno.h>» «Назад» — на «<ctype.h>», в `E2BIG` «Назад» — на `toupper_l`; обновлён блок «Библиотеки» в «C.md» и описание главы в «Библиотеки.md».

#### Глава 9. Стандартная библиотека C

- Урок 10 «Проверка символов и ctype.h»: в конце добавлена ссылка на статью «<ctype.h>» главы «Библиотеки» (полный справочник по функциям, включая расширения POSIX и GNU); ссылка «Вперёд» теперь ведёт на «<ctype.h>» вместо «<errno.h>».

## 13.08.2026

### Изменено

#### Глава 9. Стандартная библиотека C

- Урок 12 «<string.h>»: раздел 2 «Копирование строк и блоков памяти» значительно расширен — поведение `memcpy`/`memmove` (`restrict`, скорость, type punning с примером переинтерпретации `float`), таблица сравнения `strcpy`/`strncpy` и пример поля фиксированной длины, безопасный паттерн `strncat` (свободное место вместо `sizeof`) и предупреждение о классической ошибке с `n`, примечание о квадратичном времени построения строк в цикле, дополнения в `strdup`/`strndup` (эквивалент `malloc` + копирование, `strndup(s, 0)`, `errno = ENOMEM` в POSIX).
- Урок 12 «<string.h>»: раздел 3 «Сравнение строк и памяти» расширен — подробное поведение `memcmp`/`strcmp`/`strncmp`, предупреждение о сравнении структур через `memcmp` (padding), сравнительная таблица с `strcoll`.
- Урок 12 «<string.h>»: раздел 6 «Разбиение на токены. strtok» расширен — потокобезопасные альтернативы `strtok_r()` (POSIX) и `strtok_s()` (C11), пример разбора без модификации строки через `strcspn()`, примечание о пропуске пустых токенов.
- Урок 12 «<string.h>»: раздел 7 «Длина строки» расширен — оптимизации компиляторов (SIMD), пример опасности `strlen()` в цикле, формат печати `%zu`.
- Урок 12 «<string.h>»: раздел 8 «Сообщения об ошибках. strerror» расширен — потокобезопасные аналоги `strerror_r()` (XSI/GNU), `strerror_l()`, `strerror_s()` (C11), таблица частых кодов ошибок, предупреждение о многопоточности.
- Урок 12 «<string.h>»: раздел 9 «Безопасные версии функций (C11)» расширен — полный список функций Annex K с `rsize_t` и `RSIZE_MAX`, альтернативы POSIX (`strlcpy`/`strlcat`, `asprintf`), пример собственной безопасной обёртки.

## 12.08.2026

### Изменено

#### Глава 9. Стандартная библиотека C

- Урок 12 «<string.h>»: раздел 4 «Сравнение по локали» значительно расширен — подробное поведение `strcoll` (правила колляции `LC_COLLATE`: регистр, диакритика, составные буквы, многобайтовые строки) и `strxfrm` (форма сравнения, ограничение `n`, возврат требуемой длины и обнаружение усечения, запрет перекрытия), сравнительная таблица `strcmp`/`strcoll`/`strxfrm`, примеры разницы побайтового и локализованного сравнения и сортировки массива строк через ключи `strxfrm` + `qsort`.
- Урок 12 «<string.h>»: раздел 5 «Поиск в строках» значительно расширен — подробное поведение каждой функции поиска (`memchr`, `strchr`, `strrchr`, `strstr`, `strpbrk`, `strspn`, `strcspn`), сводная таблица возвращаемых значений, дополнительные примеры (имя файла из пути через `strrchr`, поиск в бинарных данных через `memchr`, разбиение строки через пары `strcspn`/`strpbrk`), примечания об указателях внутрь исходной строки и о символе как `int`.

## 11.08.2026

### Изменено

#### Глава 9. Стандартная библиотека C

- Урок 11 «<stdlib.h>»: раздел 8 «Управление памятью» значительно расширен — сводная таблица функций, подробное описание `malloc`/`calloc`/`realloc`/`free`/`aligned_alloc` (выравнивание указателя, нулевой размер, проверка переполнения `num * size` в `calloc`, безопасная идиома `realloc` с временным указателем, неопределённое поведение `realloc(ptr, 0)` в C23, «висячие» указатели), функции C23 `free_sized`/`free_aligned_sized`, примеры для каждой функции и раздел о типичных ошибках работы с памятью.

## 07.08.2026

### Добавлено

#### Глава 9. Стандартная библиотека C

- Урок 13 «<errno.h>» (механизм сообщения об ошибках: макрос `errno` и правила его сброса/проверки, стандартные коды `EDOM`/`ERANGE`/`EILSEQ`, паттерн проверки после вызова `strtol`, ошибки математических функций, вывод текста ошибки через `strerror`/`perror`, потоково-локальная природа `errno`).

### Изменено

#### Глава 9. Стандартная библиотека C

- Урок 12 «<string.h>»: добавлен раздел 2.4 о функциях `strdup`/`strndup` (входят в стандарт C23); обновлено резюме статьи.

#### Правила оформления

- `AGENTS.md`: зафиксировано правило — все статьи курса C опираются на стандарт C23; функции и возможности C23 включаются в статьи как стандартные.

## 05.08.2026

### Добавлено

#### Глава 9. Стандартная библиотека C

- Урок 11 «<stdlib.h>» (функции преобразования строк в числа, `rand`/`srand`, завершение программы `exit`/`_Exit`/`abort`/`atexit`, `getenv`/`system`, `qsort`/`bsearch`, `abs`/`labs`/`llabs` и `div`/`ldiv`/`lldiv`, управление памятью, многобайтовые символы, константы и типы).
- Урок 12 «<string.h>» (копирование `memcpy`/`memmove`/`strcpy`/`strncpy`/`strcat`/`strncat` и их ловушки, сравнение `memcmp`/`strcmp`/`strncmp`, сравнение по локали `strcoll`/`strxfrm`, поиск `strchr`/`strrchr`/`strstr`/`strpbrk`/`strspn`/`strcspn`/`memchr`, разбиение на токены `strtok`, длина `strlen`/`strnlen`, сообщения об ошибках `strerror`, безопасные версии `_s` из C11).

#### Глава 10. POSIX

- Урок 1 «<strings.h>» (заголовочный файл POSIX, которого нет в стандартной библиотеке C: регистронезависимое сравнение `strcasecmp`/`strncasecmp` и аналог `_stricmp` в Windows, устаревшие `bcmp`/`bcopy`/`bzero`/`index`/`rindex` и их замены из `<string.h>`).

### Изменено

#### Глава 9. Стандартная библиотека C

- Урок 11 «<stdlib.h>»: добавлено содержание статьи в начале; подробно расписан раздел о `strtod`/`strtof`/`strtold` (формат разбираемого числа, шестнадцатеричная форма и экспонента `p`/`P`, `INF`/`NAN`, `endptr`, `HUGE_VAL` и `errno`); разделы об остальных функциях дополнены описанием поведения, параметров, возвращаемых значений и ошибок (порядок разбора `atof`/`atoi`/`atol`/`atoll`, автоматическое определение основания в `strtol`, диапазон `[min; max]` в `rand`, порядок действий `exit` и сигнал `SIGABRT` в `abort`, безопасная функция сравнения и сортировка строк в `qsort`, усечение к нулю в `div`, поведение `malloc`/`calloc`/`realloc`/`free`/`aligned_alloc`, возвращаемые значения функций многобайтовых символов).

#### Глава 9. Стандартная библиотека C

- Урок 12 «<string.h>»: ссылка «Вперёд» теперь ведёт на первую статью новой главы 10 (POSIX, урок «<strings.h>»).

#### Главы 10–14

- Главы курса перенумерованы из-за вставки новой главы POSIX под номером 10: «Многопоточность» 10 → 11, «Макросы» 11 → 12, «Среды разработки для С» 12 → 13, «Взаимодействие с кодом Python» 13 → 14, «Дополнительные статьи» 14 → 15; обновлены обзоры глав, индекс курса, хлебные крошки и навигация всех уроков; в первой статье главы «Многопоточность» ссылка «Назад» ведёт на урок «<strings.h>».

## 04.08.2026

### Добавлено

- Индекс курса `Языки программирования/C.md`: обзор курса и содержание всех 14 глав (ссылки на все уроки); ссылка на курс добавлена в оглавление `README.md`.

#### Глава 7. Динамическая память

- Урок 2 «Выделение памяти для двухмерного массива произвольной длины» (зубчатый массив, `int **table` и `rows`, освобождение в обратном порядке).
- Урок 3 «Управление динамической памятью» (указатель как локальный, статический и глобальный объект, момент освобождения памяти).
- Урок 4 «Указатель как результат функции» (возврат указателя, возврат массива из функции, ошибка возврата локальной переменной).
- Урок 5 «Организация памяти программы и структура сегментов» (стек, куча, сегмент констант и глобальных переменных, сегмент кода).

#### Глава 8. Ввод-вывод и работа с файлами

- Урок 1 «Файлы и потоки ввода-вывода» (файл как поток, буферизация, `fopen`/`fclose`, режимы открытия, обработка ошибок) и индекс главы.
- Урок 2 «Чтение и запись бинарных файлов» (`putc`, `getc`/`fgetc`, конец файла и значение `EOF`).
- Урок 3 «Чтение и запись структур в файл» (побайтовая запись структуры, чтение через `malloc`, сохранение и чтение массива структур с метаинформацией о количестве).
- Урок 4 «Чтение и запись в файл с помощью функций fwrite и fread» (запись строк и структур, чтение массива структур и по одной структуре, `feof`/`ferror`).
- Урок 5 «Чтение и запись текстовых файлов» (`fputs`, `fgets`, копирование файлов).
- Урок 6 «Форматируемый ввод-вывод» (`fprintf`, `fscanf`).
- Урок 7 «Позиционирование в файле» (`fseek`, `ftell`, `rewind`, чтение и обновление структур по позиции).
- Урок 8 «Консольный ввод-вывод» (потоки `stdin`/`stdout`/`stderr`, `getchar`/`putchar`, `puts`/`fputs`, `fgets` и конфликт с `scanf`).
- Урок 9 «Форматированный ввод и вывод в строки. Функции sscanf и sprintf» (`sscanf` для разбора строк, связка с `fgets`, `sprintf`).

#### Глава 9. Стандартная библиотека C

- Урок 1 «Заголовочные файлы стандартной библиотеки C» (состав библиотеки по стандартам) и индекс главы.
- Урок 2 «Работа со строками» (`strlen`, `strcmp`, `strcat`, `strcpy`/`strncpy`/`strncpy_s`, `strstr`).
- Урок 3 «Работа с памятью» (`memset`, `memcpy`, `memcmp`).
- Урок 4 «Работа с датами и временем» (`time`, `localtime`, структура `tm`, `strftime`).
- Урок 5 «Математические функции» (`pow`, `round`, `sqrt`, `abs`/`labs`/`llabs`, `fabs`).
- Урок 6 «Преобразование строк в числа и чисел в строки» (`strtol`, `snprintf`).
- Урок 7 «Обобщения и макрос _Generic» (имитация обобщений макросами с `##`, выбор реализации через `_Generic`).
- Урок 8 «Поддержка Unicode и кодировки UTF-8, UTF-16 и UTF-32» (`wchar_t`, `char8_t`/`char16_t`/`char32_t`, префиксы литералов, спецификаторы `%ls`/`%lc`).
- Урок 9 «Платформо-независимые целочисленные типы» (модели данных, типы из `stdint.h`, макросы `PRI`/`SCN` из `inttypes.h`).
- Урок 10 «Проверка символов и ctype.h» (`isspace`, `isalnum`, `isalpha`, `isdigit`, `isxdigit`, `iscntrl`, `isprint`, `isgraph`, `ispunct`, `islower`/`isupper`, `tolower`/`toupper`).

#### Глава 11. Многопоточность

- Урок 1 «Создание потоков» (тип `pthread_t`, `pthread_create`, `pthread_exit`, `sleep`) и индекс главы.
- Урок 2 «Завершение потоков» (`pthread_join`, ожидание нескольких потоков, получение результата потока).
- Урок 3 «Мьютексы» (`pthread_mutex_t`, `lock`/`unlock`, критические секции, взаимоблокировка).
- Урок 4 «Сигналы и условные переменные синхронизации» (`pthread_cond_signal`/`pthread_cond_wait`, защита от раннего пробуждения).
- Урок 5 «Семафоры» (`sem_t`, `sem_init`, `sem_destroy`, `sem_wait`, `sem_post`; упорядочивание действий потоков, ограничение количества потоков).
- Урок 6 «Введение в OpenMP» (директивы `parallel`, `for`, `simd`, `ordered`, `critical`, флаг `-fopenmp`, заголовочный файл `omp.h`, функция `omp_get_thread_num`).

#### Глава 12. Макросы

- Урок 1 «Примеры распространенных макросов» (макросы `MIN`/`MAX`, побочные действия, `#` и `##`, `ARRAY_SIZE`, `SWAP`, `SAFE_FREE`, `OFFSETOF`) и индекс главы.
- Урок 2 «Макрос для вывода отладочной информации» (`DEBUG_PRINT`, `__FILE__`/`__LINE__`/`__func__`, вариативные макросы и `__VA_ARGS__`, управление через `#ifdef DEBUG`).
- Урок 3 «Макрос для создания обобщенного списка» (генерация структуры и функций через `DEFINE_LIST(T)`, `realloc`-расширение, списки через значения и указатели).
- Урок 4 «Макрос перебора списков в стиле for-each» (макрос `foreach` для односвязного списка, `for_each` для обобщенного списка, оператор запятой).
- Урок 5 «Стек на основе макросов» (`PUSH`/`POP`, `STACK_FULL`/`STACK_EMPTY`, `STACK_USED`, `CLEAR_STACK`, указатель вершины стека).
- Урок 6 «X-макросы» (список данных через макрос `X`, генерация перечислений, массивов строк и функций, макрос как параметр, вынос данных в отдельный файл, практические применения и ограничения).
- Урок 7 «Шаблон Result и обработка ошибок» (`DEFINE_RESULT(T)`, структура `Result_##T` через конкатенацию токенов, функции `Ok_##T`/`Err_##T`, конструктор с валидацией, тесты через `assert`).

#### Глава 13. Среды разработки для С

- Урок 1 «Первая программа в Visual Studio» (установка Visual Studio Community, создание проекта по шаблону Empty Project, добавление файла `hello.c`, настройка компиляции как C через параметр Compile As, запуск через `Ctrl+F5`) и индекс главы.
- Урок 2 «Первая программа в Qt Creator» (установка Qt Creator и компилятора MinGW, регистрация учетной записи Qt, создание проекта по шаблону Plain C Application, запуск программы).

#### Глава 14. Взаимодействие с кодом Python

- Урок 1 «Подключение Python» (встраиваемый интерпретатор Python, `Py_Initialize`/`Py_Finalize`/`PyRun_SimpleString`/`PyRun_SimpleFile`, компиляция на Windows и Linux, использование библиотек numpy и matplotlib) и индекс главы.

#### Глава 15. Дополнительные статьи

- Урок 1 «Разделяемые библиотеки на Linux» (динамическое связывание, формат `.so`, команда `ldd`, загрузчик `ld.so`, vDSO, статическая линковка `-static`, создание библиотеки через `-fPIC` и `-shared`, переменная `LD_LIBRARY_PATH`) и индекс главы.
- Урок 2 «Функции setjmp и longjmp и обработка ошибок» (нелокальные переходы, `jmp_buf`, выход из вложенных функций, реализация подобия try-catch, ограничения механизма).
- Урок 3 «Ассемблерные вставки» (выражение `asm()`, синтаксис AT&T, выходные и входные параметры, дескрипторы регистров `"a"`/`"d"`/`"r"`/`"m"`, обновляемые параметры `"+"`, индексы `%N`, `asm volatile`).
- Урок 4 «Измерение времени выполнения программы» (`time()` и `difftime()`, `clock()` и `CLOCKS_PER_SEC`, `gettimeofday()` из `sys/time.h`, `QueryPerformanceCounter`/`QueryPerformanceFrequency` в Windows, чтение TSC через `_rdtsc()`/`__rdtsc()` и `__rdtscp()`, сериализация конвейера инструкцией CPUID).
- Урок 5 «Атрибуты и расширение __attribute__» (синтаксис атрибутов, `noreturn`, `deprecated`, `unused`, `packed` и выравнивание структур, `aligned`, `constructor`/`destructor`, переносимость кода).
- Урок 6 «Преобразование строки в целое число» (`strtol`/`strtoll` с `endptr` и проверкой ошибок, `atol`/`atoll`, `atoi`, `sscanf`, ручное преобразование по таблице ASCII).

### Изменено

#### Глава 7. Динамическая память

- Добавлена навигация «Вперёд» в урок 4 (к уроку 5), обновлены индекс и обзор главы (охват 5 уроков).

#### Глава 8. Ввод-вывод и работа с файлами

- Исправлена фактическая ошибка исходной статьи 8.1: режим `"w+"` описан неверно; по стандарту файл очищается сразу при открытии (создается для чтения и записи).
- Исправлена фактическая ошибка исходной статьи 8.4: `feof()` возвращает ненулевое значение при достижении конца файла (в исходнике было сказано «возвращает 0»).

## 03.08.2026

### Добавлено

#### Глава 4. Функции

- Урок 12 «Функция как результат другой функции» (возврат указателя на функцию, разбор заголовка `int (*select(int choice))(int, int)`, упрощение через `typedef`).
- Урок 13 «Функции с переменным количеством параметров» (многоточие в списке параметров, макросы `va_start`/`va_arg`/`va_end` и тип `va_list` из `stdarg.h`).
- Урок 14 «Параметры командной строки» (`argc`, `argv`, вывод аргументов).

#### Глава 5. Препроцессор

- Урок 1 (этапы компиляции, директивы препроцессора, `#include`, стандартные заголовочные файлы, подключение собственных файлов и `extern`) и индекс главы.
- Урок 2 «Директива #define» (определение идентификатора и макросов с параметрами, `#undef`, константа через `-D`).
- Урок 3 «Макросы» (макросы для выражений, макросы с параметрами, скобки в параметрах, операции `#` и `##`).
- Урок 4 «Условная компиляция» (`#if`/`#elif`/`#else`/`#endif`, `#ifdef`/`#ifndef`, оператор `defined`).
- Урок 5 «Встроенные макросы» (макросы компиляторов, архитектур, порядка байтов и операционных систем).

#### Глава 6. Структуры

- Урок 1 «Определение структур» (объявление и определение, неполные типы, инициализация, `typedef`, области видимости, копирование, ввод с консоли) и индекс главы.
- Урок 2 «Структуры как элементы структур» (вложенные структуры, доступ через несколько точек, инициализация вложенных структур).
- Урок 3 «Указатели на структуры» (операция `->`, самоссылающиеся структуры и списки, объявление до определения, константные структуры).
- Урок 4 «Массивы структур» (инициализация вложенными скобками, доступ по индексу, `sizeof`, указатели на массив структур).
- Урок 5 «Структуры и функции» (передача по значению, указатели на структуры в параметрах, возврат структуры из функции).
- Урок 6 «Размещение структур и их полей в памяти» (выравнивание полей и структур, отступы, выравнивание массивов, оптимизация расположения полей).
- Урок 7 «Составные литералы» (литералы структур, возврат структуры из функции, массивы через составные литералы).
- Урок 8 «Перечисления» (`enum`, числовые значения констант, `typedef`, безымянные перечисления, применение в `switch`).
- Урок 9 «Объединения» (`union`, наложение элементов, анонимные объединения и `typedef`, хранение значений разных типов, указатели).
- Урок 10 «Битовые поля» (поля с шириной в битах, размещение в памяти, проверка через объединение).

#### Глава 7. Динамическая память

- Урок 1 «Выделение и освобождение памяти» (`malloc`, `calloc`, `realloc`, `free`, память под объекты, массивы и структуры) и индекс главы.

#### Правила оформления

- Правило ведения журнала изменений: создан `CHANGELOG.md`, в `AGENTS.md` добавлен раздел «Журнал изменений (CHANGELOG)».

### Изменено

#### Глава 4. Функции

- Добавлена навигация «Вперёд» в урок 13 (к уроку 14), обновлены индекс и обзор главы (охват всех 14 уроков).

#### Глава 5. Препроцессор

- Добавлена навигация «Вперёд» в урок 4 (к уроку 5), обновлены индекс и обзор главы (охват 5 уроков).

#### Глава 6. Структуры

- Добавлена навигация «Вперёд» в урок 9 (к уроку 10), обновлены индекс и обзор главы (охват 10 уроков).

#### Глава 7. Динамическая память

- Исправлена фактическая ошибка исходной статьи 7.1: прототип `free()` — `void free(void *bl)`, а не `void *free(void *bl)` (функция ничего не возвращает).

#### Правила оформления

- `AGENTS.md`: зафиксировано правило обновлять обзорную информацию о главе в заметке с её содержанием при добавлении новой статьи (урока).

## 02.08.2026

### Добавлено

#### Глава 2. Основы языка Си

- Уроки 1–14 (структура программы, переменные, типы данных, консольный вывод, константы, арифметические/логические/поразрядные операции и операции присваивания, преобразование типов, условные конструкции, циклы, массивы и строки, ввод через `scanf`) и индекс главы.

#### Глава 3. Указатели

- Уроки 1–7 (что такое указатели, операции с указателями, арифметика указателей, константы и указатели, указатели и массивы, указатели и строки, массивы указателей и многоуровневая адресация) и индекс главы.

#### Глава 4. Функции

- Уроки 1–11 (определение и описание функций, параметры, результат, рекурсивные функции, область видимости переменных, внешние и статические объекты, классы хранения, указатели и массивы как параметры, указатели на функцию, тип функции, функции как параметры) и индекс главы.

### Изменено

#### Глава 2. Основы языка Си

- Обновлён обзор главы (охват всех уроков).

#### Глава 3. Указатели

- Обновлён обзор главы (охват всех уроков).

#### Главы 2–4

- Все уроки глав 2–4: исправлены фактические ошибки исходных статей (описание `size_t` и `ptrdiff_t`, поведение VLA, `int (*pa)[]` как неполный тип), опечатки, добавлены callout, таблицы и навигация по главе.

## 01.08.2026

### Изменено

#### Глава 1. Введение в Си

- Введено правило нумерации файлов уроков (цифра в имени файла, без цифры в заголовке `#` и хлебных крошках), уроки главы переименованы соответствующим образом.
- Добавлена навигация «Назад | Содержание | Вперёд» в уроки главы.

#### Правила оформления

- `AGENTS.md`: зафиксированы правила именования файлов, навигации и мета-информации для курса C.
