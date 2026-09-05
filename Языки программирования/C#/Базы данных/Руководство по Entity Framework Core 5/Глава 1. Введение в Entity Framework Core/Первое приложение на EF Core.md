# Первое приложение на EF Core

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5|Руководство по Entity Framework Core 5]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 1. Введение в Entity Framework Core|Глава 1. Введение в Entity Framework Core]] / Первое приложение на EF Core

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 1. Введение в Entity Framework Core/Что такое Entity Framework Core|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 1. Введение в Entity Framework Core|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 1. Введение в Entity Framework Core/Подключение к существующей базе данных|Вперёд]]

**Дата написания:** 05.09.2026

Для работы с MS SQL Server через Entity Framework добавим NuGet-пакет Microsoft.EntityFrameworkCore.SqlServer.

Определим модель User и контекст данных:

```csharp
public class User
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int Age { get; set; }
}

public class ApplicationContext : DbContext
{
    public DbSet<User> Users { get; set; }
    public ApplicationContext()
    {
        Database.EnsureCreated();
    }
    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlServer("Server=(localdb)\\mssqllocaldb;Database=helloappdb;Trusted_Connection=True;");
    }
}
```

Использование:

```csharp
using (ApplicationContext db = new ApplicationContext())
{
    User user1 = new User { Name = "Tom", Age = 33 };
    User user2 = new User { Name = "Alice", Age = 26 };

    db.Users.Add(user1);
    db.Users.Add(user2);
    db.SaveChanges();
    Console.WriteLine("Объекты успешно сохранены");

    var users = db.Users.ToList();
    Console.WriteLine("Список объектов:");
    foreach (User u in users)
    {
        Console.WriteLine($"{u.Id}.{u.Name} - {u.Age}");
    }
}
```

**Источник:** [https://metanit.com/sharp/entityframeworkcore/1.2.php](https://metanit.com/sharp/entityframeworkcore/1.2.php)
