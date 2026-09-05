# Первое приложение на EF Core

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10|Руководство по Entity Framework Core 10]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 1. Введение в Entity Framework Core|Глава 1. Введение в Entity Framework Core]] / Первое приложение на EF Core

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 1. Введение в Entity Framework Core/Что такое Entity Framework Core|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 1. Введение в Entity Framework Core|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 10/Глава 1. Введение в Entity Framework Core/Подключение к существующей базе данных|Вперёд]]

**Дата написания:** 05.09.2026

Итак, создадим первое приложение с использованием Entity Framework Core. Для этого создадим новый проект консольного приложения в Visual Studio или с помощью .NET CLI. Например, используем .NET CLI и выполним следующую команду

```
dotnet new console -o helloapp
```

В данном случае мы создаем проект с именем "helloapp". И для работы с ним перейдем в проект с помощью команды cd:

```
cd helloapp
```

Стоит отметить, что если мы используем .NET CLI, то также лучше установить инструменты для работы с EF Core с помощью команды:

```
dotnet tool install --global dotnet-ef
```

Чтобы начать работать с EntityFramework Core, нам необходимо вначале добавить в проект Nuget-пакет EntityFramework Core. Однако в данном случае нам нужен не общий пакет для Entity Framework Core, а пакет для конкретной СУБД. Так, в данном случае мы будем использовать SQLite в качестве СУБД, поэтому нам надо добавить пакет Microsoft.EntityFrameworkCore.Sqlite. Например, с помощью .NET CLI

```
dotnet add package Microsoft.EntityFrameworkCore.Sqlite
```

Причем пакет надо добавлять, когда мы находимся в консоли внутри папки проекта:

```
eugene@Eugene:/dotnet/efcore$ dotnet new console -o helloapp
The template "Console App" was created successfully.

Processing post-creation actions...
Restoring /dotnet/efcore/helloapp/helloapp.csproj:
Restore succeeded.

eugene@Eugene:/dotnet/efcore$ cd helloapp
eugene@Eugene:/dotnet/efcore/helloapp$ dotnet add package Microsoft.EntityFrameworkCore.Sqlite
.......................................................................................................
.......................................................................................................
log  : Restored /dotnet/efcore/helloapp/helloapp.csproj (in 8.24 sec).
eugene@Eugene:/dotnet/efcore/helloapp$
```

При работе в Visual Studio пакет можно добавить через графическое окно работы с Nuget.

Для проверки добавления пакета мы можем посмотреть на содержимое файла проекта - файла `helloapp.cproj`. Он должен содержать запись о добавлении соответствующего пакета:

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net10.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Microsoft.EntityFrameworkCore.Sqlite" Version="10.0.0" />
  </ItemGroup>

</Project>
```

Итак, необходимые пакеты добавлены. Теперь мы можем их использовать.

Далее нам надо определить модель, которая будет описывать данные. Пусть наше приложение будет посвящено работе с пользователями. Поэтому добавим в проект новый класс User:

```csharp
public class User
{
    public int Id { get; set; }
    public string? Name { get; set; }
    public int Age { get; set; }
}
```

Это обычный класс, который содержит несколько свойств. Каждое свойство будет сопоставляться с отдельным столбцом в таблице из бд.

Надо отметить, что Entity Framework требует определения ключа элемента для создания первичного ключа в таблице в бд. По умолчанию при генерации бд EF в качестве первичных ключей будет рассматривать свойства с именами Id или \[Имя\_класса\]Id (то есть UserId).

Взаимодействие с базой данных в Entity Framework Core происходит посредством специального класса - контекста данных. Поэтому добавим в наш проект новый класс, который назовем ApplicationContext и который будет иметь следующий код:

```csharp
using Microsoft.EntityFrameworkCore;

public class ApplicationContext : DbContext
{
    public DbSet<User> Users => Set<User>();
    public ApplicationContext() => Database.EnsureCreated();

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlite("Data Source=helloapp.db");
    }
}
```

Основу функциональности Entity Framework Core составляют классы, которые располагаются в пространстве имен Microsoft.EntityFrameworkCore. Среди всего набора классов этого пространства имен следует выделить следующие:

-   **DbContext**: определяет контекст данных, используемый для взаимодействия с базой данных
-   **DbSet/DbSet\<TEntity\>**: представляет набор объектов, которые хранятся в базе данных
-   **DbContextOptionsBuilder**: устанавливает параметры подключения

Для работы приложения с базой данной через Entity Framework необходим контекст данных - класс производный от DbContext. В данном случае таким контекстом является класс ApplicationContext.

```csharp
public class ApplicationContext : DbContext
```

И также в классе определено одно свойство Users, которое будет хранить набор объектов User. В классе контекста данных набор объектов представляет класс DbSet\<T\>. Через это свойство будет осуществляться связь с таблицей, где будут храниться данные объектов User.

```csharp
public DbSet<User> Users => Set<User>();
```

Причем этому свойству присваивается начальное значение - результат метода `Set<User>` в виде объекта `DbSet<User>`. В реальности в функциональном плане в этой инициализации мало смысла, она никак не повляет на работу свойства,поскольку все свойства контекста, которые представляют объект DbSet, инициализируются автоматически при создании объкта контекста. Однако поскольку тип DbSet - ссылочный тип, явная инициализация свойств ссылочных типов позволяет нам обойти предупреждения статического анализа для данных ссылочных типов, которые не инициализированны и при этом не допускают значение null.

В качестве альтернативы можно было бы использовать выражение null!

```csharp
public DbSet<User> Users { get; set; } = null!;
```

Кроме того, для настройки подключения нам надо переопределить метод OnConfiguring. Передаваемый в него параметр класса DbContextOptionsBuilder с помощью метода UseSqlite позволяет настроить строку подключения для соединения с базой данных SQLite.

```csharp
optionsBuilder.UseSqlite("Data Source=helloapp.db");
```

В качестве параметра в метод передается строка подключения, которая в данном случае имеет только один параметр - Data Source. Он определяет файл базы данных - в данном случае "helloapp.db".

И также стоит отметить, что по умолчанию у нас нет базы данных. Поэтому в конструкторе класса контекста определен вызов метода `Database.EnsureCreated()`, который при создании контекста автоматически проверит наличие базы данных и, если она отсуствует, создаст ее.

```csharp
public ApplicationContext() => Database.EnsureCreated();
```

Теперь определим сам код программы, который будет взаимодействовать с созданной БД. Для этого изменим файл Program.cs следующим образом:

```csharp
using (ApplicationContext db = new ApplicationContext())
{
    // создаем два объекта User
    User tom = new User { Name = "Tom", Age = 33 };
    User alice = new User { Name = "Alice", Age = 26 };

    // добавляем их в бд
    db.Users.Add(tom);
    db.Users.Add(alice);
    db.SaveChanges();
    Console.WriteLine("Объекты успешно сохранены");

    // получаем объекты из бд и выводим на консоль
    var users = db.Users.ToList();
    Console.WriteLine("Список объектов:");
    foreach (User u in users)
    {
        Console.WriteLine($"{u.Id}.{u.Name} - {u.Age}");
    }
}
```

Так как класс ApplicationContext через базовый класс DbContext реализует интерфейс `IDisposable`, то для работы с ApplicationContext с автоматическим закрытием данного объекта мы можем использовать конструкцию `using`.

В конструкции `using` создаются два объекта User и добавляются в базу данных. Для их сохранения нам достаточно использовать метод `Add`:

```csharp
db.Users.Add(tom);
```

Чтобы получить список данных из бд, достаточно воспользоваться свойством Users контекста данных: `db.Users`

Запустим проект с помощью команды `dotnet run`. И в результате после запуска программа выведет на консоль:

```
eugene@Eugene:/dotnet/efcore/helloapp$ dotnet run
Объекты успешно сохранены
Список объектов:
1.Tom - 33
2.Alice - 26
eugene@Eugene:/dotnet/efcore/helloapp$
```

Поскольку в классе контекста при установке строки подключения к Sqlite указан относительный путь, то после выполнения программы мы можем найти файл базы данных в папке проекта:

```
eugene@Eugene:/dotnet/efcore/helloapp$ ls -l
total 21
drwxrwxrwx 1 root root   144 Nov 19 17:25 bin
-rwxrwxrwx 1 root root   362 Nov 19 17:17 helloapp.csproj
-rwxrwxrwx 1 root root 12288 Nov 19 17:25 helloapp.db
drwxr-xr-x 1 root root  4096 Nov 19 17:25 obj
-rwxrwxrwx 1 root root  1164 Nov 19 17:25 Program.cs
eugene@Eugene:/dotnet/efcore/helloapp$
```

С помощью специальных программ, например, DB Browser for SQLite мы можем посмотреть ее содержимое.

Таким образом, Entity Framework Core обеспечивает простое и удобное управление объектами из базы данных. При том в данном случае нам не надо даже создавать базу данных и определять в ней таблицы. Entity Framework все сделает за нас на основе определения класса контекста данных и классов моделей. И если база данных уже имеется, то EF не будет повторно создавать ее.

**Источник:** [https://metanit.com/sharp/efcore/1.2.php](https://metanit.com/sharp/efcore/1.2.php)
