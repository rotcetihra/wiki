# Выполнение SQL-запросов

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5|Руководство по Entity Framework Core 5]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 6. SQL в Entity Framework Core|Глава 6. SQL в Entity Framework Core]] / Выполнение SQL-запросов

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 5. Запросы и LINQ to Entities/Фильтры запросов уровня модели|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 6. SQL в Entity Framework Core|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 6. SQL в Entity Framework Core/Хранимые функции|Вперёд]]

**Дата написания:** 05.09.2026

Для выполнения SQL-запросов - FromSqlRaw/FromSqlInterpolated:

```csharp
var users = db.Users.FromSqlRaw("SELECT * FROM Users").ToList();
```

Для ExecuteSqlRaw/ExecuteSqlInterpolated - для INSERT/UPDATE/DELETE:

```csharp
db.Database.ExecuteSqlRaw("DELETE FROM Users WHERE Name={0}", "Tom");
```

**Источник:** [https://metanit.com/sharp/entityframeworkcore/6.1.php](https://metanit.com/sharp/entityframeworkcore/6.1.php)
