# Методы ExecuteCommand и ExecuteQuery. Хранимые процедуры

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET|Руководство по ADO.NET]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 4. LINQ to SQL|Глава 4. LINQ to SQL]] / Методы ExecuteCommand и ExecuteQuery

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 4. LINQ to SQL/Удаление в LINQ to SQL|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 4. LINQ to SQL|Содержание]]

**Дата написания:** 05.09.2026

Для выполнения SQL-запросов и хранимых процедур используются методы ExecuteCommand и ExecuteQuery:

```csharp
db.ExecuteCommand("DELETE FROM Users WHERE Name={0}", "Tom");
var users = db.ExecuteQuery<User>("SELECT * FROM Users");
```

**Источник:** [https://metanit.com/sharp/adonet/4.6.php](https://metanit.com/sharp/adonet/4.6.php)
