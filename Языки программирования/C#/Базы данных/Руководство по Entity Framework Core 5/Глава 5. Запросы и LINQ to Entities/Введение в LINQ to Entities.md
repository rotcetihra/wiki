# Введение в LINQ to Entities

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5|Руководство по Entity Framework Core 5]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 5. Запросы и LINQ to Entities|Глава 5. Запросы и LINQ to Entities]] / Введение в LINQ to Entities

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 4. Наследование/Подход TPT - Table Per Type|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 5. Запросы и LINQ to Entities|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 5. Запросы и LINQ to Entities/Выборка и фильтрация|Вперёд]]

**Дата написания:** 05.09.2026

Для извлечения данных из БД EF Core использует LINQ to Entities. Запросы создаются через операторы LINQ или методы расширения:

```csharp
var users = db.Users.Include(p => p.Company).Where(p => p.CompanyId == 1).ToList();
```

**Источник:** [https://metanit.com/sharp/entityframeworkcore/5.1.php](https://metanit.com/sharp/entityframeworkcore/5.1.php)
