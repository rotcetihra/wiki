# Чтение результатов запроса и SqlDataReader

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET|Руководство по ADO.NET]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 2. C# и MS SQL Server|Глава 2. C# и MS SQL Server]] / Чтение результатов запроса и SqlDataReader

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 2. C# и MS SQL Server/Выполнение команд и SqlCommand|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 2. C# и MS SQL Server|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 2. C# и MS SQL Server/Типизация результатов SqlDataReader|Вперёд]]

**Дата написания:** 05.09.2026

Для чтения данных используется метод ExecuteReader(), который возвращает SqlDataReader:

```csharp
SqlDataReader reader = command.ExecuteReader();
while (reader.Read())
{
    object id = reader.GetValue(0);
    object name = reader.GetValue(1);
    Console.WriteLine($"{id} \t{name}");
}
reader.Close();
```

**Источник:** [https://metanit.com/sharp/adonet/2.6.php](https://metanit.com/sharp/adonet/2.6.php)
