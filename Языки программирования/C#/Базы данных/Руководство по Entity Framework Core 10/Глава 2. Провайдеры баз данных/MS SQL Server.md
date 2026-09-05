# MS SQL Server

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10|Руководство по Entity Framework Core 10]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 2. Провайдеры баз данных|Глава 2. Провайдеры баз данных]] / MS SQL Server

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 1. Введение в Entity Framework Core/Управление схемой БД и миграции|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 2. Провайдеры баз данных|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 2. Провайдеры баз данных/MySQL|Вперёд]]

**Дата написания:** 05.09.2026

Для работы с базой данных MS SQL Server через Entity Framework Core в проект необходимо добавить Nuget-пакет Microsoft.EntityFrameworkCore.SqlServer.

После установки пакета определим в проекте класс User:

```csharp
public class User
{
    public int Id { get; set; }
    public string? Name { get; set; }
    public int Age { get; set; }
}
```

И также определим класс контекста данных:

```csharp
using Microsoft.EntityFrameworkCore;

public class ApplicationContext : DbContext
{
    public DbSet<User> Users { get; set; } = null!;

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlServer(@"Server=(localdb)\mssqllocaldb;Database=helloappdb;Trusted_Connection=True;");
    }
}
```

Для подключения к SQL Server у класса DbContextOptionsBuilder определен метод расширения UseSqlServer, в который передается строка подключения для соединения с MS SQL Server. Строка подключения разбивается на несколько частей:

-   **Server**: название сервера. В данном случае используется специальный движок MS SQL Server - localdb, который предназначен специально для нужд разработки. Для MS SQL Server Express этот параметр, как правило, имеет значение `.\SQLEXPRESS`
-   **Database**: название базы данных
-   **Trusted\_Connection**: устанавливает проверку подлинности

В данном случае мы определяем, что в качестве сервера будет использоваться движок localdb, который предназначен специально для разработки:`("Server=(localdb)\mssqllocaldb")`, а база данных будет называться `helloappdb` (`"Database=helloappdb"`).

Подробно про элементы строки подключения к MS SQL Server можно найти здесь: Строка подключения для MS SQL Server.

Теперь определим в файле Program.cs простейшую программу по добавлению и извлечению объектов из базы данных:

```csharp
// добавление данных
using (ApplicationContext db = new ApplicationContext())
{
    db.Database.EnsureDeleted();
    db.Database.EnsureCreated();
    // создаем два объекта User
    User user1 = new User { Name = "Tom", Age = 33 };
    User user2 = new User { Name = "Alice", Age = 26 };

    // добавляем их в бд
    db.Users.AddRange(user1, user2);
    db.SaveChanges();
}
// получение данных
using (ApplicationContext db = new ApplicationContext())
{
    // получаем объекты из бд и выводим на консоль
    var users = db.Users.ToList();
    Console.WriteLine("Users list:");
    foreach (User u in users)
    {
        Console.WriteLine($"{u.Id}.{u.Name} - {u.Age}");
    }
}
```

Консольный вывод:

```
Users list:
1.Tom - 33
2.Alice - 26
```

**Источник:** [https://metanit.com/sharp/efcore/7.1.php](https://metanit.com/sharp/efcore/7.1.php)
