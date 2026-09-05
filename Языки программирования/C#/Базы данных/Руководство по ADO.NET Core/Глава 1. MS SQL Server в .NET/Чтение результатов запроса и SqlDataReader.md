# Чтение результатов запроса и SqlDataReader

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET|Глава 1. MS SQL Server в .NET]] / Чтение результатов запроса и SqlDataReader

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET/Выполнение команд и SqlCommand|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET/Типизация результатов SqlDataReader. Сопоставление типов C# и SQL|Вперёд]]

**Дата написания:** 05.09.2026

Для чтения данных используется метод ExecuteReader/ExecuteReaderAsync, который возвращает объект SqlDataReader:

```csharp
string sqlExpression = "SELECT * FROM Users";
using (SqlConnection connection = new SqlConnection(connectionString))
{
    await connection.OpenAsync();
    SqlCommand command = new SqlCommand(sqlExpression, connection);
    using (SqlDataReader reader = await command.ExecuteReaderAsync())
    {
        if (reader.HasRows)
        {
            while (await reader.ReadAsync())
            {
                object id = reader.GetValue(0);
                object name = reader.GetValue(2);
                object age = reader.GetValue(1);
                Console.WriteLine($"{id} \t{name} \t{age}");
            }
        }
    }
}
```

**Источник:** [https://metanit.com/sharp/adonetcore/2.5.php](https://metanit.com/sharp/adonetcore/2.5.php)
