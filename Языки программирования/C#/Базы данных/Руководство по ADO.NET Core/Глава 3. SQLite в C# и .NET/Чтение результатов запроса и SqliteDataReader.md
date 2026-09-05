# Чтение результатов запроса и SqliteDataReader

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET|Глава 3. SQLite в C# и .NET]] / Чтение результатов запроса и SqliteDataReader

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET/Выполнение запросов к БД SQLite и SqliteCommand|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET/Сопоставление типов C# и SQLite. Типизация SqliteDataReader|Вперёд]]

**Дата написания:** 05.09.2026

Для чтения данных из SQLite применяется метод ExecuteReader(), который возвращает объект SqliteDataReader:

```csharp
using (var connection = new SqliteConnection("Data Source=usersdata.db"))
{
    connection.Open();
    SqliteCommand command = new SqliteCommand("SELECT * FROM Users", connection);
    using (SqliteDataReader reader = command.ExecuteReader())
    {
        if (reader.HasRows)
        {
            while (reader.Read())
            {
                var id = reader.GetValue(0);
                var name = reader.GetValue(1);
                var age = reader.GetValue(2);
                Console.WriteLine($"{id} \t {name} \t {age}");
            }
        }
    }
}
```

**Источник:** [https://metanit.com/sharp/adonetcore/4.3.php](https://metanit.com/sharp/adonetcore/4.3.php)
