# Подход TPC - Table Per Class

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10|Руководство по Entity Framework Core 10]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 5. Наследование|Глава 5. Наследование]] / Подход TPC - Table Per Class

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 5. Наследование/Подход TPT - Table Per Type|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 5. Наследование|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 6. Запросы и LINQ to Entities/Введение в LINQ to Entities|Вперёд]]

**Дата написания:** 05.09.2026

Начиная с версии EF Core 7.0 во фреймворк была добавлена поддержка нового подхода к наследованию - TPC (Table Per Concrete Type / Таблица на каждый отдельный тип). Этот подход предполагает создание для каждой модели по отдельной таблице. Столбцы в каждой таблице создаются по всем свойствам, в том числе и унаследованным. С одной стороны, может показаться, что это усложняет хранение данных. Но с другой стороны, TPC работает более оптимально по сравнению с TPT для многих типов запросов, так как количество таблиц, которые необходимо запрашивать, уменьшено. Кроме того, результаты из каждой таблицы объединяются с помощью sql-команды `UNION ALL`, что может быть значительно быстрее, чем объединение таблиц с помощью `INNER JOIN`, которое применяется в TPT.

Для применения подхода TPC для базовой сущности иерархии классов вызывается метод UseTpcMappingStrategy. Для этого переопределяется метод OnModelCreating() контекста данных:

```csharp
using Microsoft.EntityFrameworkCore;

public class User
{
    public string Id { get; set; }=Guid.NewGuid().ToString();
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
        modelBuilder.Entity<User>().UseTpcMappingStrategy();  // Используем стратегию TPC
    }
}
```

В случае с SQLite в бд будут создаваться следующие три таблицы:

```sql
CREATE TABLE "Users" (
    "Id" TEXT NOT NULL CONSTRAINT "PK_Users" PRIMARY KEY,
    "Name" TEXT NULL
);
CREATE TABLE "Employees" (
    "Id" TEXT NOT NULL CONSTRAINT "PK_Employees" PRIMARY KEY,
    "Name" TEXT NULL,
    "Salary" INTEGER NOT NULL
);
CREATE TABLE "Managers" (
    "Id" TEXT NOT NULL CONSTRAINT "PK_Managers" PRIMARY KEY,
    "Name" TEXT NULL,
    "Departament" TEXT NULL
);
```

### Генерация идентификаторов

Поход TPC имеет ограничения в плане использования свойств-идентфикаторов. Во-первых, важно понимать, что EF Core требует, чтобы все сущности в иерархии имели уникальное значение ключа, даже если сущности имеют разные типы. Таким образом, в примере выше у объекта Employee не может быть того же значения ключа Id, что и у объекта Manager. Во-вторых, в отличие от TPT, здесь нет общей таблицы, которая могла бы действовать как единственное место, где хранятся ключевые значения и могут быть сгенерированы. И здесь есть различные стратегии.

#### Явная установка Id

Выше в примере была продемонстрирована одна из стратегий, при которой мы сами явным образом генерируем id:

```csharp
public class User
{
    public string Id { get; set; }=Guid.NewGuid().ToString();
    //....................
}
```

Здесь Id присваивается guid - уникальное значение, благодаря чему мы знаем, что у нас будет только один объект, который будут иметь ключ с определенным значением.

Это могут быть и числовые ключи, главное, что ключи добавляемых объектов не конфликтовали.

#### Неявная установка с помощью последовательности

Другая стратегия для баз данных, которые поддерживают последовательности, значения ключей могут быть сгенерированы с помощью последовательностей. Эта стратегия используется по умолчанию в TPC для SQL Server.

Другие стратегии могут предусматривать установку на уровне бд генератора для идентификаторов. Для этого можно для настройки маппинга можно использовать метод UseIdentityColumn. Он принимает ряд параметров. В частности, первый параметр представляет начальное значение для id, а второй параметр - приращение для последующих добавляемых объектов.

**Источник:** [https://metanit.com/sharp/efcore/4.3.php](https://metanit.com/sharp/efcore/4.3.php)
