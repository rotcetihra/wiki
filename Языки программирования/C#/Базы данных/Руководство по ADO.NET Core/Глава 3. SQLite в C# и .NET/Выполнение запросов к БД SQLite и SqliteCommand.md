# Выполнение запросов к БД SQLite и SqliteCommand

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET|Глава 3. SQLite в C# и .NET]] / Выполнение запросов к БД SQLite и SqliteCommand

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET/Подключение к базе данных SQLite|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET/Чтение результатов запроса и SqliteDataReader|Вперёд]]

**Дата написания:** 05.09.2026

Для выполнения запросов к SQLite применяется класс SqliteCommand. Методы ExecuteNonQuery, ExecuteReader, ExecuteScalar аналогичны таковым для SqlCommand:

```csharp
using (var connection = new SqliteConnection("Data Source=usersdata.db"))
{
    connection.Open();
    SqliteCommand command = new SqliteCommand();
    command.Connection = connection;
    command.CommandText = "CREATE TABLE Users(_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Name TEXT NOT NULL, Age INTEGER NOT NULL)";
    command.ExecuteNonQuery();
    Console.WriteLine("Таблица Users создана");
}
```

**Источник:** [https://metanit.com/sharp/adonetcore/4.2.php](https://metanit.com/sharp/adonetcore/4.2.php)
