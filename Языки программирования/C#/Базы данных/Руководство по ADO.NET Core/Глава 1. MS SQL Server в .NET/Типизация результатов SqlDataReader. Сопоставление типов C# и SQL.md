# Типизация результатов SqlDataReader. Сопоставление типов C# и SQL

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET|Глава 1. MS SQL Server в .NET]] / Типизация результатов SqlDataReader

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET/Чтение результатов запроса и SqlDataReader|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET/Получение скалярных значений|Вперёд]]

**Дата написания:** 05.09.2026

Для получения типизированных данных применяются методы GetInt32(), GetString(), GetDateTime() и т.д.:

```csharp
while (await reader.ReadAsync())
{
    int id = reader.GetInt32(0);
    string name = reader.GetString(2);
    int age = reader.GetInt32(1);
    Console.WriteLine($"{id} \t{name} \t{age}");
}
```

Сопоставление типов SQL и C#:

| Тип SQL | Тип .NET | Метод |
|---------|----------|-------|
| int | Int32 | GetInt32 |
| bigint | Int64 | GetInt64 |
| nvarchar | String | GetString |
| datetime | DateTime | GetDateTime |
| bit | Boolean | GetBoolean |
| decimal | Decimal | GetDecimal |

**Источник:** [https://metanit.com/sharp/adonetcore/2.6.php](https://metanit.com/sharp/adonetcore/2.6.php)
