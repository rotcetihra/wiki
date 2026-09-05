# Подход TPT - Table Per Type

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5|Руководство по Entity Framework Core 5]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 4. Наследование|Глава 4. Наследование]] / Подход TPT - Table Per Type

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 4. Наследование/Подход TPH - Table Per Hierarchy|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 4. Наследование|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 5. Запросы и LINQ to Entities/Введение в LINQ to Entities|Вперёд]]

**Дата написания:** 05.09.2026

Подход TPT: создание отдельной таблицы для каждого класса из иерархии:

```csharp
[Table("Employees")]
public class Employee : User { public int Salary { get; set; } }
[Table("Managers")]
public class Manager : User { public string? Departament { get; set; } }
```

**Источник:** [https://metanit.com/sharp/entityframeworkcore/4.2.php](https://metanit.com/sharp/entityframeworkcore/4.2.php)
