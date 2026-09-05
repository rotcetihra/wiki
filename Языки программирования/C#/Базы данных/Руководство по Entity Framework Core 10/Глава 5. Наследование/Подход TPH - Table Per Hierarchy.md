# Подход TPH - Table Per Hierarchy

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10|Руководство по Entity Framework Core 10]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 5. Наследование|Глава 5. Наследование]] / Подход TPH - Table Per Hierarchy

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 4. Отношения между моделями/Иерархические данные|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 5. Наследование|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 5. Наследование/Подход TPT - Table Per Type|Вперёд]]

**Дата написания:** 05.09.2026

По умолчанию при работе с цепочками наследования классов Entity Framework Core использует подход TPH (Table Per Hierarchy / Таблица на одну иерархию классов). При использовании данного подхода TPH для всех классов из одной иерархии в базе данных создается одна таблица. А чтобы определить, к какому именно классу относится строка в таблице, в этой же таблице создается дополнительный столбец - дискриминатор.

Например, у нас есть следующая иерархия классов:

```csharp
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
```

Есть базовый класс User, который представляет пользователя и от которого наследуются класс Employee - класс работника и Manager - класс управляющего.

Определим контекст данных:

```csharp
using Microsoft.EntityFrameworkCore;

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

Чтобы включить все классы из иерархии наследования в базу данных, в контексте данных для каждого типа должен быть определен набор DbSet.

Сгенерированная база данных будет содержать для всех типов одну таблицу Users. Кроме всех свойств классов User, Employee и Manager здесь также появляется еще один столбец - Discriminator. Он имеет тип nvarchar (то есть строка), а в качестве значения он принимает название класса, к которому относится строка в таблице. В итоге в бд будет создаваться следующая таблица:

```sql
CREATE TABLE "Users" (
    "Id"    INTEGER NOT NULL,
    "Name"  TEXT,
    "Discriminator" TEXT NOT NULL,
    "Salary"    INTEGER,
    "Departament"   TEXT,
    CONSTRAINT "PK_Users" PRIMARY KEY("Id" AUTOINCREMENT)
);
```

### Метод UseTphMappingStrategy

Стратегия TPH применяется для создания таблиц в EF Core по умолчанию, и каких-то дополнительных настроек нам не надо настраивать. Но, начиная, с EF Core мы также можем явным образом указать, что мы хотим использовать эту стратегию с помощью метода `UseTphMappingStrategy()` для базового типа иерархии классов:

```csharp
public class ApplicationContext : DbContext
{
    public DbSet<User> Users { get; set; } = null!;

    // ................
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<User>().UseTphMappingStrategy();  // TPH
    }
}
```

**Источник:** [https://metanit.com/sharp/efcore/4.1.php](https://metanit.com/sharp/efcore/4.1.php)
