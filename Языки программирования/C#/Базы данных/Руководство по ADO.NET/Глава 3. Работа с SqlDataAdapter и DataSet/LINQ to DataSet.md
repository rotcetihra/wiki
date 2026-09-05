# LINQ to DataSet

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET|Руководство по ADO.NET]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Глава 3. Работа с SqlDataAdapter и DataSet]] / LINQ to DataSet

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet/Отношения между таблицами в DataSet|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet/DataSet и XML|Вперёд]]

**Дата написания:** 05.09.2026

Для работы с данными в DataSet используется LINQ:

```csharp
var users = ds.Tables["Users"].AsEnumerable()
    .Where(row => row.Field<int>("Age") > 30);
```

**Источник:** [https://metanit.com/sharp/adonet/3.8.php](https://metanit.com/sharp/adonet/3.8.php)
