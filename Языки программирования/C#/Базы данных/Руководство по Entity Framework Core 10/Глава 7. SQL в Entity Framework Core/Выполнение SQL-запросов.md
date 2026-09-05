# Выполнение SQL-запросов

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10|Руководство по Entity Framework Core 10]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 7. SQL в Entity Framework Core|Глава 7. SQL в Entity Framework Core]] / Выполнение SQL-запросов

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 6. Запросы и LINQ to Entities/Массовое обновление и удаление. ExecuteUpdate и ExecuteDelete|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 7. SQL в Entity Framework Core|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 7. SQL в Entity Framework Core/Хранимые функции|Вперёд]]

**Дата написания:** 05.09.2026

Кроме использования инфраструктуры LINQ to Entities для создания запросов Entity Framework Core также позволяет писать запросы к базе данных сразу на языке SQL. Это может быть удобно, если запрос очень сложный по своей структуре или если Entity Framework Core на основе Linq to Entities создает не очень оптимальный sql-запрос.

## FromSqlRaw

Для получения данных из БД у объектов DbSet определен метод FromSqlRaw(), который принимает в качестве параметра sql-выражение и набор параметров. В качестве результата FromSqlRaw возвращает набор полученных из бд объектов.

```csharp
using (ApplicationContext db = new ApplicationContext())
{
    var comps = db.Companies.FromSqlRaw("SELECT * FROM Companies").ToList();
    foreach (var company in comps)
        Console.WriteLine(company.Name);
}
```

### Параметры

Другая версия метода `FromSqlRaw()` позволяет использовать параметры. Например, выберем из бд все модели, в названии которых есть подстрока "Tom":

```csharp
using Microsoft.Data.Sqlite;

using (ApplicationContext db = new ApplicationContext())
{
    SqliteParameter param = new SqliteParameter("@name", "%Tom%");
    var users = db.Users.FromSqlRaw("SELECT * FROM Users WHERE Name LIKE @name", param).ToList();
    foreach (var user in users)
        Console.WriteLine(user.Name);
}
```

Также мы можем определять параметры как простые переменные:

```csharp
using (ApplicationContext db = new ApplicationContext())
{
    var name = "%Tom%";
    var users = db.Users.FromSqlRaw("SELECT * FROM Users WHERE Name LIKE {0}", name).ToList();
    foreach (var user in users)
        Console.WriteLine(user.Name);

    var age = 30;
    users = db.Users.FromSqlRaw("SELECT * FROM Users WHERE Age > {0}", age).ToList();
    foreach (var user in users)
        Console.WriteLine(user.Name);
}
```

### ExecuteSqlRaw

Метод `FromSqlRaw()` осуществляет выборку из БД, но кроме выборки нам, возможно, придется удалять, обновлять уже существующие или вставлять новые записи. Для этой цели применяется метод ExecuteSqlRaw() и его асинхронная версия - ExecuteSqlRawAsync(), которые возвращают количество затронутых командой строк. Для его вызова у контекста данных используется свойство `Database`:

```csharp
// вставка
string newComp = "Apple";
int numberOfRowInserted = db.Database.ExecuteSqlRaw("INSERT INTO Companies (Name) VALUES ({0})", newComp);

// обновление
string appleInc = "Apple Inc.";
string apple = "Apple";
int numberOfRowUpdated = db.Database.ExecuteSqlRaw("UPDATE Companies SET Name={0} WHERE Name={1}", appleInc, apple);

// удаление
int numberOfRowDeleted = db.Database.ExecuteSqlRaw("DELETE FROM Companies WHERE Name={0}", appleInc);
```

### Интерполяция строк

Для методов FromSqlRaw и ExecuteSqlRaw в EF Core определены их двойники - методы FromSqlInterpolated() и ExecuteSqlInterpolated() (асинхронная версия - ExecuteSqlInterpolatedAsync()), которые позволяют использовать интерполяцию строк для передачи параметров:

```csharp
using (ApplicationContext db = new ApplicationContext())
{
    var name = "%Tom%";
    var age = 30;
    var users = db.Users.FromSqlInterpolated($"SELECT * FROM Users WHERE Name LIKE {name} AND Age > {age}").ToList();
    foreach (var user in users)
        Console.WriteLine(user.Name);
}
```

**Источник:** [https://metanit.com/sharp/efcore/6.1.php](https://metanit.com/sharp/efcore/6.1.php)
