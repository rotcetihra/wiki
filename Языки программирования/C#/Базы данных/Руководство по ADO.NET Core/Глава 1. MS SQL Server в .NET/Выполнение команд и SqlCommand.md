# Выполнение команд и SqlCommand

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET|Глава 1. MS SQL Server в .NET]] / Выполнение команд и SqlCommand

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET/Пул подключений|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET/Чтение результатов запроса и SqlDataReader|Вперёд]]

**Дата написания:** 05.09.2026

Команды в ADO.NET представлены объектом SqlCommand. Для выполнения команды применяются методы:

-   **ExecuteNonQuery/ExecuteNonQueryAsync**: выполняет sql-выражение и возвращает количество измененных записей (INSERT, UPDATE, DELETE, CREATE)
-   **ExecuteReader/ExecuteReaderAsync**: выполняет sql-выражение и возвращает строки (SELECT)
-   **ExecuteScalar/ExecuteScalarAsync**: выполняет sql-выражение и возвращает одно скалярное значение

```csharp
string connectionString = "Server=(localdb)\\mssqllocaldb;Database=adonetdb;Trusted_Connection=True;";
string sqlExpression = "INSERT INTO Users (Name, Age) VALUES ('Tom', 36)";

using (SqlConnection connection = new SqlConnection(connectionString))
{
    await connection.OpenAsync();
    SqlCommand command = new SqlCommand(sqlExpression, connection);
    int number = await command.ExecuteNonQueryAsync();
    Console.WriteLine($"Добавлено объектов: {number}");
}
```

**Источник:** [https://metanit.com/sharp/adonetcore/2.4.php](https://metanit.com/sharp/adonetcore/2.4.php)
