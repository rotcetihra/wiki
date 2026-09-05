# <type_traits>

[[Языки программирования/C++/Библиотеки|Библиотеки]] / <type_traits>

[[Языки программирования/C++/Библиотеки/<tuple>|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<typeindex>|Вперёд]]

**Дата написания:** 05.09.2026

## Оглавление

### Функции

- [[Языки программирования/C++/Библиотеки/<type_traits>/is_same|is_same]] — проверка равенства типов
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_integral|is_integral]] — проверка целочисленного типа
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_floating_point|is_floating_point]] — проверка floating-point типа
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_array|is_array]] — проверка массива
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_class|is_class]] — проверка класса
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_enum|is_enum]] — проверка перечисления
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_function|is_function]] — проверка функции
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_pointer|is_pointer]] — проверка указателя
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_reference|is_reference]] — проверка ссылки
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_const|is_const]] — проверка const
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_volatile|is_volatile]] — проверка volatile
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_signed|is_signed]] — проверка знакового типа
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_unsigned|is_unsigned]] — проверка беззнакового типа
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_void|is_void]] — проверка void
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_null_pointer|is_null_pointer]] — проверка nullptr
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_bounded_array|is_bounded_array]] — проверка фикс. массива
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_unbounded_array|is_unbounded_array]] — проверка массива непред. размера
- [[Языки программирования/C++/Библиотеки/<type_traits>/remove_const|remove_const]] — удаление const
- [[Языки программирования/C++/Библиотеки/<type_traits>/remove_volatile|remove_volatile]] — удаление volatile
- [[Языки программирования/C++/Библиотеки/<type_traits>/remove_cv|remove_cv]] — удаление const и volatile
- [[Языки программирования/C++/Библиотеки/<type_traits>/remove_reference|remove_reference]] — удаление ссылки
- [[Языки программирования/C++/Библиотеки/<type_traits>/remove_cvref|remove_cvref]] — удаление cv и ссылки (C++20)
- [[Языки программирования/C++/Библиотеки/<type_traits>/add_const|add_const]] — добавление const
- [[Языки программирования/C++/Библиотеки/<type_traits>/add_volatile|add_volatile]] — добавление volatile
- [[Языки программирования/C++/Библиотеки/<type_traits>/add_cv|add_cv]] — добавление const и volatile
- [[Языки программирования/C++/Библиотеки/<type_traits>/add_lvalue_reference|add_lvalue_reference]] — добавление lvalue-ссылки
- [[Языки программирования/C++/Библиотеки/<type_traits>/add_rvalue_reference|add_rvalue_reference]] — добавление rvalue-ссылки
- [[Языки программирования/C++/Библиотеки/<type_traits>/add_pointer|add_pointer]] — добавление указателя
- [[Языки программирования/C++/Библиотеки/<type_traits>/decay|decay]] — свёртывание типа
- [[Языки программирования/C++/Библиотеки/<type_traits>/enable_if|enable_if]] — условное включение (SFINAE)
- [[Языки программирования/C++/Библиотеки/<type_traits>/conditional|conditional]] — выбор типа по условию
- [[Языки программирования/C++/Библиотеки/<type_traits>/common_type|common_type]] — общий тип
- [[Языки программирования/C++/Библиотеки/<type_traits>/underlying_type|underlying_type]] — базовый тип перечисления
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_convertible|is_convertible]] — проверка преобразования
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_nothrow_constructible|is_nothrow_constructible]] — безопасность исключений
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_trivially_copyable|is_trivially_copyable]] — тривиальная копируемость
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_standard_layout|is_standard_layout]] — стандартное расположение
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_pod|is_pod]] — проверка POD
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_literal_type|is_literal_type]] — проверка литерального типа
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_empty|is_empty]] — пустой класс
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_polymorphic|is_polymorphic]] — полиморфный класс
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_abstract|is_abstract]] — абстрактный класс
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_final|is_final]] — final-класс
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_aggregate|is_aggregate]] — агрегат (C++17)
- [[Языки программирования/C++/Библиотеки/<type_traits>/alignment_of|alignment_of]] — выравнивание
- [[Языки программирования/C++/Библиотеки/<type_traits>/rank|rank]] — размерность массива
- [[Языки программирования/C++/Библиотеки/<type_traits>/extent|extent]] — размер по измерению
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_invocable|is_invocable]] — проверка вызываемости (C++17)
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_nothrow_invocable|is_nothrow_invocable]] — безопасность исключений вызова (C++17)
- [[Языки программирования/C++/Библиотеки/<type_traits>/invoke_result|invoke_result]] — тип результата вызова (C++17)
- [[Языки программирования/C++/Библиотеки/<type_traits>/conjunction|conjunction]] — логическое И метатипов
- [[Языки программирования/C++/Библиотеки/<type_traits>/disjunction|disjunction]] — логическое ИЛИ метатипов
- [[Языки программирования/C++/Библиотеки/<type_traits>/negation|negation]] — логическое отрицание
- [[Языки программирования/C++/Библиотеки/<type_traits>/is_constant_evaluated|is_constant_evaluated]] — проверка constexpr (C++20)

## Описание библиотеки

Заголовочный файл `<type_traits>` определяет набор метатипов для проверки свойств типов на этапе компиляции.

## Исключения

- **Исключения:** См. описание отдельных функций и типов.
- **Безопасность в C++11:** Не является потокобезопасным — один объект не должен использоваться из нескольких потоков без синхронизации.

## Стандарты

C++11, C++17, C++20, C++23.

## Источники

- https://en.cppreference.com/w/cpp/header/type_traits
- ISO/IEC 14882:2024

[[Языки программирования/C++/Библиотеки/<tuple>|Назад]] | [[Языки программирования/C++/Библиотеки|Содержание]] | [[Языки программирования/C++/Библиотеки/<typeindex>|Вперёд]]
