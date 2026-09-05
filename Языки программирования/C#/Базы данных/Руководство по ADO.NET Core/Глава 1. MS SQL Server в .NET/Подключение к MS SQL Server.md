# Подключение к MS SQL Server

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET|Глава 1. MS SQL Server в .NET]] / Подключение к MS SQL Server

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET/Строка подключения для MS SQL Server|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET/Пул подключений|Вперёд]]

**Дата написания:** 05.09.2026

Для работы с базой данных MS SQL Server в .NET необходимо установить через nuget пакет Microsoft.Data.SqlClient. Для создания подключения применяется класс SqlConnection:

```csharp
using Microsoft.Data.SqlClient;

string connectionString = "Server=(localdb)\\mssqllocaldb;Database=master;Trusted_Connection=True;";
using(SqlConnection connection = new SqlConnection(connectionString))
{
    await connection.OpenAsync();
    Console.WriteLine("Подключение открыто");
}
```

**Источник:** [https://metanit.com/sharp/adonetcore/2.2.php](https://metanit.com/sharp/adonetcore/2.2.php)
