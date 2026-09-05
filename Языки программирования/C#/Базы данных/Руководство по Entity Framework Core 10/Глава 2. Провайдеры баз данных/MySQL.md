# MySQL

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10|Руководство по Entity Framework Core 10]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 2. Провайдеры баз данных|Глава 2. Провайдеры баз данных]] / MySQL

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 2. Провайдеры баз данных/MS SQL Server|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 2. Провайдеры баз данных|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 2. Провайдеры баз данных/PostgreSQL|Вперёд]]

**Дата написания:** 05.09.2026

Для подключения к MySQL добавим через Nuget пакет Pomelo.EntityFrameworkCore.MySql.

Стоит отметить, что также есть официальный провайдер от Oracle - MySql.EntityFrameworkCore, но он развивается довольно медленно, кроме того, не имеет поддержки ряда функционала. Поэтому предпочтительнее использовать пакет Pomelo.EntityFrameworkCore.MySql.

Для работы определим класс User:

```csharp
public class User
{
    public int Id { get; set; }
    public string? Name { get; set; }
    public int Age { get; set; }
}
```

И также определим контекст данных - класс ApplicationContext:

```csharp
using Microsoft.EntityFrameworkCore;

public class ApplicationContext : DbContext
{
    public DbSet<User> Users { get; set; } = null!;

    public ApplicationContext()
    {
        Database.EnsureCreated();
    }
    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseMySql("server=localhost;user=root;password=123456789;database=usersdb;",
            new MySqlServerVersion(new Version(8, 0, 25)));
    }
}
```

Для работы с MySQL вызывается метод UseMySql(), в который передается строка подключения. В строке подключения указываются адрес сервера (параметр server), имя пользователя в субд (User), его пароль (Password) и имя базы данных (Database).

В качестве второго параметра передается номер версии MySQL в виде объекта MySqlServerVersion - в его конструктор передается объект `Version`, который собственно содержит номер установленной версии MySQL. Например, в моем случае это версия 8.0.25, соответственно я передаю объект `new MySqlServerVersion(new Version(8, 0, 25))`. Версию MySQL можно узнать, например, через MySQL Workbench.

И для тестирования определим в файле Program.cs добавление и вывод данных:

```csharp
// добавление данных
using (ApplicationContext db = new ApplicationContext())
{
    User user1 = new User { Name = "Tom", Age = 33 };
    User user2 = new User { Name = "Alice", Age = 26 };

    db.Users.AddRange(user1, user2);
    db.SaveChanges();
}
// получение данных
using (ApplicationContext db = new ApplicationContext())
{
    var users = db.Users.ToList();
    Console.WriteLine("Список объектов:");
    foreach (User u in users)
    {
        Console.WriteLine($"{u.Id}.{u.Name} - {u.Age}");
    }
}
```

Результат программы:

```
Объекты успешно сохранены
Список объектов:
1.Tom - 33
2.Alice - 26
```

**Источник:** [https://metanit.com/sharp/efcore/7.2.php](https://metanit.com/sharp/efcore/7.2.php)
