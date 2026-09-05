# DataSet и DataTable

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET|Руководство по ADO.NET]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Глава 3. Работа с SqlDataAdapter и DataSet]] / DataSet и DataTable

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet/Все операции с БД в графическом приложении|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet/Отношения между таблицами в DataSet|Вперёд]]

**Дата написания:** 05.09.2026

DataSet содержит DataTable, которые состоят из DataColumn и DataRow. DataSet можно создавать и без подключения к БД:

```csharp
DataSet ds = new DataSet();
DataTable dt = new DataTable("Users");
ds.Tables.Add(dt);
DataColumn col = new DataColumn("Name", typeof(string));
dt.Columns.Add(col);
```

**Источник:** [https://metanit.com/sharp/adonet/3.6.php](https://metanit.com/sharp/adonet/3.6.php)
