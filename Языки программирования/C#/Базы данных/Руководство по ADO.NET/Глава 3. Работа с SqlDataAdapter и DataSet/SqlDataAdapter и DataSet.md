# SqlDataAdapter и DataSet

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET|Руководство по ADO.NET]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Глава 3. Работа с SqlDataAdapter и DataSet]] / SqlDataAdapter и DataSet

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 2. C# и MS SQL Server/Сохранение и извлечение файлов из базы данных|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet/Постраничный просмотр в SqlDataAdapter|Вперёд]]

**Дата написания:** 05.09.2026

DataSet представляет хранилище данных в памяти. SqlDataAdapter заполняет DataSet данными из БД:

```csharp
SqlDataAdapter adapter = new SqlDataAdapter(sql, connection);
DataSet ds = new DataSet();
adapter.Fill(ds);
```

**Источник:** [https://metanit.com/sharp/adonet/3.1.php](https://metanit.com/sharp/adonet/3.1.php)
