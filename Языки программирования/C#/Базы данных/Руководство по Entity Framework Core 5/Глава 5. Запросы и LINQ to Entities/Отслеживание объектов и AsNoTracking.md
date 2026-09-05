# Отслеживание объектов и AsNoTracking

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5|Руководство по Entity Framework Core 5]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 5. Запросы и LINQ to Entities|Глава 5. Запросы и LINQ to Entities]] / Отслеживание объектов и AsNoTracking

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 5. Запросы и LINQ to Entities/Агрегатные операции|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 5. Запросы и LINQ to Entities|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 5. Запросы и LINQ to Entities/Выполнение запросов|Вперёд]]

**Дата написания:** 05.09.2026

Для отключения отслеживания используется метод AsNoTracking():

```csharp
var users = db.Users.AsNoTracking().ToList();
```

**Источник:** [https://metanit.com/sharp/entityframeworkcore/5.7.php](https://metanit.com/sharp/entityframeworkcore/5.7.php)
