# Подход TPH - Table Per Hierarchy

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5|Руководство по Entity Framework Core 5]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 4. Наследование|Глава 4. Наследование]] / Подход TPH - Table Per Hierarchy

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 3. Отношения между моделями/Комплексные типы|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 4. Наследование|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 4. Наследование/Подход TPT - Table Per Type|Вперёд]]

**Дата написания:** 05.09.2026

По умолчанию EF Core использует подход TPH - одна таблица для всей иерархии классов. Для различия строк используется столбец-дискриминатор:

```csharp
public class User { public int Id { get; set; } public string? Name { get; set; } }
public class Employee : User { public int Salary { get; set; } }
public class Manager : User { public string? Departament { get; set; } }
```

**Источник:** [https://metanit.com/sharp/entityframeworkcore/4.1.php](https://metanit.com/sharp/entityframeworkcore/4.1.php)
