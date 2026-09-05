# DataSet и XML

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET|Руководство по ADO.NET]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Глава 3. Работа с SqlDataAdapter и DataSet]] / DataSet и XML

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet/LINQ to DataSet|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 4. LINQ to SQL/Определение контекста данных и моделей|Вперёд]]

**Дата написания:** 05.09.2026

DataSet можно сохранять и загружать из XML:

```csharp
ds.WriteXml("data.xml");
DataSet ds2 = new DataSet();
ds2.ReadXml("data.xml");
```

**Источник:** [https://metanit.com/sharp/adonet/3.9.php](https://metanit.com/sharp/adonet/3.9.php)
