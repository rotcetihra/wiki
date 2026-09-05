# Explicit loading

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10|Руководство по Entity Framework Core 10]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 4. Отношения между моделями|Глава 4. Отношения между моделями]] / Explicit loading

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 4. Отношения между моделями/Загрузка связанных данных. Метод Include|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 4. Отношения между моделями|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 4. Отношения между моделями/Lazy loading|Вперёд]]

**Дата написания:** 05.09.2026

Стратегия Explicit loading предполагает явную загрузку данных с помощью метода Load(). Допустим, у нас имеются следующие сущности и контекст данных:

```csharp
using Microsoft.EntityFrameworkCore;

public class ApplicationContext : DbContext
{
    public DbSet<User> Users { get; set; } = null!;
    public DbSet<Company> Companies { get; set; } = null!;

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlite("Data Source=helloapp.db");
    }
}
public class Company
{
    public int Id { get; set; }
    public string? Name { get; set; }
    public List<User> Users { get; set; } = new ();
}
public class User
{
    public int Id { get; set; }
    public string? Name { get; set; }

    public int? CompanyId { get; set; }
    public Company? Company { get; set; }
}
```

Загрузим данные по первой компании:

```csharp
using Microsoft.EntityFrameworkCore;

using (ApplicationContext db = new ApplicationContext())
{
    // пересоздадим базу данных
    db.Database.EnsureDeleted();
    db.Database.EnsureCreated();

    // добавляем начальные данные
    Company microsoft = new Company { Name = "Microsoft" };
    Company google = new Company { Name = "Google" };
    db.Companies.AddRange(microsoft, google);

    User tom = new User { Name = "Tom", Company = microsoft };
    User bob = new User { Name = "Bob", Company = google };
    User alice = new User { Name = "Alice", Company = microsoft };
    User kate = new User { Name = "Kate", Company = google };
    db.Users.AddRange(tom, bob, alice, kate);

    db.SaveChanges();
}
using (ApplicationContext db = new ApplicationContext())
{
    Company? company = db.Companies.FirstOrDefault();
    if (company != null)
    {
        db.Users.Where(u => u.CompanyId == company.Id).Load();

        Console.WriteLine($"Company: {company.Name}");
        foreach (var u in company.Users)
            Console.WriteLine($"User: {u.Name}");
    }
}
```

Выражение `db.Users.Where(p=>p.CompanyId==company.Id).Load()` загружает пользователей в контекст. Подвыражение `Where(p=>p.CompanyId==company.Id)` означает, что загружаются только те пользователи, у которых свойство CompanyId соответствует свойству Id ранее полученной компании. После этого нам не надо подгружать связанные данные, так как они уже есть в контексте.

Консольный вывод программы:

```
Company: Microsoft
User: Tom
User: Alice
```

Для загрузки связанных данных мы также можем использовать методы Collection() и Reference. Метод Collection применяется, если навигационное свойство представляет коллекцию:

```csharp
using (ApplicationContext db = new ApplicationContext())
{
    Company? company = db.Companies.FirstOrDefault();
    if(company != null)
    {
        db.Entry(company).Collection(c => c.Users).Load();

        Console.WriteLine($"Company: {company.Name}");
        foreach (var u in company.Users)
            Console.WriteLine($"User: {u.Name}");
    }
}
```

Если навигационное свойство представляет одиночный объект, то можно применять метод Reference:

```csharp
using (ApplicationContext db = new ApplicationContext())
{
    User? user = db.Users.FirstOrDefault();  // получаем первого пользователя
    if (user != null)
    {
        db.Entry(user).Reference(u => u.Company).Load();
        Console.WriteLine($"{user.Name} - {user.Company?.Name}");   // Tom - Microsoft
    }
}
```

**Источник:** [https://metanit.com/sharp/efcore/3.8.php](https://metanit.com/sharp/efcore/3.8.php)
