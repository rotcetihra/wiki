# Параметризация запросов к БД Sqlite

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET|Глава 3. SQLite в C# и .NET]] / Параметризация запросов к БД Sqlite

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET/Сопоставление типов C# и SQLite. Типизация SqliteDataReader|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET/Получение скалярных значений в SQLite|Вперёд]]

**Дата написания:** 05.09.2026

Для определения параметров применяется класс SqliteParameter:

```csharp
string sqlExpression = "INSERT INTO Users (Name, Age) VALUES (@name, @age)";
using (var connection = new SqliteConnection("Data Source=usersdata.db"))
{
    connection.Open();
    SqliteCommand command = new SqliteCommand(sqlExpression, connection);

    SqliteParameter nameParam = new SqliteParameter("@name", username);
    command.Parameters.Add(nameParam);

    SqliteParameter ageParam = new SqliteParameter("@age", userage);
    command.Parameters.Add(ageParam);

    int number = command.ExecuteNonQuery();
}
```

Типы SqliteType: `SqliteType.Integer`, `SqliteType.Real`, `SqliteType.Text`, `SqliteType.Blob`.

**Источник:** [https://metanit.com/sharp/adonetcore/4.5.php](https://metanit.com/sharp/adonetcore/4.5.php)
