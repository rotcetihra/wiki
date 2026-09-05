# MySQL

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5|Руководство по Entity Framework Core 5]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 7. Провайдеры баз данных|Глава 7. Провайдеры баз данных]] / MySQL

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 7. Провайдеры баз данных/PostgreSQL|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 7. Провайдеры баз данных|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 8. Дополнительные статьи/Параллелизм|Вперёд]]

**Дата написания:** 05.09.2026

Для работы с MySQL добавляется пакет Pomelo.EntityFrameworkCore.MySql. Для подключения - метод UseMySql():

```csharp
optionsBuilder.UseMySql("server=localhost;user=root;password=123456789;database=usersdb;",
    new MySqlServerVersion(new Version(8, 0, 25)));
```

**Источник:** [https://metanit.com/sharp/entityframeworkcore/7.2.php](https://metanit.com/sharp/entityframeworkcore/7.2.php)
