# SqlCommandBuilder и сохранение изменений DataSet в базе данных

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET|Руководство по ADO.NET]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Глава 3. Работа с SqlDataAdapter и DataSet]] / SqlCommandBuilder и сохранение изменений DataSet в базе данных

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet/Постраничный просмотр в SqlDataAdapter|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet/Обновление БД из DataSet вручную|Вперёд]]

**Дата написания:** 05.09.2026

SqlCommandBuilder автоматически генерирует команды для сохранения изменений:

```csharp
SqlCommandBuilder commandBuilder = new SqlCommandBuilder(adapter);
adapter.Update(ds);
```

**Источник:** [https://metanit.com/sharp/adonet/3.3.php](https://metanit.com/sharp/adonet/3.3.php)
