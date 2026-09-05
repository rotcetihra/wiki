# Подход TPT - Table Per Type

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10|Руководство по Entity Framework Core 10]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 5. Наследование|Глава 5. Наследование]] / Подход TPT - Table Per Type

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 5. Наследование/Подход TPH - Table Per Hierarchy|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 5. Наследование|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 5. Наследование/Подход TPC - Table Per Class|Вперёд]]

**Дата написания:** 05.09.2026

В прошлой статье был рассмотрен подход TPH - одна таблица для всей иерархии наследования классов. Но также EntityFramework Core позволяет использовать другой подход - TPT или Table Per Type, который предполагает создание отдельной таблицы для каждого класса из иерархии. Для реализации подхода TPT можно использовать два способа: атрибуты или Fluent API.

## Применение TPT на основе атрибутов

С помощью атрибута [Table] мы можем указать для каждого класса свою таблицу:

```csharp
using System.ComponentModel.DataAnnotations.Schema;
using Microsoft.EntityFrameworkCore;

public class User
{
    public int Id { get; set; }
    public string? Name { get; set; }
}
[Table("Employees")]
public class Employee : User
{
    public int Salary { get; set; }
}
[Table("Managers")]
public class Manager : User
{
    public string? Departament { get; set; }
}

public class ApplicationContext : DbContext
{
    public DbSet<User> Users { get; set; } = null!;
    public DbSet<Employee> Employees { get; set; } = null!;
    public DbSet<Manager> Managers { get; set; } = null!;
    public ApplicationContext()
    {
        Database.EnsureDeleted();
        Database.EnsureCreated();
    }
    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlite("Data Source=helloapp.db");
    }
}
```

В этом случае в бд будут создаваться следующие три таблицы:

```sql
CREATE TABLE "Users" (
    "Id"    INTEGER NOT NULL,
    "Name"  TEXT,
    CONSTRAINT "PK_Users" PRIMARY KEY("Id" AUTOINCREMENT)
);
CREATE TABLE "Employees" (
    "Id"    INTEGER NOT NULL,
    "Salary"    INTEGER NOT NULL,
    CONSTRAINT "FK_Employees_Users_Id" FOREIGN KEY("Id") REFERENCES "Users"("Id") ON DELETE CASCADE,
    CONSTRAINT "PK_Employees" PRIMARY KEY("Id" AUTOINCREMENT)
);
CREATE TABLE "Managers" (
    "Id"    INTEGER NOT NULL,
    "Departament"   TEXT,
    CONSTRAINT "FK_Managers_Users_Id" FOREIGN KEY("Id") REFERENCES "Users"("Id") ON DELETE CASCADE,
    CONSTRAINT "PK_Managers" PRIMARY KEY("Id" AUTOINCREMENT)
);
```

Здесь мы видим, что все свойства базового класса User будут храниться в одной таблице, а те данные, которые относятся только к производным классам, хранятся в отдельных таблицах.

## Применение TPT на основе Fluent API

Также мы можем настроить TPT с помощью метода ToTable() во Fluent API:

```csharp
using Microsoft.EntityFrameworkCore;

public class User
{
    public int Id { get; set; }
    public string? Name { get; set; }
}
public class Employee : User
{
    public int Salary { get; set; }
}
public class Manager : User
{
    public string? Departament { get; set; }
}

public class ApplicationContext : DbContext
{
    public DbSet<User> Users { get; set; } = null!;
    public DbSet<Employee> Employees { get; set; } = null!;
    public DbSet<Manager> Managers { get; set; } = null!;
    public ApplicationContext()
    {
        Database.EnsureDeleted();
        Database.EnsureCreated();
    }
    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlite("Data Source=helloapp.db");
    }
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Employee>().ToTable("Employees");
        modelBuilder.Entity<Manager>().ToTable("Managers");
    }
}
```

### Метод UseTptMappingStrategy

Начиная с версии EF Core 7.0 также можно вызвать метод UseTptMappingStrategy для базовой сущности иерархии:

```csharp
public class ApplicationContext : DbContext
{
    public DbSet<User> Users { get; set; } = null!;
    public DbSet<Employee> Employees { get; set; } = null!;
    public DbSet<Manager> Managers { get; set; } = null!;
    public ApplicationContext()
    {
        Database.EnsureDeleted();
        Database.EnsureCreated();
    }
    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlite("Data Source=helloapp.db");
    }
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<User>().UseTptMappingStrategy();    // устанавливаем подход TPT
    }
}
```

**Источник:** [https://metanit.com/sharp/efcore/4.2.php](https://metanit.com/sharp/efcore/4.2.php)
