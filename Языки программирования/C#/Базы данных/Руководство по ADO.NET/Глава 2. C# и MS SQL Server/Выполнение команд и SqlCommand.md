# Выполнение команд и SqlCommand

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET|Руководство по ADO.NET]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 2. C# и MS SQL Server|Глава 2. C# и MS SQL Server]] / Выполнение команд и SqlCommand

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 2. C# и MS SQL Server/Пул подключений|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 2. C# и MS SQL Server|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 2. C# и MS SQL Server/Чтение результатов запроса и SqlDataReader|Вперёд]]

**Дата написания:** 05.09.2026

Для выполнения команд используется класс SqlCommand. Методы ExecuteNonQuery, ExecuteReader, ExecuteScalar:

```csharp
SqlCommand command = new SqlCommand("INSERT INTO Users (Name, Age) VALUES ('Tom', 36)", connection);
int number = command.ExecuteNonQuery();
```

**Источник:** [https://metanit.com/sharp/adonet/2.5.php](https://metanit.com/sharp/adonet/2.5.php)
