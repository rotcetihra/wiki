# Обновление БД из DataSet вручную

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET|Руководство по ADO.NET]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Глава 3. Работа с SqlDataAdapter и DataSet]] / Обновление БД из DataSet вручную

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet/SqlCommandBuilder и сохранение изменений DataSet в базе данных|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet/Все операции с БД в графическом приложении|Вперёд]]

**Дата написания:** 05.09.2026

Для ручного обновления устанавливаются команды InsertCommand, UpdateCommand, DeleteCommand:

```csharp
adapter.InsertCommand = insertCommand;
adapter.UpdateCommand = updateCommand;
adapter.DeleteCommand = deleteCommand;
adapter.Update(ds);
```

**Источник:** [https://metanit.com/sharp/adonet/3.4.php](https://metanit.com/sharp/adonet/3.4.php)
