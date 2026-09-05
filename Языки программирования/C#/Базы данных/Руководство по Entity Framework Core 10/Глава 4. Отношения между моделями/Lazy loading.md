# Lazy loading

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10|Руководство по Entity Framework Core 10]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 4. Отношения между моделями|Глава 4. Отношения между моделями]] / Lazy loading

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 4. Отношения между моделями/Explicit loading|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 4. Отношения между моделями|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 4. Отношения между моделями/Отношение один к одному|Вперёд]]

**Дата написания:** 05.09.2026

Lazy loading или ленивая загрузка предполагает неявную автоматическую загрузку связанных данных при обращении к навигационному свойству. Однако здесь есть ряд условий:

-   При конфигурации контекста данных вызвать метод UseLazyLoadingProxies()
-   Все навигационные свойства должны быть определены как виртуальные (то есть с модификатором virtual), при этом сами классы моделей должны быть открыты для наследования

Используем lazy loading. Прежде всего добавим в проект через nuget пакет Microsoft.EntityFrameworkCore.Proxies.

Далее определим следующие модели и контекст данных:

```csharp
using Microsoft.EntityFrameworkCore;

public class ApplicationContext : DbContext
{
    public DbSet<User> Users { get; set; } = null!;
    public DbSet<Company> Companies { get; set; } = null!;

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder
            .UseLazyLoadingProxies()		// подключение lazy loading
            .UseSqlite("Data Source=helloapp.db");
    }
}
public class Company
{
    public int Id { get; set; }
    public string? Name { get; set; }
    public virtual List<User> Users { get; set; } = new ();
}

public class User
{
    public int Id { get; set; }
    public string? Name { get; set; }

    public int? CompanyId { get; set; }
    public virtual Company? Company { get; set; }
}
```

Прежде всего в методе OnConfiguring у объекта DbContextOptionsBuilder вызывается метод UseLazyLoadingProxies(), который делает доступной ленивую загрузку.

Также навигационное свойство Users в классе Company и навигационное свойство Company в классе User определены как виртуальные, то есть имеют модификатор virtual.

После этого мы можем загрузить пользователей и связанные с ними компании следующим образом:

```csharp
using (ApplicationContext db = new ApplicationContext())
{
    // пересоздадим базу данных
    db.Database.EnsureDeleted();
    db.Database.EnsureCreated();

    // добавляем начальные данные
    Company microsoft = new Company { Name = "Microsoft" };
    Company google = new Company { Name = "Google"};
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
    var users = db.Users.ToList();
    foreach (User user in users)
        Console.WriteLine($"{user.Name} - {user.Company?.Name}");
}
```

Консольный вывод:

```
Tom - Microsoft
Alice - Microsoft
Bob - Google
Kate - Google
```

Теперь посмотрим, что происходит на уровне базы данныx. Вначале получаем пользователей:

```csharp
var users = db.Users.ToList();
```

В базе данных выполняется sql-команда:

```sql
SELECT "u"."Id", "u"."CompanyId", "u"."Name"
FROM "Users" AS "u"
```

Далее в цикле перебираем всех полученных пользователей и обращаемся к навигационному свойству Company для получения связанной компании:

```csharp
foreach (User user in users)
    Console.WriteLine($"{user.Name} - {user.Company?.Name}");
```

Поскольку идет обращение к навигационному свойству Company, то автоматически подтягиваются связанные с ним данные - объекты Company. Перебираются четыре пользователя, но выполняются только два запроса, так как после того как объект загружен в контекст, в дальнейшем он берется из контекста.

Однако при использовании lazy loading следует учитывать что если в базе данных произошли какие-нибудь изменения, например, другой пользователь изменил данные, то данные не перезагужаются, контекст продолжает использовать те данные, которые были ранее загружены.

**Источник:** [https://metanit.com/sharp/efcore/3.9.php](https://metanit.com/sharp/efcore/3.9.php)
