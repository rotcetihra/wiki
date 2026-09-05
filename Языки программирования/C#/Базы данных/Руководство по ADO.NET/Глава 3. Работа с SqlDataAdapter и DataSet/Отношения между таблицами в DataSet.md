# Отношения между таблицами в DataSet

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET|Руководство по ADO.NET]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Глава 3. Работа с SqlDataAdapter и DataSet]] / Отношения между таблицами в DataSet

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet/DataSet и DataTable|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet/LINQ to DataSet|Вперёд]]

**Дата написания:** 05.09.2026

Для установки отношений между таблицами в DataSet используется класс DataRelation:

```csharp
DataRelation relation = new DataRelation("UsersCompanies",
    ds.Tables["Companies"].Columns["Id"],
    ds.Tables["Users"].Columns["CompanyId"]);
ds.Relations.Add(relation);
```

**Источник:** [https://metanit.com/sharp/adonet/3.7.php](https://metanit.com/sharp/adonet/3.7.php)
