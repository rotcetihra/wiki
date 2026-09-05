# Отслеживание объектов и AsNoTracking

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10|Руководство по Entity Framework Core 10]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 6. Запросы и LINQ to Entities|Глава 6. Запросы и LINQ to Entities]] / Отслеживание объектов и AsNoTracking

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 6. Запросы и LINQ to Entities/Агрегатные операции|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 6. Запросы и LINQ to Entities|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 6. Запросы и LINQ to Entities/Выполнение запросов|Вперёд]]

**Дата написания:** 05.09.2026

Запросы могут быть отслеживаемыми и неотслеживаемыми. По умолчанию все запросы, которые возвращают объекты классов моделей являются отслеживаемыми. Когда контекст данных извлекает данные из базы данных, Entity Framework Core помещает извлеченные объекты в кэш и отслеживает изменения, которые происходят с этими объектами вплоть до использования метода SaveChanges()/SaveChangesAsync(), который фиксирует все изменения в базе данных. Но нам не всегда необходимо отслеживать изменения. Например, нам надо просто вывести данные для просмотра.

Чтобы данные не помещались в кэш, применяется метод AsNoTracking(). Этот метод применяется к объекту IQueryable. При его применении возвращаемые из запроса данные не кэшируются. То есть запрос является неотслеживаемым. А это означает, что Entity Framework Core не производит какую-то дополнительную обработку и не выделяет дополнительное место для хранения извлеченных из БД объектов. И поэтому такие запросы работают быстрее.

```csharp
using (ApplicationContext db = new ApplicationContext())
{
    var user = db.Users.AsNoTracking().FirstOrDefault();
    if (user != null)
    {
        user.Age = 22;
        db.SaveChanges();
    }

    var users = db.Users.AsNoTracking().ToList();
    foreach (var u in users)
        Console.WriteLine($"{u.Name} ({u.Age})");
}
```

### Свойство ChangeTracker

Кроме использования метода AsNoTracking, можно отключить отслеживание в целом для объекта контекста. Для этого надо установить значение QueryTrackingBehavior.NoTracking для свойства db.ChangeTracker.QueryTrackingBehavior:

```csharp
using (ApplicationContext db = new ApplicationContext())
{
    db.ChangeTracker.QueryTrackingBehavior = QueryTrackingBehavior.NoTracking;
    var user = db.Users.FirstOrDefault();
    if (user != null)
    {
        user.Age = 8;
        db.SaveChanges();
    }

    var users = db.Users.ToList();
    foreach (var u in users)
        Console.WriteLine($"{u.Name} ({u.Age})");
}
```

Также можно отключить отслеживание на уровне всего контекста данных, например, в его конструкторе:

```csharp
public ApplicationContext()
{
    ChangeTracker.QueryTrackingBehavior = QueryTrackingBehavior.NoTracking;
}
```

**Источник:** [https://metanit.com/sharp/efcore/5.7.php](https://metanit.com/sharp/efcore/5.7.php)
