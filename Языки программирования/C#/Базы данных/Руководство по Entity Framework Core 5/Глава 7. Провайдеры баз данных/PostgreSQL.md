# PostgreSQL

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5|Руководство по Entity Framework Core 5]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 7. Провайдеры баз данных|Глава 7. Провайдеры баз данных]] / PostgreSQL

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 6. SQL в Entity Framework Core/Хранимые процедуры|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 7. Провайдеры баз данных|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 7. Провайдеры баз данных/MySQL|Вперёд]]

**Дата написания:** 05.09.2026

Для работы с PostgreSQL добавляется пакет Npgsql.EntityFrameworkCore.PostgreSQL. Для подключения - метод UseNpgsql():

```csharp
optionsBuilder.UseNpgsql("Host=localhost;Port=5432;Database=usersdb;Username=postgres;Password=пароль");
```

**Источник:** [https://metanit.com/sharp/entityframeworkcore/7.1.php](https://metanit.com/sharp/entityframeworkcore/7.1.php)
